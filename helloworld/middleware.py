
import sys


class LiveDebuggerTestMiddleware(object):

    def process_request(self, request):
        a = "Aaron"
        b = request.GET.get("name", "Madison")
        c = "{a} {b}".format(a=a, b=b)
        sys.stdout.write("User is: {}".format(c))
