import logging
import unittest
logger = logging.getLogger(__name__)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_test = Runner('First', -10)
            for i in range(10):
                runner_test.walk()
            self.assertEqual(runner_test.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_test = Runner(2)
            for i in range(10):
                runner_test.run()
            self.assertEqual(runner_test.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_slow = Runner('Turtle')
        runner_fast = Runner('Bunny')
        for i in range(10):
            runner_slow.walk()
            runner_fast.run()
        self.assertNotEqual(runner_fast.distance, runner_slow.distance)

FORMAT = '%(asctime)s | %(levelname)s | %(message)s'
logging.basicConfig(filename='runner_tests.log', encoding='utf-8', level=logging.INFO, format=FORMAT)

