public int countHi2(String str) {
  
    // base case
    if (str.length() <= 1) return 0;
  
    // check first two characters to see if it starts with hi
    // length 2 should not matter for substring, since it will return an empty string
    if (str.substring(0,2).equals("hi")) return 1 + countHi2(str.substring(2));
      
    // if string is long enough, check for hi
    if (str.length() >= 3 && str.substring(1,3).equals("hi"))
      if (str.charAt(0) != 'x') return 1 + countHi2(str.substring(3));
      else return countHi2(str.substring(3));
    
    // otherwise move to next letter
    return countHi2(str.substring(1));
    
  }
  