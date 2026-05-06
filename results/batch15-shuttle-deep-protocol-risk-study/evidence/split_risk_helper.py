#!/usr/bin/env python3
"""Tiny Batch 15 split-risk helper."""

def classify(delta_macro_f1, rare_class_warning=False, protocol_ambiguous=False):
    points = 0
    if abs(delta_macro_f1) >= 0.05:
        points += 3
    elif abs(delta_macro_f1) >= 0.02:
        points += 2
    elif abs(delta_macro_f1) >= 0.005:
        points += 1
    if rare_class_warning:
        points += 2
    if protocol_ambiguous:
        points += 1
    if points >= 6:
        return "high"
    if points >= 4:
        return "moderate"
    if points >= 1:
        return "low"
    return "none"

def _tests():
    return {
        "positive": classify(0.0702, rare_class_warning=True) == "high",
        "negative": classify(0.002, rare_class_warning=False) == "none",
    }

if __name__ == "__main__":
    import json
    print(json.dumps(_tests(), sort_keys=True))
