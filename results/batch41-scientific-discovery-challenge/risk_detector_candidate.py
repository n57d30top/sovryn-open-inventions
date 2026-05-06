def risk_score(features):
    score = 0
    score += 1 if features.get("source_protocol") else 0
    score += 2 if features.get("ambiguous") else 0
    score += 2 if features.get("source_group_overlap") == 0 and features.get("random_group_overlap", 0) > 0 else 0
    score += 1 if features.get("model_variance", 0) > 0.04 else 0
    score += 1 if features.get("class_imbalance_ratio", 1) > 10 else 0
    return score
