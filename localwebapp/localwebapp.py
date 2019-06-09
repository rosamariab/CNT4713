
import http.server
import socketserver

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

handler.extensions_map={
        '.manifest': 'text/cache-manifest',
	'.html': 'text/html',
    '.png': 'image/png',
	'.jpg': 'image/jpg',
	'.svg':	'image/svg+xml',
	'.css':	'text/css',
    '.mp4' : 'video/mp4',
    '.aac' : 'audio/aac',
	'.js':	'application/x-javascript',
	'': 'application/octet-stream', # Default
    }

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()