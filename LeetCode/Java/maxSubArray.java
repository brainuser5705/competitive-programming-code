package Java;
/*
    First attempt with dynamic programming 
    
 public int maxSubArray(int[] nums) {
        
        // Create a table to store all the values
        int[][] table = new int[nums.length][nums.length];
            
        // the value that we are returning
        // we start with the first element of the array (not 0) 
        // ex. array [-1] max would be -1 not 0
        int max = nums[0];
        
        // double for loops: for every start index of the subarray,
        // look at every possible end index up to the last index of the array
        for (int start = 0; start < nums.length; start++){
            for (int end = start; end < nums.length; end++){

                // the value to add
                int value = 0;

                if (start == end){  
                    // if it is the same index, then 
                    // the value to add is just the number
                    value = nums[end];
                }else{
                    // ow it would be the previous entry (of the same start index)
                    // plus the number
                    value = table[start][end-1] + nums[end];
                }

                // lastly, assign the value into the dp table
                table[start][end] = value;
                
                // change the return value if applicable
                if (value > max){
                    max = value;
                }
            }
        }
        
        return max;
        
    }
 */

class Solution {
    public int maxSubArray(int[] nums) {
            
        int max = nums[0];

        int currentSum = 0;
        
        // for each start index - same for loop conditions as first attempt
        for (int start = 0; start < nums.length; start++){
            
            // we start with 0 at the start index
            currentSum = 0;
            
            for (int end = start; end < nums.length; end++){
            
                // as we loop through the possible end indices,
                // we add the numbers of the array
                if (start == end){
                    currentSum = nums[end]; // or nums[end]
                }else{
                    currentSum += nums[end];
                }
                
                // for each loop, we change max
                if (currentSum > max){
                    max = currentSum;
                }
                
            }
            
        }
        
        return max;
        
    }
}