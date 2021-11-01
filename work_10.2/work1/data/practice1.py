import csv

def read_csv(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines
# 文件名到字符串数组


def write_csv(file_name, data_list):
    with open(file_name, "w", newline = "") as f:
        csv.writer(f).writerows(data_list)

# def LMDI(delta, now):
#     delta_p, delta_a, delta_e, delta_c = delta
#     p, a, e, c = now
#     return delta_p * a * e *c + delta_p * (
#             (1/2) * (delta_a *e * c + a * delta_e * c + a * e * delta_c) +
#             (1/3) * (delta_a * delta_e * c + delta_a * e * delta_c + a * delta_e * delta_c )+
#             (1/4) * delta_a * delta_e * delta_c)

        # p_f = get_LMDI(p, a, e, c, delta_p, delta_a, delta_e, delta_c)
        # a_f = get_LMDI(a, p, e, c, delta_a, delta_p, delta_e, delta_c)
        # e_f = get_LMDI(e, a, p, c, delta_e, delta_a, delta_p, delta_c)
        # c_f = get_LMDI(c, a, e, p, delta_c, delta_a, delta_e, delta_p)

def divide(a, b):
    if b == 0:
        return b
    return a/b


def LMDI(p, a, e, c, delta_p, delta_a, delta_e, delta_c):
    return delta_p * a * e *c + delta_p * (
            (1/2) * (delta_a *e * c + a * delta_e * c + a * e * delta_c) +
            (1/3) * (delta_a * delta_e * c + delta_a * e * delta_c + a * delta_e * delta_c )+
            (1/4) * delta_a * delta_e * delta_c)

def get_LMDI(arr):
    res = [["Year", "P", "E", "A", "C", "p_f", "a_f", "e_f", "c_f"]]
    last_p, last_a, last_e, last_c = None, None, None, None
    for i in range(1, len(arr)):
        line = arr[i].strip().split(",")
        P, A, E, C = map(float, line[1:])
        p, a, e, c = P, divide(A, P), divide(E, A), divide(C, E)
        if i > 1:
           delta_p, delta_a, delta_e, delta_c = p-last_p, a-last_a, e-last_e, c-last_c
           p_f = LMDI(p, a, e, c, delta_p, delta_a, delta_e, delta_c)
           a_f = LMDI(a, p, e, c, delta_a, delta_p, delta_e, delta_c)
           e_f = LMDI(e, a, p, c, delta_e, delta_a, delta_p, delta_c)
           c_f = LMDI(c, a, e, p, delta_c, delta_a, delta_e, delta_p)
           res.append(line + [p_f, a_f, e_f, c_f])
        last_p, last_a, last_e, last_c = p, a, e, c
    return res


def main():
  data = read_csv("HK.csv")
  # result = get_LMDI(data)
  res = [["Year", "P", "E", "A", "C", "p_f", "a_f", "e_f", "c_f"]]
  last_p, last_a, last_e, last_c = None, None, None, None
  for i in range(1, len(data)):
      line = data[i].strip().split(",")
      P, A, E, C = map(float, line[1:])
      p, a, e, c = P, divide(A, P), divide(E, A), divide(C, E)
      if i > 1:
          delta_p, delta_a, delta_e, delta_c = p - last_p, a - last_a, e - last_e, c - last_c
          p_f = LMDI(p, a, e, c, delta_p, delta_a, delta_e, delta_c)
          a_f = LMDI(a, p, e, c, delta_a, delta_p, delta_e, delta_c)
          e_f = LMDI(e, a, p, c, delta_e, delta_a, delta_p, delta_c)
          c_f = LMDI(c, a, e, p, delta_c, delta_a, delta_e, delta_p)
          res.append(line + [p_f, a_f, e_f, c_f])
      last_p, last_a, last_e, last_c = p, a, e, c
  write_csv("today_result1.csv", res)
  print("--END--")

if __name__ == '__main__':
  main()


