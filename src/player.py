# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room= current_room
        self.items = []

    def print_info(self):
        makeString = ''.join(str(x) for x in self.items)
        print(f"{self.name}, Your items:{makeString} {self.current_room}")
        

    def grab_item(self, cmd):
        if cmd == 'grab':
            self.items.extend(self.current_room.items)
            self.current_room.items.clear()
            self.print_info()
        else:
            self.current_room.items.extend(self.items)
            self.items.clear()
            self.print_info()


    def travel(self,direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            self.print_info()
        else:
            print('You cant move in that direction')

