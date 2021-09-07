

import os

with open("production/bom_grouped.csv","r") as fr:
    with open("temp.txt","w") as fw:
        header = fr.readline().strip().split('","')
        header_len = len(header)
        fw.write("|"+"|".join([item.strip('"') for item in header])+"|\n")
        fw.write("|---"*header_len+"|\n")
        for line in fr:
            tbl_line = "|"+"|".join([item.strip('"').replace(":"," ").replace("_"," ") for item in line.strip().split('","')])+"|\n"
            fw.write(tbl_line)

os.system("cat README_preamble.txt > README.md")
os.system("cat temp.txt >> README.md")
os.system("rm temp.txt")
