from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head><title>dhanvarsini</title>
    </head>
    <body>
        <table border = '5' cellpadding='5' cellspacing='10'>
            <tr>
                <th colspan="4">Lap Configurations(Dhanvarsini)cd</th>
            </tr>

                <tr bgcolour="red">
                <td>S.no</td>
                <td>Device Specification</td>
                <td>ans</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Device name</td>
                <td>dhanvarsini</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Processor</td>
                <td>13th gen</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed ram</td>
                <td>16.0</td>
            </tr>
            <tr>
                <td>4</td>
                <td>device id</td>
                <td>E39825b0</td>
            </tr>
            <tr>
                <td>5</td>
                <td>system id</td>
                <td>64 bit</td>
            </tr>
        </table>
    </body>
    </html>
    """
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()