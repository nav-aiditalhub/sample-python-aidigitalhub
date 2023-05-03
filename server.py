import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! Everyone, you requested %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port Nav %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello Tutorialspoint'

if __name__ == '__main__':
   app.run()