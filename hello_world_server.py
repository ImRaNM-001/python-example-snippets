""" from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello PE Engineering - GoodBye!")  # this will be printed as a response when you request /
        else:
            self.send_error(404, "File not found")

def run(server_class=HTTPServer, handler_class=HelloWorldHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on port {port}")
    httpd.serve_forever()  # this will start the HTTP server (blocking operation) and listen on port 8080

if __name__ == '__main__':
    run() """

# print('Hello World')
    
# using file writing,

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from datetime import datetime

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Record new visit
        timestamp = datetime.now().isoformat() + "\n"
        os.makedirs("data", exist_ok=True)
        with open("data/visits.txt", "a") as f:
            f.write(timestamp)

        # Read and display all visits
        try:
            with open("data/visits.txt", "r") as f:
                data = f.read()
        except IOError:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error reading visits!")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello PE Engineering!\n")
        response = f"New visit recorded at {timestamp}\n\nAll visits:\n{data}"
        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()


    """
    from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from datetime import datetime

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Record new visit
        timestamp = datetime.now().isoformat() + "\n"
        os.makedirs("data", exist_ok=True)
        with open("data/visits.txt", "a") as f:
            f.write(timestamp)

        # Read and display all visits
        try:
            with open("data/visits.txt", "r") as f:
                data = f.read()
        except IOError:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error reading visits!")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello PE Engineering!\n\n")
        response = f"New visit recorded at {timestamp}\n\nAll visits:\n{data}"
        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

    """