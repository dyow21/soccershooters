import unittest

from src.ball import Ball


class TestBall(unittest.TestCase):
    def test_ball_initialization(self):
        ball = Ball(100, 200)
        self.assertEqual(ball.rect.x, 100)
        self.assertEqual(ball.rect.y, 200)
        self.assertEqual(ball.velocity, [0, 0])

    def test_ball_update(self):
        ball = Ball(100, 200)
        ball.velocity = [5, 10]
        ball.update()
        self.assertEqual(ball.rect.x, 105)
        self.assertEqual(ball.rect.y, 210)


if __name__ == "__main__":
    unittest.main()
