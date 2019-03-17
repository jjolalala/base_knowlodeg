a = [11, 22, 33, 44, 55, 66]
for i in a:
    if i == 33:
        a.remove(i)
# 当i=33被删除的时候，i=44会接替i=33的位置


for i in a:
    if i == 33 & i ==44:
        a.remove(i)



# 解决办法
b = []
for i in a:
    if i == 33 or i ==44:
        b.append(i)

for i in b:
    if i == 33 or i == 44:
        a.remove(i)
