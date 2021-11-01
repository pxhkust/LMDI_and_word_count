from statistics import mean
import csv

def read_csv(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines
# 文件名到字符串数组

def write_csv(file_name, data_list):
    with open(file_name, "w", newline="") as f:
        csv.writer(f).writerows(data_list)
# 二维字符串数组到文件

def average_score(arr):
  # total_score = [float(arr[i].split(",")[-1]) for i in range(1, len(arr))]
  return mean([float(arr[i].strip().split(",")[-1]) for i in range(1, len(arr))])
  # total_score = []
  # for i in range(1, len(arr)):
  #   score = arr[i].split(",")
  #   total_score.append(float(score[0])+ float(score[1])
  # return total_score


# 先创造类别 dic
# 对类别算平均分

def deal_data(arr):
  dic = {}
  for i in range(1, len(arr)):
    _, label, score = arr[i].strip().split(",")
    if label not in dic:
      dic[label] = []
    dic[label].append(float(score))

  # return {k: sum(v) / len(v) for k, v in dic.items()}
# 列表推导式
  score_dict = [["Class", "Avg"]]
  for k, v in dic.items():
    score_dict.append([k, str(sum(v) / len(v))])
  return score_dict

def main():
  data = read_csv("score.csv")
  result = deal_data(data)
  write_csv("result.csv", result)
  print("--END--")

if __name__ == '__main__':
  main()





