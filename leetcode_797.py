class Solution(object):
    def allPathsSourceTarget(self, graph):
        ans =[]

        def cal(a,b):
            if b[-1]==len(graph)-1:
                ans.append(b)
            else:
                for index,val in enumerate(a):
                    if val==len(graph)-1:
                        ans.append(b+[val])
                    else:
                        cal(graph[val],b+[val])
            return


        cal(graph[0],[0])
        #print(ans)
        return ans
