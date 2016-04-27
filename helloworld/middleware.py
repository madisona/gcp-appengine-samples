
import logging


class LiveDebuggerTestMiddleware(object):

    def process_request(self, request):
        logging.info("User is: {}".format(request.user))
