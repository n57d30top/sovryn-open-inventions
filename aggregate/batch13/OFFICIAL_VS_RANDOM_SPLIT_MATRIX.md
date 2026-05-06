# Official Versus Random Split Matrix

This matrix uses source train/test files as the protocol split and a same-size stratified random split as the challenger.

| Target | Source split logistic macro-F1 | Random challenger logistic macro-F1 | Random minus source | Finding |
| --- | ---: | ---: | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | 0.9544 | 0.9832 | 0.0288 | material_protocol_difference |
| UCI Optical Recognition of Handwritten Digits | 0.9500 | 0.9722 | 0.0222 | material_protocol_difference |
| UCI Pen-Based Recognition of Handwritten Digits | 0.9164 | 0.9458 | 0.0293 | material_protocol_difference |
