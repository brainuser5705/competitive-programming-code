public String stringClean(String str) {

    if (str.length() <= 1) return str;
    else if (str.charAt(1) == str.charAt(0)) return stringClean(str.substring(1));
    else return str.charAt(0) + stringClean(str.substring(1));
  }