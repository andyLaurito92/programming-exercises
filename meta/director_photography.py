def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # 3 conditions
  # 1. P < A < B
  # 2. |P - A| IN [X, Y]
  # 3. |A - B| IN [X, Y]
  bucket = [[] for _ in range(4)]
  mapping = {'A': 0, 'P':1, 'B':2, '.': 3}
  for idx, c in enumerate(C):
    bucket[mapping[c]].append(idx + 1)
  
  artistic_photograph = 0
  for p in bucket[1]:
    for a in bucket[0]:
      for b in bucket[2]:
        if (p < a < b or b < a < p) and abs(p - a) in range(X, Y+1) and abs(a-b) in range(X, Y+1):
          artistic_photograph += 1
  
  return artistic_photograph


assert 1 == getArtisticPhotographCount(5, 'APABA', 1, 2)

assert 0 == getArtisticPhotographCount(5, 'APABA', 2, 3)

assert 3 == getArtisticPhotographCount(8, '.PBAAP.B', 1, 3)




"""
How many artistic photographs can I get until C[:i]?
S: C[:i]
R: Max artistic photographs until C[:i] =
num = C[:i-1]
if C[i] == 'P':
	

if C[i] == 'A':
if C[i] == 'C':
if C[i] == '.':



T: for i in range(len(c))
B
O
T

bucket = [[4,5], [2, 6], [3, 8]]

valid_pairs = [(2, 8), (6, 8), (3, 6))]

"""


"""
P1 A1 B1 x
P1 A1 B2 Y
P1 A2 B1
"""

# runtime, if P = #p, A = #A & B = #b then O(N + P*A + A*(P+B)) and we know that
# P + A + B <= N
def getArtisticPhotographCount2(N: int, C: str, X: int, Y: int) -> int:
  # 3 conditions
  # 1. P < A < B
  # 2. |P - A| IN [X, Y]
  # 3. |A - B| IN [X, Y]
  bucket = [[] for _ in range(4)]
  mapping = {'A': 0, 'P':1, 'B':2, '.': 3}
  for idx, c in enumerate(C):
    bucket[mapping[c]].append(idx + 1)

  valid_pairs = []
  for p in bucket[1]:
      for b in bucket[2]:
          if p < b and b - p > 1:
              valid_pairs.append((p, b))
          elif b < p and p - b > 1:
              valid_pairs.append((b, p))


  artistic_photograph = 0
  for a in bucket[0]:
      for p, b in valid_pairs:
        if (p < a < b or b < a < p) and abs(p - a) in range(X, Y+1) and abs(a-b) in range(X, Y+1):
          artistic_photograph += 1
  
  return artistic_photograph

assert 1 == getArtisticPhotographCount2(5, 'APABA', 1, 2)

assert 0 == getArtisticPhotographCount2(5, 'APABA', 2, 3)

assert 3 == getArtisticPhotographCount2(8, '.PBAAP.B', 1, 3)

