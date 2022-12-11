from collections import Counter

S = input()
cnt = Counter(S)
print(cnt["v"] + 2 * cnt["w"])
