public String pairStar(String str) {
  
    if (str.length() <= 1) return str;
    else{
      char letter1 = str.charAt(0);
      char letter2 = str.charAt(1);
      if (letter1 == letter2) return letter1 + "*" + pairStar(str.substring(1));
      return letter1 + pairStar(str.substring(1));
    }
  }
  