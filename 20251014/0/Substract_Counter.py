from collections import Counter

gazeta = Counter(input().split())
zapiska = Counter(input().split())

print(not(zapiska - gazeta))

