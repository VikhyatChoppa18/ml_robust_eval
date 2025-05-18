# from src.ml_robust_eval.metrics import ClassifMetricsCalc
# from src.ml_robust_eval.crossvalidator import CrossValidatorCalc
# from src.ml_robust_eval.vizual import Vizualizer
# from src.ml_eval_robust.testcasegen import TestCaseGenerator, Classification Metrics
#
# cm = ClassificationMetrics()
# y_true = [1, 0, 1, 1,pred = [1,
#
#
# print("Accuracy:", cm.accuracy(y_true, y_pred))
# print("Confusion Matrix:", cm.confusion_matrix(y_true, y_pred))
# Cross-Validation
#
# cv = CrossValidator()
# folds = cv.k_fold_split([
# ,,,,], [0,
#
# , k=2)
# print("Folds:", folds)
# Visualization
#
# viz = Visualizer()
# viz.print_confusion_matrix([
# ,
#
# ], ["Class 0", "Class 1"])
# Test Case Generation
#
# tcg = TestCaseGenerator()
# X = [[0.5, 0.7], [0.2, 0.8]]
# feature_ranges = [(0.0, 1.0), (0.0, 1.0)]
# print("Edge Cases:", tcg.generate_edge_cases(X, feature_ranges))