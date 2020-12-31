class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int ans=0;
        int n =nums.size();
        if  (n==1){
            ans =0;
        }
        else if (nums[0]>nums[1]){
            ans =0;
        }
        else if (nums[n-1]>nums[n-2]){
            ans = n-1;
        }
        else{
            for (int i=1;i<n-1;i++){
            if (nums[i]>nums[i+1] && nums[i]>nums[i-1]){
                ans =i;
                break;
            }
        }
        }
        return ans;

    }
};
