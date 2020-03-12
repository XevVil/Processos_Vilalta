from http.server import HTTPServer, BaseHTTPRequestHandler
import smtplib
import ssl


hostname = 'localhost'
port = 8080
class Server(BaseHTTPRequestHandler):
    """docstring for Server."""

    def do_GET(self):
        if self.path == "/practica":

            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            image = open('/home/xavier/Imatges/PC.png', 'rb')
            self.wfile.write(image.read())


            contra = "xavi121996"
            msg = """
            Subject: Imatge rebuda


            conexió:%s
             """ % str(self.client_address)

            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.ehlo()
            server.login("xvilalta96@gmail.com",contra)
            server.sendmail("xvilalta96@gmail.com","xvilalta96@gmail.com",msg)
            server.quit()




        else:
            self.send_error(404,"HTTP/1.1 404 Not Found")




httpd = HTTPServer((hostname, port), Server)
httpd.serve_forever()
