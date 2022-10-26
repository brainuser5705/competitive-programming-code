public String changeXY(String str) {
  
    if (str.length() == 0) return str;
    else{
      char letter = str.charAt(0);
      if (letter == 'x') return 'y' + changeXY(str.substring(1,str.length()));
      else return letter + changeXY(str.substring(1,str.length()));
  }
    
  }
  