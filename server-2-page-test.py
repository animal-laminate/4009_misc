import cherrypy
import datetime
import jinja2, os

ROOTDIR = os.path.dirname(os.path.abspath(__file__)) 
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(ROOTDIR,'templates')),extensions=['jinja2.ext.autoescape'])

config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 3000                                 #change your port number if necessary
    },
    '/': {
        'tools.staticdir.root': os.path.join(ROOTDIR,'static')
    },
    '/css': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'css'
    },
    '/img': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'images'
    }
}

class Website:
    @cherrypy.expose
    def index(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')

        now = datetime.datetime.now()
        template_values = { 'time': now.strftime("%I:%M %P on %A %e/%-m/%Y"), \
                            'ustime': now.strftime("%-m/%e/%Y") }

        return template.render(template_values)
    
    @cherrypy.expose
    def sub(self):
        template = JINJA_ENVIRONMENT.get_template('points-and-lines.html')

        now = datetime.datetime.now()
        template_values = { 'time': now.strftime("%I:%M %P on %A %e/%-m/%Y"), \
                            'ustime': now.strftime("%-m/%e/%Y") }

        return template.render(template_values)

if __name__ == '__main__':
    cherrypy.quickstart(Website(), '/', config)
