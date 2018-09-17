import unittest
from robot import Robot

class TestRobot(unittest.TestCase):

    def test_place(self):
        robot = Robot()

        robot.place("PLACE 0,0,NORTH")
        self.assertEqual(robot.report(),"0,0,NORTH")

        robot.place("PLACE 0,0,WEST")
        self.assertEqual(robot.report(),"0,0,WEST")

        robot.place("PLACE 0,0,SOUTH")
        self.assertEqual(robot.report(),"0,0,SOUTH")

        robot.place("PLACE 0,0,EAST")
        self.assertEqual(robot.report(),"0,0,EAST")

        robot.place("PLACE 4,4,NORTH")
        self.assertEqual(robot.report(),"4,4,NORTH")

        robot.place("PLACE 0,-1,NORTH")
        self.assertNotEqual(robot.report(),"0,-1,NORTH")

        robot.place("PLACE -1,0,NORTH")
        self.assertNotEqual(robot.report(),"-1,0,NORTH")

        robot.place("PLACE 0,5,NORTH")
        self.assertNotEqual(robot.report(),"0,5,NORTH")

        robot.place("PLACE 5,0,NORTH")
        self.assertNotEqual(robot.report(),"5,0,NORTH")



    def test_move(self):
        robot = Robot()

        robot.move()
        self.assertEqual(robot.report(),"Error, robot has not been placed properly")

        robot.place("PLACE 0,0,NORTH")

        robot.move()
        self.assertEqual(robot.report(),"0,1,NORTH")

        robot.move()
        self.assertEqual(robot.report(),"0,2,NORTH")

        robot.move()
        self.assertEqual(robot.report(),"0,3,NORTH")

        robot.move()
        self.assertEqual(robot.report(),"0,4,NORTH")

        robot.move()
        self.assertEqual(robot.report(),"0,4,NORTH")

        robot.place("PLACE 0,0,EAST")

        robot.move()
        self.assertEqual(robot.report(),"1,0,EAST")

        robot.move()
        self.assertEqual(robot.report(),"2,0,EAST")

        robot.move()
        self.assertEqual(robot.report(),"3,0,EAST")

        robot.move()
        self.assertEqual(robot.report(),"4,0,EAST")

        robot.move()
        self.assertEqual(robot.report(),"4,0,EAST")

        robot.place("PLACE 0,0,WEST")

        robot.move()
        self.assertEqual(robot.report(),"0,0,WEST")

        robot.move()
        self.assertEqual(robot.report(),"0,0,WEST")

        robot.place("PLACE 0,0,SOUTH")

        robot.move()
        self.assertEqual(robot.report(),"0,0,SOUTH")

        robot.move()
        self.assertEqual(robot.report(),"0,0,SOUTH")


    def test_report(self):
        robot = Robot()

        #misspelling and other garbage after PLACE
        robot.place("PLACE 3,4,NORHT")
        self.assertEqual(robot.report(),"Error, robot has not been placed properly")

        robot.place("PLACE 3,4,NORTH")
        self.assertEqual(robot.report(),"3,4,NORTH")

        robot.place("PLACE 5,7,NORTH")
        self.assertEqual(robot.report(),"3,4,NORTH")

        robot.place("PLACE 2,3,SOUTH")
        self.assertEqual(robot.report(),"2,3,SOUTH")

        robot.place("PLACE 3,4,EAST")
        self.assertEqual(robot.report(),"3,4,EAST")

        robot.place("PLACE 0,1,WEST")
        self.assertEqual(robot.report(),"0,1,WEST")


    def test_rotate(self):
        robot = Robot()

        robot.place("PLACE 0,0,NORTH")

        robot.rotate("LEFT")
        self.assertEqual(robot.report(), "0,0,WEST")

        robot.rotate("LEFT")
        self.assertEqual(robot.report(), "0,0,SOUTH")

        robot.rotate("LEFT")
        self.assertEqual(robot.report(), "0,0,EAST")

        robot.rotate("LEFT")
        self.assertEqual(robot.report(), "0,0,NORTH")

        robot.rotate("RIGHT")
        self.assertEqual(robot.report(), "0,0,EAST")

        robot.rotate("RIGHT")
        self.assertEqual(robot.report(), "0,0,SOUTH")

        robot.rotate("RIGHT")
        self.assertEqual(robot.report(), "0,0,WEST")

        robot.rotate("RIGHT")
        self.assertEqual(robot.report(), "0,0,NORTH")


    def test_constrain(self):
        robot = Robot()
        self.assertEqual(robot.constrain(0,0),1)
        self.assertEqual(robot.constrain(4,4),1)
        self.assertEqual(robot.constrain(0,4),1)
        self.assertEqual(robot.constrain(4,0),1)
        self.assertEqual(robot.constrain(5,0),0)
        self.assertEqual(robot.constrain(-1,0),0)
        self.assertEqual(robot.constrain(0,5),0)
        self.assertEqual(robot.constrain(0,-1),0)

if __name__ == '__main__':
    unittest.main()
