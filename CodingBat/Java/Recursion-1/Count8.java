public int count8(int n) {
    return is8(n, 0, false);
  }
  
  public int is8 (int n, int count, boolean before){
    
    if (n == 0) return count;
    
    if (n % 10 == 8){
      if (before){
        // continuing the 8 train
        count += 2;
      }else{
        // first 8!
        count++;
        before = true;
      }
    }else{
      // resets the boolean
      before = false;
    }
    
    return is8(n / 10, count, before);
  }
  