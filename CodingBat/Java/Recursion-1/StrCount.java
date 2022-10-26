public int strCount(String str, String sub) {
  
    int subLength = sub.length();
    
    if (str.length() < subLength) return 0;
    else if (str.substring(0,subLength).equals(sub)) return 1 + strCount(str.substring(subLength), sub);
    else return strCount(str.substring(1),sub);
    
  }
  