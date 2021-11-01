import os
import re
import math

data_dir = "./Data/"
stop = set(["a", "the", "this", "that", "an", "and",
            "are", "is", "", "on", "in", "for", "it",
            "to", "as", "also", "yet", "both", "from",
            "of", "been", "being", "while", "their",
            "be", "by", "only", "your", "you", "with"])  # 禁用词表


def read_txt(file_path):
    with open(file_path, "r") as fr:
        text_str = fr.read()
        word_list = re.split("[\d\s\,\.\(\)\:]+", text_str)
        word_dic = {}
        word_num = 0
        for _word in word_list:
            word_l = _word.lower()
            if word_l in stop:
                continue
            if word_l not in word_dic:
               word_dic[word_l] = 0
            word_dic[word_l] += 1
            word_num += 1
        tf = {}
        for k, v in word_dic.items():
            tf[(k, file_path)] = v / word_num
            print(tf)




# def word_count_dic(word_list):
#     word_dic = {}
#     for _word in word_list:
#         word_l = _word.lower()
#         print(word_l)
#         if word_l not in word_dic:
#             word_dic[word_l] = 0
#         word_dic[word_l] += 1
#         print(word_dic)
#     return word_dic





def main():
    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        read_txt(file_path)



if __name__ == '__main__':
  main()



