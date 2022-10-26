public boolean split53(int[] nums) {
    return recursive(0,0,0,nums);
  }
  
  public boolean recursive(int start, int sum1, int sum2, int[] nums){
    if (start == nums.length){
      return sum1 == sum2;
    }else{
      int num = nums[start];
      if (num % 5 == 0){
        return recursive(start+1, sum1+num, sum2, nums);
      }else if (num % 3 == 0){
        return recursive(start+1, sum1, sum2+num, nums);
      }else{
        return recursive(start+1, sum1+num, sum2, nums) || recursive(start+1, sum1, sum2+num, nums);
      }
    }
  }
  