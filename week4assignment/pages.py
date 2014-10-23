__author__ = 'jacobritenour'


class Page(object):#adding Page class to load initial page
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = ''
        self._close = '''
    </body>
</html>'''
    def print_initial(self):
        return self._head + self._body + self._close