from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import datetime
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Asia/Jakarta")

OPEN_TIME = datetime.time(18, 00, 20)  # ⏰ JAM WAR WIB

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status":
            now = datetime.datetime.now(TZ)
            now_time = now.time()

            enabled = now_time >= OPEN_TIME

            data = {
                "enabled": enabled,
                "server_time": now.strftime("%H:%M:%S.%f")[:-3],
                "open_time": OPEN_TIME.strftime("%H:%M:%S"),
                "timezone": "Asia/Jakarta (WIB)"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

server = HTTPServer(("localhost", 8001), Handler)
print("Server running (WIB) at http://localhost:8001")
server.serve_forever()
