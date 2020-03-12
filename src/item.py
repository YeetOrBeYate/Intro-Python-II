
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return_string = f"{self.name}-{self.description}"
        return_string += "\n\n"
        return return_string

class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories

    def __str__(self):
        return_string = f"{self.name}-{self.description}"
        return_string += "\n\n"
        return_string += f"calories:{self.calories}"
        return_string += "\n\n"
        return return_string


class Tool(Item):
    def __init__(self, name, description, size):
        super().__init__(name, description)
        self.size = size

    
    def __str__(self):
        return_string = f"{self.name}-{self.description}"
        return_string += "\n\n"
        return_string += f"size:{self.size}"
        return_string += "\n\n"
        return return_string