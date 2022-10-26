public boolean strCopies(String str, String sub, int n) {
  
    int subLength = sub.length();
    
    if (n == 0) return true;
    else if (str.length() < subLength) return false;
    else if (str.substring(0,subLength).equals(sub)) return strCopies(str.substring(1), sub, n-1);
    else return strCopies(str.substring(1), sub, n);
    
  }
  