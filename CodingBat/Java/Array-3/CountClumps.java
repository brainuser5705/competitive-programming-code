public class CountClumps {
    
    public int countClumps(int[] nums) {
  
        int count = 0;
        int i = 0;
        
        boolean on = false;
        while (i < nums.length-1){
          
          if (nums[i] == nums[i+1]){
            on = true; 
          }else{
            if (on){
              count++;
              on = false;
            }
          }
          
          i++;
        }
        
        // final one
        if (on){
          count++;
        }
        
        return count;
    }
}

