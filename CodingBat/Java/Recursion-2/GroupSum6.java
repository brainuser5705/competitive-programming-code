public boolean groupSum6(int start, int[] nums, int target) {
    if (start == nums.length){
      return target == 0;
    }else if (start < nums.length){
      int num = nums[start];
      boolean added = groupSum6(start+1, nums, target-num);
      if (num == 6)
        return added;
      else
        return added || groupSum6(start+1, nums, target);
    }else{
      return false;
    }
  }