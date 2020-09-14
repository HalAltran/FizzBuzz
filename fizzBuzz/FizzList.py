class FizzList:
    def __init__(self, x):
        self.object_list = []
        self.eff_list = []
        self.bee_list = []
        self.reverse = False
        self.x = x

    def add_object(self, fizz_object):
        if fizz_object[0] == "F":
            self.eff_list.append(fizz_object)
        elif fizz_object[0] == "B":
            self.bee_list.append(fizz_object)
        elif fizz_object == "Reverse":
            self.reverse = True

    def contains(self, name):
        if name in self.object_list:
            return True

    def format_output(self):
        output_list = []
        output_list += self.eff_list

        if self.contains("Fezz"):
            output_list.append("Fezz")
        output_list += self.bee_list
        if self.contains("Bong"):
            output_list = []
            if self.contains("Fezz"):
                output_list.append("Fezz")
            output_list.append("Bong")

        output = ""
        if len(output_list) > 0:
            if self.reverse:
                output_list.reverse()
                output += "".join(output_list)
            else:
                output += "".join(output_list)
        else:
            return str(self.x)

        return output
