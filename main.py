import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

if __name__ == '__main__':
    with socketserver.TCPServer(('', PORT), Handler) as server:
        print(f'Hosting server on port {PORT}')
        server.serve_forever()