class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {

        vector<int> minCost = cost; // copy vectors

        // starting at second last index
        for (int i = cost.size()-3; i >= 0; i--){
            minCost[i] = minCost[i] + min(minCost[i+1], minCost[i+2]);
        }
        
        return min(minCost[0], minCost[1]);

    }
};
