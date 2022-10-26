public boolean groupNoAdj(int start, int[] nums, int target) {
    if (target == 0)
      return true;
    else if (start < nums.length){
      boolean even = groupNoAdj(start+1, nums, target); // no add
      boolean odd = groupNoAdj(start+2, nums, target-nums[start]); // add
      return even || odd;
    }
    else
      return false;
  }