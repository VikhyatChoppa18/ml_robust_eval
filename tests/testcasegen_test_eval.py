import unittest
from src.ml_robust_eval.testcasegenerator import TestCaseGeneratorT

class TestTestCaseGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = TestCaseGeneratorT()
        self.X = [[0.5, 0.7], [0.2, 0.8]]
        self.feature_ranges = [(0.0, 1.0), (0.0, 1.0)]

    def testing_generate_edge_cases(self):
        edge_cases = self.gen.gen_edge_cases(self.X, self.feature_ranges)
        self.assertTrue(any(sample[0] == 0.0 for sample in edge_cases))
        self.assertTrue(any(sample[1] == 1.0 for sample in edge_cases))

    def testing_generate_boundary_cases(self):
        boundary_cases = self.gen.gen_boundary_cases(self.X, self.feature_ranges, delta=0.01)
        self.assertTrue(any(abs(sample[0] - 0.01) < 1e-6 for sample in boundary_cases))
        self.assertTrue(any(abs(sample[1] - 0.99) < 1e-6 for sample in boundary_cases))

    def testing_generate_adversarial_cases(self):
        adv_cases = self.gen.gen_adversarial_cases(self.X, epsilon=0.1)
        for orig, adv in zip(self.X, adv_cases):
            diffs = [abs(a - o) for a, o in zip(adv, orig)]
            self.assertTrue(all(abs(d - 0.1) < 1e-6 for d in diffs))

if __name__ == "__main__":
    unittest.main()
