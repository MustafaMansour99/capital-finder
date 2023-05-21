from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 #handle a request for me 
 #methode to handle HTTP Get request
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        mustafa ="Hello Mustafa"
        self.wfile.write(mustafa.encode('utf-8'))
        return