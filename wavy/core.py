class Application:

    def __init__(self, routes: dict, front_controllers: list):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        view = self.routes.get(path, None)
        if not view:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Page not found"]
        request = {}
        for front_controller in self.front_controllers:
            front_controller(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
