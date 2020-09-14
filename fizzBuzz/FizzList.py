class FizzList:
    def __init__(self, x):
        self.eff_list = []
        self.bee_list = []
        self.reverse = False
        self.x = x

    def add_object(self, rule_name):
        if rule_name[0] == "F":
            self.eff_list.append(rule_name)
        elif rule_name[0] == "B":
            self.bee_list.append(rule_name)
        elif rule_name == "Reverse":
            self.reverse = True

    def contains(self, name: str):
        if name in self.eff_list:
            return True
        if name in self.bee_list:
            return True
        return False

    def format_output(self):
        output_list = []
        output_list += self.eff_list + self.bee_list

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
