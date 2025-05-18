import unittest
from src.ml_robust_eval.vizual import Vizualizer

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        self.viz = Vizualizer()
        self.cm = [[2, 1], [1, 2]]
        self.class_names = ['A', 'B']

    def test_print_confusion_matrix(self):
        try:
            self.viz.printing_confusion_matrix(self.cm, self.class_names)
        except Exception as e:
            self.fail(f"print_confusion_matrix raised an exception: {e}")

    def test_print_roc_curve(self):
        y_true = [1, 0, 1, 0, 1]
        y_scores = [0.9, 0.1, 0.8, 0.4, 0.7]
        try:
            self.viz.printing_roc_curve(y_true, y_scores, steps=5)
        except Exception as e:
            self.fail(f"print_roc_curve raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
