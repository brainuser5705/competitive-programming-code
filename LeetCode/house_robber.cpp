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

// Don't need maxAmount or to copy nums vector

class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() == 1){
            return nums[0];
        }

        int nonAdjMax = nums[0];
        int adjMax = nums[1];

        int amt;
        for (int i = 2; i < nums.size(); i++){

            // get the max amount at current position
            // note that nonAdjMax has not been updated yet
            amt = nums[i] + nonAdjMax;
            
            // update nonAdjMax with old adjMax first
            nonAdjMax = max(nonAdjMax, adjMax);

            // finally update the adjMax
            adjMax = amt;

        }


        return max(nonAdjMax, adjMax);
        
    }
};
