from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        if self.path in ("/healthz", "/ready"):
            self.wfile.write(b"ok")
        else:
            self.wfile.write(b"Hello World from EKS! - Production\n")

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()