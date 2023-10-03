import http.server
import socketserver

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check the requested URL
        if self.path == "/Fetch_AuditLogs.html":
            # Serve the specific file
            return super().do_GET()
        else:
            # Respond with a 403 Forbidden status code for all other URLs
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Forbidden')

if __name__ == "__main__":
    PORT = 8000 # You can replace 8000 with any Port you want to use
    with socketserver.TCPServer(("Your Machine IP", PORT), CustomHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
