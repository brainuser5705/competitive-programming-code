public int countAbc(String str) {
    if (str.length() < 3) return 0;
    else{
      String sub = str.substring(0,3);
      if (sub.equals("abc") || sub.equals("aba")) return 1 + countAbc(str.substring(1));
      return countAbc(str.substring(1));
    } 
  }