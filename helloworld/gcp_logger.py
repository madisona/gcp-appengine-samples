
import logging
import json


class GCPJsonFormatter(logging.Formatter):

    def format(self, record):
        return json.dumps({
            'message': '{0}'.format(record.getMessage()),
            'user': str(record.request.user),
            'level': record.levelname,
            'traceback': self.formatException(record.exc_info),
            'serviceContext': {'service': 'myapp'}
        })
