import os
import keyboard
import time

filename = "test.txt"
n = 0
pbe = []
wszystkielinie = []
wszystkiehasla = []
with open(filename, 'r') as file:
    for line in file:
        wszystkielinie.append(line.strip())
        if line.strip().isdigit():
            n += 1
for c, j in enumerate(wszystkielinie):
    listapoboczna = []
    if j.isdigit():
        for i in range(4):
            listapoboczna.append(wszystkielinie[c + i])
        wszystkiehasla.append(listapoboczna)
for i in wszystkiehasla:
    if i[1].count('PBE') == 1:
        pbe.append(i[0])

for i in range(n):
    print(f"{i + 1}.  {wszystkiehasla[i][1]}\n")
nr_konta = int(input("Wybież na którym kącie byś pograł :\n"))
if pbe.count(str(nr_konta)) == 1:
    print("pbe ")
    os.system('start pbe.lnk')
else:
    os.system('start test.lnk')
time.sleep(7)
keyboard.write(wszystkiehasla[nr_konta - 1][2])
keyboard.press('TAB')
keyboard.write(wszystkiehasla[nr_konta - 1][3])
keyboard.press('enter')
