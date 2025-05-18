import unittest
from src.ml_robust_eval.crossvalidator import CrossValidatorCalc, ABTesterTool

class TestCrossValidatoN(unittest.TestCase):
    def setUp(self):
        self.cv = CrossValidatorCalc()
        self.X = [[1], [2], [3], [4], [5]]
        self.y = [0, 1, 0, 1, 0]

    def testing_k_fold_split(self):
        folds = self.cv.k_fold_splitter(self.X, self.y, k=2, seed=42)
        self.assertEqual(len(folds), 2)
        all_indices = [idx for fold in folds for idx in fold[0] + fold[1]]
        self.assertEqual(sorted(set(all_indices)), list(range(5)))

class TestABTesting(unittest.TestCase):
    def setUp(self):
        self.tester = ABTesterTool()
        self.metric = lambda y_true, y_pred: sum(yt == yp for yt, yp in zip(y_true, y_pred)) / len(y_true)

    def testing_ab_test(self):
        result = self.tester.ab_testing(self.metric, [1, 0, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1])
        self.assertIn('A', result)
        self.assertIn('B', result)
        self.assertIn('diff', result)
        self.assertAlmostEqual(result['A'], 2/3)
        self.assertAlmostEqual(result['B'], 2/3)

if __name__ == "__main__":
    unittest.main()
