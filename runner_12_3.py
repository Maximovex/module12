import unittest


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


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_test = Runner('First')
        for i in range(10):
            runner_test.walk()
        self.assertEqual(runner_test.distance, 50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_test = Runner('Second')
        for i in range(10):
            runner_test.run()
        self.assertEqual(runner_test.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_slow = Runner('Turtle')
        runner_fast = Runner('Bunny')
        for i in range(10):
            runner_slow.walk()
            runner_fast.run()
        self.assertNotEqual(runner_fast.distance, runner_slow.distance)


if __name__ == '__main__':
    RunnerTest.main()
