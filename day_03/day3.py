class localGeology():


    def __init__(self, file_path):
        with open (file_path, "r") as myfile:
            list_of_lines = myfile.readlines()
            list_of_lines = [x.strip() for x in list_of_lines]
        self.terrain = list_of_lines

    def _get_nature_of_the_spot(self, x_coord, y_coord):
        """ x : horizontal axis towards the right, 0 is in top left
            y : vertical axis towards the bottom, 0 is in top left"""
        if y_coord > len(self.terrain):
            raise OutOfBoundsError
        return self.terrain[y_coord][x_coord % len(self.terrain[0])]

    def toboggan_down_the_terrain(self):
        x = 0
        y = 0
        encountered_terrain = []
        while y < len(self.terrain):
            encountered_terrain.append(self._get_nature_of_the_spot(x, y))
            x = x + 3
            y = y + 1
        encountered_terrain = encountered_terrain[1:] # Removal of the top left that doesn't count
        return encountered_terrain

    def test(self):
        print(self.terrain)
        print(self._get_nature_of_the_spot(3, 1))
        print(self._get_nature_of_the_spot(6, 2))
        print(self._get_nature_of_the_spot(9, 3))
        print(self._get_nature_of_the_spot(12, 4))
        print(self._get_nature_of_the_spot(15, 5))
        # print(self._get_nature_of_the_spot(15, 15))
        print(self.toboggan_down_the_terrain())


if __name__=="__main__":
    day3 = localGeology('test_terrain.txt')
    day3.test()
