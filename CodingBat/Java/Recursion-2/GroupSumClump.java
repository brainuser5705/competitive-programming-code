public boolean groupSumClump(int start, int[] nums, int target) {
    if (target == 0)
      return true;
    else if (start < nums.length){
      int num = nums[start];
      int i = start;
      for (i = start+1;i < nums.length && nums[i] == num; i++);
      return groupSumClump(i, nums, target-(num*(i-start))) || groupSumClump(i, nums, target);
    }
    return false;
    
  }