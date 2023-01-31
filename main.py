
import random

class game:
    def __init__(self):
        self.map = []
        self.current_location = []
        self.map_list = []
        self.shown_map = []
        self.temp_location = []
        self.skip = bool
        self.location_list = 0
        self.score = 0
        self.sword = 0
        self.potion = 0
        self.vital = True
        self.message = " "
        pass
    def location(self, s:int):
        return [s//7, s%7]
    def maps(self):
        self.map_list = ['T', 'T', 'T', 'T', 'T', 'M', 'M', 'M', 'M', 'M', 'S', 'S', 'P', 'P', 'P', 'V', 'V', 'V', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        random.shuffle(self.map_list)
        self.current_location = self.location(self.map_list.index("E"))
        self.location_list = self.map_list.index("E")
        self.shown_map = [" " for i in range(42)]
        self.shown_map[self.map_list.index("E")] = "E"
    def temp_location_finder(self, s: str):
        s = s.lower()

        if s == "u":
            self.temp_location = [self.current_location[0]-1, self.current_location[1]]
        if s == "d":
            self.temp_location = [self.current_location[0]+1, self.current_location[1]]
        if s == "l":
            self.temp_location = [self.current_location[0], self.current_location[1]-1]
        if s == "r":
            self.temp_location = [self.current_location[0], self.current_location[1]+1]
    def move(self):
        if 6 > self.temp_location[0] > -1 and 7 > self.temp_location[1] > -1 and self.shown_map[self.temp_location[0]*7 + self.temp_location[1]] == " ":
            self.current_location = self.temp_location
            self.location_list = self.temp_location[0]*7 + self.temp_location[1]
            self.skip = False
            if self.map_list[self.location_list] == " ":
                self.shown_map[self.location_list] = "E"
            else:
                self.shown_map[self.location_list] = self.map_list[self.location_list]
        else:
            self.temp_location = self.current_location
            self.skip = True
            self.message = " "

    def location_checker(self):
        if self.map_list[self.location_list] == " ":
            self.message = " "
            pass
        if self.map_list[self.location_list] == "T":
            self.score += 1
            self.message = "\n--------------------------------\n\n+TREASURE\n\n--------------------------------"
        if self.map_list[self.location_list] == "M":
            if self.sword == 0:
                self.message = "\n--------------------------------\n\nOh No! MONSTER.\nYou die"
                self.score -= 1
                self.vital = False
            else:
                self.message = "\n--------------------------------\n\nOh No! MONSTER.\nSWORD is used!\n\n--------------------------------"
                self.sword -= 1
        if self.map_list[self.location_list] == "S":
            self.sword +=1
            self.message = "\n--------------------------------\n\n+SWORD\n\n--------------------------------"
        if self.map_list[self.location_list] == "P":
            self.potion +=1
            self.message = "\n--------------------------------\n\n+POTION\n\n--------------------------------"
        if self.map_list[self.location_list] == "V":
            if self.potion == 0:
                self.message = "\n--------------------------------\n\nOh No! VENOM.\nYou die"
                self.vital = False
                self.score -= 1
            else:
                self.message = "\n--------------------------------\n\nOh No! VENOM.\nPOTION is used!\n\n--------------------------------"
                self.potion -= 1

    def all_printer(self):
        self.maps()
        while self.vital:
            print('\033[H\033[J', end='')
            for i in range(0,42,7):
                print(self.shown_map[i:i+7])
            print(self.message)
            print("\nScore: [{}] Sword: [{}] Potion: [{}]".format(self.score, self.sword, self.potion))
            s = input("Press L, U, R, D to move: ")
            print("\n\n")
            self.temp_location_finder(s)
            self.move()
            if not self.skip:
                self.location_checker()
                self.score += 1
        for i in range(0, 42, 7):
            print(self.shown_map[i:i + 7])
        print(self.message)
        print("\nScore: [{}] Sword: [{}] Potion: [{}]".format(self.score, self.sword, self.potion))
        print("\nGame over.")

testing = game()
testing.all_printer()




