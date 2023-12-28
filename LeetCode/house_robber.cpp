class Solution {
public:
    int rob(vector<int>& nums) {

        int size = nums.size();

        if (size == 1){
            return nums[0];
        }
        
        int nonAdjMax = nums[0];
        int adjMax = nums[1];
        int maxAmount = max(nonAdjMax, adjMax);

        vector<int> amounts = nums;
        for (int i = 2; i < size; i++){
            amounts[i] = nonAdjMax + nums[i];
            maxAmount = max(maxAmount, amounts[i]);

            nonAdjMax = max(nonAdjMax, adjMax);
            adjMax = amounts[i];
        }

        return maxAmount;

    }
};
