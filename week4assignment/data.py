__author__ = 'jacobritenour'


class DataObject(object):#created the class for data object
    def __init__(self):# initiate the class
        self.name = ""
        self.type = ""
        self.trigger = ""
        self.food = ""
        self.reproduce = ""
        self.life_span = ""
        self.main_ability = ""
        self.weakness = ""

    def print_types(self):
        return "Do you resemble a " + self.name