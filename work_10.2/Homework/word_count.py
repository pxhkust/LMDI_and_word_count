import os
import re
import math



def main():
    data_dir = "./Email/"
    stop = set(["a", "the", "this", "that", "an", "and",
                "are", "is", "", "on", "in", "for", "it",
                "to", "as", "also", "yet", "both", "from",
                "of", "been", "being", "while", "their",
                "be", "by", "only", "your", "you", "with"])  # 禁用词表

    # 计算tf
    tf = {}
    doc_num = 0
    for file_name in os.listdir(data_dir):
        doc_num += 1
        file_path = os.path.join(data_dir, file_name)
        with open(file_path, "r") as fr:
            text_str = fr.read()
        word_list = re.split("[\d\s\,\.\(\)\:]+", text_str)
        word_count_dic = {}
        word_num = 0
        for _word in word_list:
            word = _word.lower()
            if word in stop:
                continue
            if word not in word_count_dic:
                word_count_dic[word] = 0
            word_count_dic[word] += 1
            word_num += 1
        for k, v in word_count_dic.items():
            tf[(k, file_name)] = v/word_num

    # 计算idf
    word_exist_in_file_num = {}
    for word, file_name in tf.keys():
        if word not in word_exist_in_file_num:
            word_exist_in_file_num[word] = 0
        word_exist_in_file_num[word] += 1
    idf = {}
    for k, v in word_exist_in_file_num.items():
        idf[k] = math.log(v/(1+doc_num))

    # 计算tf_idf
    tf_idf = {}
    for k, v in tf.items():
        word, file_name = k
        tf_idf[k] = v * idf[word]

    # 排序输出（全局）
    sort_tf_idf = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)
    # for k, v in sort_tf_idf:
    #     # print(k, v)

    # 按文档排序
    tf_idf_file = {}
    for (word, file_name), tf_idf_val in tf_idf.items():
        if file_name not in tf_idf_file:
            tf_idf_file[file_name] = {}
        tf_idf_file[file_name][word] = tf_idf_val
    for k, v in tf_idf_file.items():
        sort_tf_idf_each_file = sorted(v.items(), key=lambda x: x[1], reverse=True)[:20]
        print(k)
        for word, tf_idf_val in sort_tf_idf_each_file:
            print(word, tf_idf_val)
        print("-"*100)




if __name__ == '__main__':
  main()



