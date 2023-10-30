class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        int bound = nums.size();
        
        int nonZero = 0;
        int zero = 0;

        while (true){

            while (nonZero < bound && nums[nonZero] == 0){
                nonZero++;
            }

            while (zero < bound && nums[zero] != 0){
                zero++;
            }

            if (nonZero == bound || zero == bound){
                break;
            }else if (nonZero > zero){ // only swap if necessary
                int temp = nums[zero];
                nums[zero] = nums[nonZero];
                nums[nonZero] = temp;
            }else if (nonZero < zero){
                nonZero++;  // move on so the loop isn't stuck
                            // we keep the zero ptr the same since we are swapping with it
            }
        }
        
        
    }
};
