import unittest
from src.ml_robust_eval.metrics import ClassifMetricsCalc

class TestClassificationMetricsEval(unittest.TestCase):
    def setUp(self):
        self.metrics = ClassifMetricsCalc()
        self.y_true = [1, 0, 1, 1, 0]
        self.y_pred = [1, 0, 0, 1, 1]

    def testing_accuracy(self):
        self.assertAlmostEqual(self.metrics.accuracy_calc(self.y_true, self.y_pred), 0.6)

    def testing_confusion_matrix(self):
        cm = self.metrics.confusion_matrix_(self.y_true, self.y_pred)
        self.assertEqual(cm, [[1, 1], [1, 2]])

if __name__ == '__main__':
    unittest.main()
