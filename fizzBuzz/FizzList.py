from fizzBuzz import FizzObject


class FizzList:
    def __init__(self, x: int):
        self.object_list = []
        self.reverse = False
        self.x = x

    def add_object(self, fizz_object: FizzObject):
        self.object_list.append(fizz_object)

    def format_output(self):
        if any(fizz_object.delete_others for fizz_object in self.object_list):
            for fizz_object in self.object_list:
                if not fizz_object.permanent:
                    self.object_list.remove(fizz_object)

        self.object_list = sorted(self.object_list, key=lambda fizz_object_2: fizz_object_2.priority)
        if self.reverse:
            self.object_list.reverse()
        names = (fizz_object.name for fizz_object in self.object_list)
        if len(self.object_list) == 0:
            return str(self.x)

        return "".join(names)
