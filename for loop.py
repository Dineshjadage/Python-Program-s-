"""program to demonatarte for loop"""

for i in range(5):
    print(1,"Tom")

for j in range(2,5):
    print(j,"jack")

for i in range(2,10,2):
    print(i,"Roose")

for i in range(5):
    if i==2:break
    print(i,"break")

for i in range(5):
    if i==2:continue
    print(i,"continue")


"""output:
1 Tom
1 Tom
1 Tom
1 Tom
1 Tom
2 jack
3 jack
4 jack
2 Roose
4 Roose
6 Roose
8 Roose
0 break
1 break
0 continue
1 continue
3 continue
4 continue"""
