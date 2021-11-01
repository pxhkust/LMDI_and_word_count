import numpy as np
import pandas as pd

m = 40  # 最终输出维度
n = 149  # 原始维度
init_row, init_col = 5, 3
init_total_col = 164
file_path = "2017.xlsx"

df1 = pd.read_excel(file_path, sheet_name="2017年全国投入产出表")
matrix1 = df1.iloc[init_row:init_row+n, init_col:init_col+n].to_numpy()
init_total = df1.iloc[init_row:init_row+n, init_total_col].to_numpy()

df2 = pd.read_excel(file_path, sheet_name="行")
matrix2 = df2.iloc[init_row:init_row+m, init_col:init_col+n].to_numpy()

df3 = pd.read_excel(file_path, sheet_name="列")
matrix3 = df3.iloc[init_row:init_row+n, init_col:init_col+m].to_numpy()

merge = matrix2.dot(matrix1).dot(matrix3)

df4 = pd.read_excel(file_path, sheet_name="new")
total = matrix2.dot(init_total)
A = np.divide(merge, total, out=np.zeros_like(merge), where=total!=0)
D = np.array(np.eye(m)-A, dtype="float64")
F = np.linalg.inv(D)

np.savetxt("Final_%s.csv" % m, F, delimiter=",")













