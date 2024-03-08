def compute_lps(pattern):
    """
    Compute the longest prefix suffix (lps) array for the pattern.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    Search for occurrences of pattern in text using Knuth-Morris-Pratt algorithm.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    occurrences = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences


# Input section to take text and pattern from the user
text = input("Enter the text: ")
pattern = input("Enter the pattern to search for: ")

# Find occurrences of pattern in text
occurrences = kmp_search(text, pattern)

if occurrences:
    print("Pattern found at positions:", occurrences)
else:
    print("Pattern not found in the text.")
