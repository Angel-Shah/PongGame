import unittest
import os
import pongFunctions as pf
from random import randint

# unit testing for the functions used in the pong game using Python's inbuilt unit tester
# only had 4 functions in whole game for moving the paddles up and down so only those could be used
# if all tests pass, 'OK' should be outputted or else 'FAILURE' is there are errors


class TestPong(unittest.TestCase):
    # a random int is passed as the parameter each time
    def test_movingPaddle1Up(self):
        x = randint(-230, 220)
        result = pf.paddle1_up(x)
        self.assertEqual(result, x + 25)

    def test_movingPaddle1Down(self):
        y = randint(-230, 220)
        result = pf.paddle1_down(y)
        self.assertEqual(result, y - 25)

    def test_movingPaddle2Up(self):
        randNum = randint(-230, 220)
        result = pf.paddle2_up(randNum)
        self.assertEqual(result, randNum + 25)

    def test_movingPaddle2Down(self):
        randNum = randint(-230, 220)
        result = pf.paddle2_down(randNum)
        self.assertEqual(result, randNum - 25)


if __name__ == "__main__":
    unittest.main()

os.system("")
