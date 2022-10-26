public String noX(String str) {
    if (str.length() == 0) return str;
    else{
      char letter = str.charAt(0);
      if (letter == 'x') return noX(str.substring(1));
      else return letter + noX(str.substring(1));
    }
  }