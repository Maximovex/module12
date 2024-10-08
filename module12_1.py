import unittest as ut


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(ut.TestCase):

    def test_walk(self):
        runner_test = Runner('First')
        for i in range(10):
            runner_test.walk()
        ut.TestCase.assertEqual(self, runner_test.distance, 50)

    def test_run(self):
        runner_test = Runner('Second')
        for i in range(10):
            runner_test.run()
        ut.TestCase.assertEqual(self, runner_test.distance, 100)

    def test_challenge(self):
        runner_slow = Runner('Turtle')
        runner_fast = Runner('Bunny')
        for i in range(10):
            runner_slow.walk()
            runner_fast.run()
        ut.TestCase.assertNotEqual(self, runner_fast.distance, runner_slow.distance)


if __name__ == '__main__':
    ut.main()
