public int countHi(String str) {
    return countHiRecursive(str, 0);
  }
  
  public int countHiRecursive(String str, int count){
    if (str.length() < 2) return count;
    else if (str.substring(0,2).equals("hi")) return countHiRecursive(str.substring(2,str.length()),count+1);
    else return countHiRecursive(str.substring(1,str.length()), count);
  }
  