import re


class bagRules():
    def __init__(self, file_path):
        self.input_rules = self._load_file(file_path)
        self.rule_dict = self._build_rule_dict()

    @staticmethod
    def _load_file(file_path):
        with open(file_path, "r") as input_file:
            return input_file.readlines()

    def _build_rule_dict(self):
        rule_dict = dict()
        for rule in self.input_rules:
            container_bag_name = re.match("^(\w+\s){2}",
                                          rule).group(0).rstrip(' ')
            items_contained = [
                (count, color.rstrip(' '))
                for (count, color,
                     _) in re.findall("(\d+)\s((\w+\s){2})bags?", rule)
            ]
            rule_dict[container_bag_name] = items_contained
        return rule_dict

    def get_count_inside_bag(self, color):
        print(color)
        print(self.rule_dict[color])
        if self.rule_dict[color] == []:
            return 0
        else:
            count = 0
            for bag in self.rule_dict[color]:
                (subcount, subcolor) = bag
                count += int(subcount) * (1 +
                                          self.get_count_inside_bag(subcolor))
            return count


if __name__ == "__main__":
    day_07 = bagRules('input_file.txt')
    print(day_07.get_count_inside_bag("shiny gold"))
