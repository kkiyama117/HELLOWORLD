from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return ["Hello World".encode("utf-8"), ]


if __name__ == '__main__':
    with make_server('', 8080, simple_app) as httpd:
        print("Serving on port 8080...")
        httpd.serve_forever()
