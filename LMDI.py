import os
import csv

data_dir = "work_10.2/work1/data/"

def read_csv(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines
# 文件名到字符串数组


def write_csv(file_name, data_list):
    with open(file_name, "w", newline="") as f:
        csv.writer(f).writerows(data_list)


def LMDI(delta, now):
    delta_p, delta_a, delta_e, delta_c = delta
    p, a, e, c = now
    return delta_p * a * e *c + delta_p * (
            (1/2) * (delta_a *e * c + a * delta_e * c + a * e * delta_c) +
            (1/3) * (delta_a * delta_e * c + delta_a * e * delta_c + a * delta_e * delta_c )+
            (1/4) * delta_a * delta_e * delta_c)


def divide(a, b):
    if b == 0:
        return 0
    return a/b


def prase_LMDI(file_name):
    data = read_csv(data_dir + "%s.csv"%file_name)
    last_p, last_a, last_e, last_c = None, None, None, None
    result = [["Year", "P", "A", "E", "C", "p_f", "a_f", "e_f", "c_f"]]
    for i in range(1, len(data)):
        line = data[i].strip().split(",")
        P, A, E, C = map(float, line[1:])
        p, a, e, c = [P, divide(A, P), divide(E, A), divide(C, E)]
        if i > 1:
            delta_p, delta_a, delta_e, delta_c = [p - last_p, a - last_a, e - last_e, c - last_c]
            p_f = LMDI([delta_p, delta_a, delta_e, delta_c], [p, a, e, c])
            a_f = LMDI([delta_a, delta_p, delta_e, delta_c], [a, p, e, c])
            e_f = LMDI([delta_e, delta_a, delta_p, delta_c], [e, a, p, c])
            c_f = LMDI([delta_c, delta_a, delta_e, delta_p], [c, a, e, p])
            raw = line + [p_f, a_f, e_f, c_f]
            result.append(raw)
        last_p, last_a, last_e, last_c = p, a, e, c
    write_csv(data_dir + "%s_result.csv"%file_name, result)


def main():
    for file_name in os.listdir(data_dir):
        if "_result" in file_name or ".csv" not in file_name:
            continue
        file_real_name = file_name.split(".")[0]
        print(file_real_name)
        prase_LMDI(file_real_name)


if __name__ == '__main__':
  main()


