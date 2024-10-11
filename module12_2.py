import operator
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        runner1 = Runner('Усэйн', 10)
        runner2 = Runner('Андрей', 9)
        runner3 = Runner('Ник', 3)
        self.runners = [runner1, runner2, runner3]

    def test_win(self):
        runners1 = self.runners
        runners1.pop(1)
        tourn1 = Tournament(90, *runners1)
        self.all_results.update(tourn1.start())
        self.assertTrue(list(self.all_results.values())[-1] == 'Ник')

    def test_win2(self):
        runners2 = self.runners
        runners2.pop(0)
        tourn1 = Tournament(90, *runners2)
        self.all_results.clear()
        self.all_results.update(tourn1.start())
        self.assertTrue(list(self.all_results.values())[-1] == 'Ник')

    def test_win3(self):
        runners3 = self.runners
        tourn1 = Tournament(90, *runners3)
        self.all_results.clear()
        self.all_results.update(tourn1.start())
        self.assertTrue(list(self.all_results.values())[-1] == 'Ник')

    def tearDown(self):
        print(self.all_results)

   


if __name__ == '__main__':
    TournamentTest.main()
