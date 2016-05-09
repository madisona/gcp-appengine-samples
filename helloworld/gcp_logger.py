
import logging
import json
import os


class GCPJsonFormatter(logging.Formatter):

    def format(self, record):
        # https://cloud.google.com/error-reporting/docs/formatting-error-messages
        return json.dumps({
            'eventTime': record.created,
            'message': self.formatException(record.exc_info),
            'level': record.levelname,
            'serviceContext': {
                'service': os.environ.get('GAE_MODULE_NAME', ''),
                'version': os.environ.get('GAE_MODULE_VERSION', ''),
            },
            "context": {
                "httpRequest": self._get_request_info(record),
                'user': str(record.request.user) if record.request else "",
                "reportLocation": {
                    "filePath": record.pathname,
                    "lineNumber": record.lineno,
                    "functionName": record.funcName,
                },
            }
        })

    def _get_request_info(self, record):
        try:
            request = record.request
            return {
                "method": request.method,
                "url": request.get_full_path(),
                "userAgent": request.META.get("HTTP_USER_AGENT", ""),
                "referrer": request.META.get("HTTP_REFERER", ""),
                "responseStatusCode": record.status_code,
                "remoteIp": request.META.get("REMOTE_ADDR", "")
            }
        except Exception:
            return {}
