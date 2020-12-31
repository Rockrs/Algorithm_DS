class Solution:
    def nextPermutation(self, perm: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(perm)
        if n==1:
            pass
        else:
            swap_v =0
            swap_i = 0
            index=n-1

            while(index>=0):
                if index==0:
                    pass
                else:
                    if perm[index-1]<perm[index]:
                        swap_v = perm[index-1]
                        for i in range(index,n):
                            if perm[i]>swap_v:
                                swap_i = i
                        perm[index-1] ,perm[swap_i] = perm[swap_i],perm[index-1]
                        index-=1
                        break
                index-=1

            print (index)
            l = index+1
            r = n-1
            while(l<=r):
                perm[l],perm[r] = perm[r],perm[l]
                l+=1
                r-=1
