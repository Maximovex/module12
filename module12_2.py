
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results={}

    def setUp(self):
        runner1 = Runner('Усэйн', 10)
        runner2 = Runner('Андрей', 9)
        runner3 = Runner('Ник', 3)
        self.runners=[runner1,runner2,runner3]

    def test_win(self):
        tourn1=Tournament(90,*self.runners)

        self.all_results=tourn1.start()
        print(self.all_results)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)


if __name__=='__main__':
    TournamentTest.main()
