public boolean groupSum(int start, int[] nums, int target) {
  
    if (target==0){
      return true;
    }else if (start < nums.length){
      // either add the number or not
      return groupSum(start+1, nums, target-nums[start]) || groupSum(start+1, nums, target);
    }
    return false;
    
  }