from src.ml_robust_eval.metrics import ClassifMetricsCalc, RegressionMetricsCalc, NLPMetricsCalc, CVMetricsCalc
from src.ml_robust_eval.crossvalidator import CrossValidatorCalc, ABTesterTool
from src.ml_robust_eval.vizual import Vizualizer
from src.ml_robust_eval.testcasegenerator import TestCaseGeneratorT

print("=== Classification Metrics ===")
cm = ClassifMetricsCalc()
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]
print("Accuracy:", cm.accuracy(y_true, y_pred))
print("Precision:", cm.precision(y_true, y_pred))
print("Recall:", cm.recall(y_true, y_pred))
print("F1 Score:", cm.f1_score(y_true, y_pred))
conf_matrix = cm.confusion_matrix(y_true, y_pred)
print("Confusion Matrix:", conf_matrix)

print("\n=== Regression Metrics ===")
rm = RegressionMetricsCalc()
y_true_reg = [2.0, 3.0, 4.0]
y_pred_reg = [2.5, 2.8, 4.2]
print("MAE:", rm.mae(y_true_reg, y_pred_reg))
print("MSE:", rm.mse(y_true_reg, y_pred_reg))
print("R2 Score:", rm.r2_score(y_true_reg, y_pred_reg))

print("\n=== NLP Metrics ===")
nlp = NLPMetricsCalc()
ref = "the quick brown fox"
cand = "the quick fox"
print("BLEU Score:", nlp.bleu(ref, cand))

print("\n=== CV Metrics ===")
cv_m = CVMetricsCalc()
boxA = [0, 0, 2, 2]
boxB = [1, 1, 3, 3]
print("IoU:", cv_m.iou(boxA, boxB))

print("\n=== Cross-Validation ===")
cv = CrossValidatorCalc()
X = [[1], [2], [3], [4], [5]]
y = [0, 1, 0, 1, 0]
folds = cv.k_fold_splitter(X, y, k=2, seed=42)
print("K-Fold Splits:", folds)

print("\n=== A/B Testing ===")
tester = ABTesterTool()
result = tester.ab_testing(cm.accuracy, [1,0,1], [1,0,0], [1,0,1], [1,1,1])
print("A/B Test Result:", result)

print("\n=== Visualization ===")
viz = Vizualizer()
print("Confusion Matrix (Printed):")
viz.printing_confusion_matrix(conf_matrix, ["Class 0", "Class 1"])
print("ROC Curve (Printed):")
y_scores = [0.9, 0.1, 0.8, 0.4, 0.7]
viz.printing_roc_curve(y_true, y_scores, steps=5)

print("\n=== Test Case Generation ===")
tcg = TestCaseGeneratorT()
X = [[0.5, 0.7], [0.2, 0.8]]
feature_ranges = [(0.0, 1.0), (0.0, 1.0)]
edge_cases = tcg.gen_edge_cases(X, feature_ranges)
boundary_cases = tcg.gen_boundary_cases(X, feature_ranges, delta=0.01)
adv_cases = tcg.gen_adversarial_cases(X, epsilon=0.1)
print("Edge Cases:", edge_cases)
print("Boundary Cases:", boundary_cases)
print("Adversarial Cases:", adv_cases)
