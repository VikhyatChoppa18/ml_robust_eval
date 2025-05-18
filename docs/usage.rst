Usage
=====

Quick Example
-------------

.. code-block:: python

   from ml_eval_robust.metrics import ClassificationMetrics
   cm = ClassifMetricsCalc()
   y_true = [1, 0, 1, 1, 0]
   y_pred = [1, 0, 1, 0, 0]
   print("Accuracy:", cm.accuracy_calc(y_true, y_pred))
   print("Precision:", cm.precision_calc(y_true, y_pred))
   print("Recall:", cm.recall_calc(y_true, y_pred))
   print("F1 Score:", cm.f1_score_calc(y_true, y_pred))
   conf_matrix = cm.confusion_matrix_(y_true, y_pred)
   print("Confusion Matrix:", conf_matrix)

   === Classification Metrics ===
   Accuracy: 0.8
   Precision: 0.999999995
   Recall: 0.6666666644444444
   F1 Score: 0.799999992
   Confusion Matrix: [[2, 0], [1, 2]]


See the :doc:`api_reference` for all available classes and methods.
