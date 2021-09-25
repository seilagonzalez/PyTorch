import csv
import os
import glob
import pandas as pd


def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


path = "/Users/seila/Documents/PyTorch/pythontest/YSRJ/test"
all_files = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
last_header = None
total = 0
for f in all_files:
    data = pd.read_csv(f)
    header1=list(data.columns.values)
    if last_header == None:
        last_header = header1
        lines = data[data.columns[0]].count()
        print(f)
        print(lines)
        total += lines
    elif header1 != last_header:
        print("Some information to user")
        diff = Diff(last_header, header1)
        print(diff)  
        quit()
    else:
        print(f)
        lines = data[data.columns[0]].count()
        print(lines)
        total+= lines
print(total)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv("merged.csv")
total_merge = df_merged[df_merged.columns[0]].count()
print(total_merge)
