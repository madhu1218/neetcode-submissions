from typing import List

def read_integers() -> List[int]:
    num = input()
    listNum = num.split(",")
    for i in range(len(listNum)):
        listNum[i] = int(listNum[i])
    return listNum

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
