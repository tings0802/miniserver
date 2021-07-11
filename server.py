from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def __respond(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def __render(self, template):
        self.__respond()
        with open(template, 'r') as content:
            self.wfile.write(content.read().encode('utf-8'))

    def do_GET(self):
        print(f'GET request for {self.path}')

        if self.path == '/form':
            html = 'form.html'
        else:
            html = 'index.html'
        
        self.__render(html)

    def do_POST(self):
        print(f'POST request for {self.path}'.encode('utf-8'))

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self.__render('form.html')

def run(server=HTTPServer, handler=Handler, port=8000):
    domain = '127.0.0.1'
    httpd = server((domain, port), handler)
    print(f'Serving HTTP on http://{domain}:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('\rHTTP daemon stopped')

if __name__ == '__main__':
    run()
