__author__ = 'jacobritenour'

'''
Jacob Ritenour
10/9/2014
DPFWP
Simple Form
'''

import webapp2 #using webapp2 library

class MainHandler(webapp2.RequestHandler): #making a class
    def get(self): #function that is going to make everything work
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''
        page_body = '''<form method="GET">
            <label>Name</label><input type="text" name="username" />
            <label>Email</label><input type="text" name="email" />
            <label>Date of Birth</label><input type="text" name="dob" />
            <label>Email</label><input type="text" name="email" />
            <input type="submit" value="Submit" />'''
