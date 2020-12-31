class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        d = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
        arr = []
        for i in range(n):
            arr.append(1)

        prev_chk=n-1
        for i in range(n-1,-1,-1):
            if k-prev_chk>26:
                arr[i]=26
                k-=26
                prev_chk-=1
            else:
                arr[i] = k-prev_chk
                break
        str1=""
        for i in range(n):
            str1 += d[arr[i]]

        return str1
