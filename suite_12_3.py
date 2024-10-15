import unittest
import tests_12_3
import runner_12_3

stTests = unittest.TestSuite()
stTests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
stTests.addTest(unittest.TestLoader().loadTestsFromTestCase(module12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(stTests)
