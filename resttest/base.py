from __future__ import unicode_literals, print_function, division
from unittest import TestCase
import httplib2

class Request(object):
    def __init__(self, path, method, headers={}, credentials=None, body=''):
        self.path = path
        self.method = method
        self.headers = headers
        self.credentials = credentials
        self.body = body

class Response(object):
    def __init__(self, status, headers=None, body=''):
        self.status = status
        self.headers = headers
        self.body = body

class RestCase(TestCase):
    def __init__(self, name, request, response, context={}, depends_on=[], host=None):
        super(RestCase, self).__init__()
        self.name = name
        self.context = context
        self.depends_on = depends_on
        self.request = request
        self.response = response
        self.host = host
        if context:
            request.body=request.body % context
            response.body=response.body % context

    def __str__(self):
        return self.name

    def _rest_call(self):
        h = httplib2.Http()
        if self.request.credentials:
            h.add_credentials(self.request.credentials['name'], self.request.credentials['password'])
        return h.request(self.host+self.request.path,
                                  self.request.method,
                                  self.request.body,
                                  headers=self.request.headers)
    def runTest(self):
        for case in self.depends_on:
            case._rest_call()
        resp, content = self._rest_call()
        self.assertEquals(self.response.status, resp.status)
        self.assertEquals(self.response.body, content)

class suite:
    def __init__(self, context, setup, teardown, tests):
        self.context = context
        self.setup = setup
        self.teardown = teardown
        self.tests = tests
