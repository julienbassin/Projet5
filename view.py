import logging


class MenuItem():

    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __str__(self):
        return self.name

    def cls(self):
        print(80*'\n')

    def read_number(self, text = ''):
        INP='>>'
        text += '\n' + INP if text else INP
        str = ''
        try:
            str = input(text)
            return int(str)
        except ValueError:
            self.press_enter("Error value: '{}'! Enter please the number".format(str))
            return -1

    def press_enter(self, str = ''):
        str += '\nPress Enter'
        input(str)


class Menu(MenuItem):

    def __init__(self, name):
        MenuItem.__init__(self, name, self.show_menu)
        self.items={}

    def add_item(self, item):
        self.items[len(self.items) + 1] = item

    def show_menu(self):
        choice = -1
        while choice:
            self.cls()
            print(self)
            choice = self.read_number()
            if choice in self.items:
                self.items[choice].action()

    def __str__(self):
        res_str = self.name + ':\n0: Exit'
        for i in self.items.keys():
            res_str += str.format('\n{}: {}', i, self.items[i].name)
        return res_str

