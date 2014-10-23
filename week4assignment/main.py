'''
Jacob Ritenour
10/21/2014
DPFWP
Week 4 Assignment Dynamic Site
'''
import webapp2
from pages import Page
from data import DataObject


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()# created instance of Page
        d = DataObject() #created instance of Data Object


        werewolf = DataObject()
        werewolf.type = "Shape Shifter"
        werewolf.trigger = "Full Moon"
        werewolf.food = "Mainly meat, but can eat anything almost (see weaknesses)"
        werewolf.reproduce = "Some are born this way others are bitten and gain the ability after the first full moon"
        werewolf.life_span = "Some sources say they are immortal, others say they grow older and die, there may be a bit of both"
        werewolf.main_ability = "Shape Shifting to gain claws and large teeth. Gaining enormous strength and speed and the ability to scent out just about anything. There are rumors of them changing into a very large wolf and other that say they change into a large hairy beast with the snout and teeth of a wolf but stand like a man.Along with the ability to heal very quickly."
        werewolf.weakness = "Werewolves are weak against silver and wolvesbayne. This herb burns away at the flesh and the silver causes a very bad allergic reaction. Another weakness, yet not really a weakness but a caution is that on a full moon they tend to loss control of themselves to beast inside."


        vampire = DataObject()
        vampire.type = "Nocturnal Superbeing"
        vampire.trigger = "Being Bitten - Sustained"
        vampire.food = "Blood"
        vampire.reproduce = "Can not"
        vampire.life_span = "Immortal"
        vampire.main_ability = "Super Strength and gets stronger the longer they live. Super senses, hearing, taste, touch, sight, everything. The ability to convince others to do their bidding called Compulsion.The ability to heal very quickly and see the memories of those they consume the blood from."
        vampire.weakness = "The sun lights them on fire. A stake to the heart, cutting off their head, or ripping their heart out will kill them."

        mermaid = DataObject()
        mermaid.type = ""
        mermaid.trigger = ""
        mermaid.food = ""
        mermaid.reproduce = ""
        mermaid.life_span = ""
        mermaid.main_ability = ""
        mermaid.weakness = ""

        witch = DataObject()
        witch.type = ""
        witch.trigger = ""
        witch.food = ""
        witch.reproduce = ""
        witch.life_span = ""
        witch.main_ability = ""
        witch.weakness = ""




        self.response.write(p.print_initial())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
