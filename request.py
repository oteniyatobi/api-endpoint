import http.server
import socketserver

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        import json

        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        a = float(params['a'][0])
        b = float(params['b'][0])

        if parsed.path == '/add':
            result = add(a, b)
        elif parsed.path == '/subtract':
            result = subtract(a, b)
        elif parsed.path == '/multiply':
            result = multiply(a, b)
        elif parsed.path == '/divide':
            result = divide(a, b)
        response = json.dumps({'result': result})
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode())

with socketserver.TCPServer(("", 7000), MyHandler) as server:
    server.serve_forever()