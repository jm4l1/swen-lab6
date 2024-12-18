import http.server
import ssl

server_address = ('swen2003.example.com', 50000)
httpd = http.server.HTTPServer(
    server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='cert.pem',
                               keyfile='key.pem',
                               ssl_version=ssl.PROTOCOL_TLS)

httpd.serve_forever()
