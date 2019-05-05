

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        print(request.META.get('HTTP_ORIGIN',None))
        print(request.META.get('PATH_INFO',None))
        print(request.META.get('HTTP_COOKIE',None))
        print(request.META.get('REQUEST_METHOD',None))
        print(request.META.get('PATH_INFO',None))

        # Code to be executed for each request/response after
        # the view is called.

        return response