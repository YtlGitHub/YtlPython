f1 = open("new1.txt","r",encoding="UTF_8")
f01 = f1.readlines()
print(f01)
f2 = open("new2.txt","r",encoding="UTF_8")
f02 = f2.readlines()
print(f02)
for i in f01:
    if i not in f02:
        print(i)
