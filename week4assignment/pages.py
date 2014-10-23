__author__ = 'jacobritenour'


class Page(object):#adding Page class to load initial page
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Types of SuperNatural Beings</title>
    </head>
    <body>
        <h1>What Type of Super-Natural Being do You Relate Too?</h1>
        <section>
            <p>There are many types of different supernatural beings that have been thought up through out history. Listed below are a few that you can review and see which one you most closely resemble. The abilities of these creatures or beings can range from immortality or shape-shifting to super-speed and the strength of 100 men. There has been such a large imagination on creating different characters that in order to be unique you have to combine several of these abilities. Vampires, Werewolves, Mermaids/Mermen, Witches/Warlocks, and a few others are listed below so you can compare and possibly relate. </p>
        </section>

    '''

        self._body = ''
        self._close = '''
    </body>
</html>'''
    def print_initial(self):
        return self._head + self._body + self._close