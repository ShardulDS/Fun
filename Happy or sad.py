from collections import Counter
def happyLadybugs(b):
    # Write your code here
    b=list(b)
    if b.count('_') == 0:
        if len(b) < 2:
            return 'NO'
        if b[0] != b[1]:
            return 'NO'
        if b[-1] != b[-2]:
            return 'NO'
        for i in range(1, len(b) - 1):
            if b[i - 1] != b[i] and b[i+1] != b[i]:
                return 'NO'
        return 'YES'
    freq = Counter(b)
    if len(b) == freq['_']:
        return 'YES'
    del freq['_']
    if 1 in freq.values():
        return 'NO'
    return 'YES'

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        b = input().strip()
        print(happyLadybugs(b))