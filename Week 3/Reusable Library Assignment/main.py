__author__ = 'jacobritenour'


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("hello world")
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)