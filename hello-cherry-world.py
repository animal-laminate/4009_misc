'''simple Hello World which specifies a remote host and port (not localhost) to make use of codio box'''

import cherrypy

class HelloWorld(object):
    @cherrypy.expose                                                            #use cherrypy
    @cherrypy.tools.gzip()                                                      #use cherrypy configuration tools                                                    
    def index(self):                                                            #method 
        return "Hello 4009CEM-world from Dr John Halloran!"                                           #returns string (will appear in browser)

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})                   #configure host (not 127.0.0.1)
    cherrypy.config.update({'server.socket_port': 3000})                        #configure port                 
    cherrypy.quickstart(HelloWorld(), '/', {'/': {'tools.gzip.on': True}})      #start application; provide configuration support
