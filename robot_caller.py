from robot import Robot

robot = Robot()
print("Input exit to exit")

while True:
    command = input(">")
    if command.upper() == "REPORT":
        print(robot.report())
    elif command.upper() == "EXIT":
        break
    robot.parser(command)
