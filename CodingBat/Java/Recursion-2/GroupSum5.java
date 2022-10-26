public boolean groupSum5(int start, int[] nums, int target) {
    if (start == nums.length)
      return target == 0;
    else if (start < nums.length){
      int num = nums[start];
      if (start < nums.length-1 && num % 5 == 0 && nums[start+1] == 1)
        return groupSum5(start+2, nums, target-num);
      else{
        boolean added = groupSum5(start+1, nums, target-num);
        if (nums[start] % 5 == 0) return added;
        return added || groupSum5(start+1, nums, target);
      }
    }else
      return false;
      
  }