public String endX(String str) {
  
    if (str.length() == 0) return str;
    else{
      char letter = str.charAt(0);
      if (letter == 'x') return endX(str.substring(1)) + 'x';
      else return letter + endX(str.substring(1));
    }
  }
  