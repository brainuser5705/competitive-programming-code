public boolean array220(int[] nums, int index) {
  
    if (index == nums.length) return false;
    else if (array220Recursive(nums, index, nums[index]*10)) return true;
    else return array220(nums, index+1);
  }
  
  public boolean array220Recursive(int[] nums, int index, int target){
    
    if (index == nums.length) return false;
    else if (nums[index] == target) return true;
    else return array220Recursive(nums, index+1, target);
     
  }