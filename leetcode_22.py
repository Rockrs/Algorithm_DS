class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        arr =[]
        def recur(A,op,cl):
            if op==cl==n:
                arr.append(A)
                return
            if cl>op:
                return
            if op>n or cl>n:
                return
            else:
                recur(A+"(",op+1,cl)
                recur(A+")",op,cl+1)
                return

        recur("",0,0)
        return arr
