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


def index(request):
    return HttpResponse(
        'Hello, World. This is Django running on Google App Engine')


class ErrorView(View):

    def get(self, request, *args, **kwargs):
        Exception("Woops.. an Error Occurred")


class ClassView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("This was a successful response")


class HealthCheckView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("OK")
