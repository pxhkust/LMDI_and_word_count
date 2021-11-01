import os

data_dir = "work_10.2/"

def read_abstract(file_name):
    with open("%s.txt" % file_name, "r") as f:
      context = f.read().split(" ")
    return context



# def main():
#     context = read_paper(file_name)
#     word_list = paper_word_list(context)
#     word_dic = paper_word_dic{word_list}

def main():
    for file_name in os.listdir(data_dir):
        if ".txt" in file_name:
            continue
        file_real_name = file_name.split(".")[0]
        print(file_real_name)
        read_abstract(file_real_name)


#
if __name__ == '__main__':
  main()
