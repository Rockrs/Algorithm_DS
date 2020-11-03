import re
class Solution(object):
    def calculate(self, s):
        st = list(s.replace(" ",""))

        sym_st = []
        op_st = []
        eval_list = []

        i=0

        char=""
        while(i<len(st)):
            if st[i] not in ['+','-',')','(']:
                char += st[i]
                if i==len(st)-1:
                    op_st.append(char)
            else:
                op_st.append(char)
                char=""
                if st[i]=='(':
                    sym_st.append('(')
                elif st[i]==')':
                    while sym_st[-1]!='(':
                        op_st.append(sym_st.pop())
                    sym_st.pop()
                elif st[i]=='+' or st[i]=='-':
                    while sym_st!=[]:
                        if sym_st[-1]=='(':
                            break
                        else:
                            op_st.append(sym_st.pop())
                    sym_st.append(st[i])
            #print(op_st)
            #print(sym_st)

            i+=1

        while (sym_st!=[]):
            op_st.append(sym_st.pop())

        print(op_st)

        if any(item=='+' for item in op_st) or any(item=='-' for item in op_st):
            for i in range(len(op_st)):
                if op_st[i]=='+' or op_st[i]=='-':
                    a = eval_list.pop()
                    b = eval_list.pop()

                    if op_st[i]=='+':
                        eval_list.append(a+b)
                    elif op_st[i]=='-':
                        eval_list.append(b-a)
                else:
                    if op_st[i]!='':
                        eval_list.append(int(op_st[i]))
            return eval_list[0]
        else:
            for i in range(len(op_st)):
                if op_st[i]!='':
                    return op_st[i]
