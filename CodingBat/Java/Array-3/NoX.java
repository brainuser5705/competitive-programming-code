public List<String> noX(List<String> strings) {
    strings.replaceAll(s -> stripX(s));
    return strings;
  }
  
  public String stripX(String string){
    String result = "";
    for (int i = 0; i < string.length(); i++){
      if (string.charAt(i) != 'x'){
        result += string.charAt(i);
      }
    }
    return result;
  }
  
---

public List<String> noX(List<String> strings) {
  strings.replaceAll(s -> s.replaceAll("x", ""));
  return strings;
}