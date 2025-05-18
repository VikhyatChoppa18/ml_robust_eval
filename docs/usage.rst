Usage
=====

Quick Example
-------------

.. code-block:: python

   from ml_eval_robust.metrics import ClassificationMetrics
   cm = ClassificationMetrics()
   y_true = [1, 0, 1, 1, 0]
   y_pred = [1, 0, 0, 1, 1]
   print("Accuracy:", cm.accuracy_calc(y_true, y_pred))
   print("Confusion Matrix:", cm.confusion_matrix_(y_true, y_pred))

See the :doc:`api_reference` for all available classes and methods.
