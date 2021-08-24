# Import the server module

import http.server


# Set the hostname and port number

HOST = "localhost"

PORT = 4000

# Define class to display the leaflet page of the web server

class PythonServer(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/':

            self.path = 'leaflet.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Declare object of the class

webServer = http.server.HTTPServer((HOST, PORT), PythonServer)


# Print the URL of the webserver

print("Server started http://%s:%s" % (HOST, PORT))


try:
    # Run the web server

    webServer.serve_forever()

except KeyboardInterrupt:

    # Stop the web server

    webServer.server_close()

    print("The server is stopped.")
