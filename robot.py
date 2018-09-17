class Robot():


    def __init__(self):
        self.is_moving= False


    def parser(self,command_name):
        command_name = command_name.upper()
        if "PLACE" in command_name:
            if self.place(command_name):
                self.is_moving = True
        if self.is_moving:
            if command_name == "MOVE":
                self.move()
            if command_name == "REPORT":
                self.report()
            if command_name == "LEFT":
                self.rotate("LEFT")
            if command_name == "RIGHT":
                self.rotate("RIGHT")


    def place(self,command_name):
        try:
            command_name = command_name.split(' ')[1]
            a = command_name.split(',')
            if a[2].upper() in ["NORTH","EAST","SOUTH","WEST"] and self.constrain(int(a[0]),int(a[1])):
                self.x = int(a[0])
                self.y = int(a[1])
                self.rotation = a[2]
                return True
        except (ValueError,IndexError):
            return False

    def move(self):
        try:
            if self.rotation == "NORTH":
                self.y += self.constrain(self.x,self.y+1)
            elif self.rotation == "SOUTH":
                self.y -= self.constrain(self.x,self.y-1)
            elif self.rotation == "EAST":
                self.x += self.constrain(self.x+1,self.y)
            elif self.rotation == "WEST":
                self.x -= self.constrain(self.x-1,self.y)
        except AttributeError:
            pass


    def rotate(self,side):
        rotations = ["NORTH","EAST","SOUTH","WEST"]
        current_index_of_rotation = rotations.index(self.rotation)
        if side == "LEFT":
            if current_index_of_rotation - 1 < 0:
                self.rotation = rotations[-1]
            else:
                self.rotation = rotations[current_index_of_rotation-1]
        elif side == "RIGHT":
            if current_index_of_rotation + 1 > 3:
                self.rotation = rotations[0]
            else:
                self.rotation = rotations[current_index_of_rotation+1]


    def report(self):
        try:
            return f"{self.x},{self.y},{self.rotation}"
        except AttributeError:
            return "Error, robot has not been placed properly"


    def constrain(self,x,y):
        if x>4 or x<0 or y>4 or y<0:
            return 0
        else:
            return 1
