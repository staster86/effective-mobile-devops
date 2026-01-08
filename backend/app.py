import http.server
import socketserver

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

# Сервер слушает только внутри Docker-сети на порту 8080
with socketserver.TCPServer(("", 8080), CustomHandler) as httpd:
    print("Сервер запущен на порту 8080")
    httpd.serve_forever()