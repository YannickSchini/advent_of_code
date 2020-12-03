class localGeology():


    def __init__(self, file_path):
        with open (file_path, "r") as myfile:
            list_of_lines = myfile.readlines()
            list_of_lines = [x.strip() for x in list_of_lines]
        self.terrain = list_of_lines

    def test(self):
        print(self.terrain)


if __name__=="__main__":
    day3 = localGeology('test_terrain.txt')
    day3.test()
