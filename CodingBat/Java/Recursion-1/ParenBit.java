public String parenBit(String str) {
    return recursiveCall(str, false);
  }
  
  public String recursiveCall(String str, boolean in){
    
    if (str.charAt(0) == ')') return ")";
    else if (str.charAt(0) == '(') return '(' + recursiveCall(str.substring(1), true);
    else {
      if (in) return str.charAt(0) + recursiveCall(str.substring(1), true);
      else return recursiveCall(str.substring(1), false);
    }
    
  }

// smart way

public String parenBit(String str) {
  if (str.charAt(0) != '(') {
    return parenBit(str.substring(1));
  }
  if (str.charAt(str.length()-1) != ')') {
    return parenBit(str.substring(0, str.length()-1));
  }
  return str;
  
  // Solution notes: this is tricky. Is the first char a '('?
  // If not, recur, removing one char from the left of the string.
  // Eventually this gets us to '(' at the start of the string.
  // If the first char is '(', then recur similarly, removing one char from
  // the end of the string, until it is ')'.
  // Now the first and last chars are ( .. ) and you're done.
}
