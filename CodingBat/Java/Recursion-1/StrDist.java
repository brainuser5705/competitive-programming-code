public int strDist(String str, String sub) {
  
    int subLength = sub.length();
    
    // there is no substring in the string
    if (str.length() == 0 || str.length() < subLength){
      return 0;
    }
    
    // parse front
    if (!(str.substring(0, subLength).equals(sub))){
      return strDist(str.substring(1), sub);
    }
    
    // parse back
    if (!(str.substring(str.length()-subLength).equals(sub))){
      return strDist(str.substring(0, str.length()-1), sub);
    }
    
    // length of the remaining string
    return str.length();
  }
  