import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Vulnerable: allows writing data sent by attacker to the container's filesystem
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length).decode('utf-8')
        with open('data/owned.txt', 'w') as f:
            f.write(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Success')

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving on port", PORT)
        httpd.serve_forever()
