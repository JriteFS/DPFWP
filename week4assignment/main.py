'''
Jacob Ritenour
10/21/2014
DPFWP
Week 4 Assignment Dynamic Site
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
