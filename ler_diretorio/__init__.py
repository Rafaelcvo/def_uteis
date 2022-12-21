import os

path_read = ""

txt_list = os.listdir(path_read)

for txt in txt_list:
    if txt.endswith(".txt"):
        print(txt)