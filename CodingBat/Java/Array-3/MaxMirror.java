public class MaxMirror {
    
    public static void main(String[] args){
        System.out.println(maxMirror(new int[]{1,1,1,1}));
        System.out.println(maxMirror(new int[]{3,3}));
        System.out.println(maxMirror(new int[]{1}));
    }

    public static int maxMirror(int[] nums) {
  
        // two pointers at duplicate
        // keep going until no more matching (record the size)
        // or until they meet in the middle (max size)

        int maxLength = 0;
        
        for (int i = 0; i <= nums.length - 1; i++){
          
          // find duplicates

            for (int j = nums.length - 1; j >= i; j--){
            
                // if duplicate is found
                if (nums[i] == nums[j]){
                    int a = i;
                    int b = j;
                    int count = 0;

                    // check if it's a mirror, add to count
                    while (a < b && nums[a] == nums[b]){
                        count++;
                        a++;
                        b--;
                    }

                    // full length mirror
                    if (a == b){ // odd length, size 1
                        count += (count + 1);
                    }else if (a > b){ // even
                        count *= 2;
                    }
                    maxLength = Math.max(maxLength, count);

                }
            
            }
        }
        
        return maxLength;
        
    }
      
}
