class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k==0:
            seen = {}
            for i in range(len(nums)):
                if nums[i]==0 and nums[i] not in seen:
                    seen[nums[i]] = i
                elif nums[i]==0 and nums[i] in seen:
                    if i-seen[nums[i]]==1:
                        return True
                    else:
                        seen[nums[i]] =i
            return False
        else:
            prefix_arr = []
            prefix_modulo_arr = []
            seen  ={nums[0]%k:0}
            res = False

            prefix_arr.append(nums[0])
            for i in range(1,len(nums)):
                a = prefix_arr[i-1]+nums[i]
                prefix_arr.append(a)
                if a%k==0:
                    return True
                else:
                    #print(seen)
                    #print(a%k)
                    if a%k not in seen:
                        seen[a%k] = i
                    elif a%k in seen:
                        if i - seen[a%k]>=2:
                            return True
            return False
