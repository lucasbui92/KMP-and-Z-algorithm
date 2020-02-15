# Knuth-Morris-Pratt (KMP) and Z- algorithm
* **Q1**: Modifies SPi to SPi(x) in KMP algorithm. Then, SPi(x) is defined as the length of the longest proper suffix of pat[1 . . . i] that matches the prefix of pat, with the extra condition that pat[SPi(x) + 1] = x. That is, pat[i−SPi(x)+1 . . . i] = pat[1 . . . SPi(x)], and pat[SPi(x)+1] ≡ x while pat[i+1] ≡ y.
* **Q2**: Identify all positions within txt[1..n] that matches the pat[1..m] within a Hamming distance ≤1
* **Q3**: Identify all positions within txt[1..n] that matches the pat[1..m] within an Edit distance ≤ 1
