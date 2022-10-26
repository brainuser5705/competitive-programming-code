public int countX(String str) {
    return countXRecursive(str, 0);
  }
  
  public int countXRecursive(String str, int count){
    if (str.length() == 0) return count;
    else if (str.charAt(0) == 'x') return countXRecursive(str.substring(1,str.length()), count+1);
    else return countXRecursive(str.substring(1,str.length()), count);
  }