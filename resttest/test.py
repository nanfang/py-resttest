import unittest
from resttest.base import RestCase, Request, Response


def rest_case(name, request, response):
    return RestCase(name=name, request=request, response=response)

test_case_1 = RestCase(name='test echo service',
                       context={
                           'name': 'nanfang'
                       },
                       request=Request(
                           path='/echo',
                           method='POST',
                           headers={},
                           body='hello: %(name)s'
                       ),
                       response=Response(
                           status=200,
                           body='echo: fhello: %(name)s'
                       ),
                       host='http://localhost:5000'
                       )

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(test_case_1)