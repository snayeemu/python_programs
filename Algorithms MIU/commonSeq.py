m = 5
n = 6
L = [[]]
def longestCommonSubSequence
    for i in range (m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif