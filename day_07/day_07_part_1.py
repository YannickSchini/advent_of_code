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
                x.rstrip(' ')
                for (x, _) in re.findall("\d+\s((\w+\s){2})bags?", rule)
            ]
            rule_dict[container_bag_name] = items_contained
        return rule_dict

    def _find_bags_that_contain_key(self, key):
        return [
            color for color in self.rule_dict.keys()
            if key in self.rule_dict[color]
        ]

    def get_available_options(self):
        list_of_colors_to_check = self._find_bags_that_contain_key(
            "shiny gold")
        set_of_available_options = set(list_of_colors_to_check)
        while len(list_of_colors_to_check) > 0:
            list_of_additional_containers = self._find_bags_that_contain_key(
                list_of_colors_to_check.pop())
            for container in list_of_additional_containers:
                set_of_available_options.add(container)
                list_of_colors_to_check.append(container)
        return set_of_available_options


if __name__ == "__main__":
    day_07 = bagRules('input_file.txt')
    print(len(day_07.get_available_options()))
