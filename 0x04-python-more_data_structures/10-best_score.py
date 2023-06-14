#!/usr/bin/python3
def best_score(a_dictionary)
    max_score = None
    max_k = None
    for k, v in a_dictionary.items():
        if max_score is None or v > max_score:
            max_score = v
            max_k = k
    return max_k
