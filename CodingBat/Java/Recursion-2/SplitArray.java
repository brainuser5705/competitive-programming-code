public boolean splitArray(int[] nums) {
    return recursive(0, 0, 0, nums);
  }
  
  public boolean recursive(int start, int sum1, int sum2, int[] nums){
    
    if (start == nums.length){
      return sum1 == sum2;
    }else{
      int num = nums[start];
      return recursive(start+1, sum1+num, sum2, nums) || recursive(start+1, sum1, sum2+num, nums);
    }
    
  }