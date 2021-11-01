import math
from collections import Counter

def read_txt(file_name):
    with open("%s.txt"%file_name, "r") as f:



data1 = f.read().split(" ")

def deal_data1(arr1):
  dic1 = {}
  for x in arr1:
      dic1[x] = dic1.get(x, 0) + 1
  return dic1

result1 = deal_data1(data1)
print("1", result1)

with open("work_10.2/Homework/Data/1.txt", "r") as f:
    data2 = f.read().split(" ")

def deal_data2(arr2):
  dic2 = {}
  for x in arr2:
      dic2[x] = dic2.get(x, 0) + 1
  return dic2

result2 = deal_data2(data2)
print("2", result2)

res1, res2 = Counter(result1) , Counter(result2)
z = dict(res1+ res2)
print(z)

a = sorted(z.items(), key=lambda x: x[1], reverse=True)
print(a)

c = dict(a)
print(c)
#
print([i for i in c.values()][0])

print(sum(c.values()))

tf_ij = ([i for i in c.values()][0] / sum(c.values()))
print(tf_ij)


def count_file(d):
    if "and" in d:
        return 1
    return 0

r1 = count_file(result1)
r2 = count_file(result2)



idfi = math.log (2/ (r1 + r2))
print(idfi)

tfidfij = tf_ij * idfi
print("final", tfidfij)


