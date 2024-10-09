# CREDIT: Raghavender
# OPTIMIZATION ISSUE

pcfg = {
    "S": [("NP", "VP", 1.0)],
    "PP": [("P", "NP", 1.0)],
    "VP": [("V", "NP", 0.7), ("VP", "PP", 0.3)],
    "P": [("with", 1.0)],
    "V": [("saw", 1.0)],
    "NP": [("NP", "PP", 0.4), ("astronomer", 0.1), ("ears", 0.18), 
           ("saw", 0.04), ("stars", 0.18), ("telescopes", 0.1)]
}

sentences = ['astronomer', 'saw', 'stars', 'with', 'ears']
n = len(sentences)
T = [[{} for _ in range(n)] for _ in range(n)]

# Fill diagonal elements
for i, word in enumerate(sentences):
    for lhs, rules in pcfg.items():
        for rule in rules:
            if len(rule) == 2 and rule[0] == word:
                T[i][i][lhs] = rule[1]

# Fill the rest of the matrix
for span in range(2, n+1):
    for i in range(n-span+1):
        j = i + span - 1
        for k in range(i, j):
            for lhs, rules in pcfg.items():
                for rule in rules:
                    if len(rule) == 3:
                        A, B, prob = rule
                        if A in T[i][k] and B in T[k+1][j]:
                            combined_prob = prob * T[i][k].get(A, 0) * T[k+1][j].get(B, 0)
                            T[i][j][lhs] = T[i][j].get(lhs, 0) + combined_prob

# Print the resulting table
for row in T:
    print(row)
