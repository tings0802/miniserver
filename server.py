from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == '/':
            self.path = 'index.html'
        super().do_GET()
        
def run(server=HTTPServer, handler=Handler, domain='127.0.0.1', port=8000):
    try:
        daemon = server((domain, port), handler)
        print(f'Serving on http://{domain}:{port}')
        daemon.serve_forever()
    except KeyboardInterrupt:
        print(f'Server stopped')

run()