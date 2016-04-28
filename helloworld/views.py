#!/usr/bin/env python
# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from django.http import HttpResponse
from django.views.generic import View

from fluent import sender
from fluent import event
import traceback

sender.setup('myapp', host='localhost', port=24224)


def report(ex):
    data = {}
    data['message'] = '{0}'.format(ex)
    data['serviceContext'] = {'service' : 'myapp'}
    # ... add more metadata
    event.Event('errors', data)


def index(request):
    return HttpResponse(
        'Hello, World. This is Django running on Google App Engine')


class ErrorView(View):

    def get(self, request, *args, **kwargs):
        # report exception data using:
        try:
            Exception("Woops.. an Error Occurred")
        except Exception as e:
            report(traceback.format_exc())
            raise e


class ClassView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("This was a successful response")


class HealthCheckView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("OK")
