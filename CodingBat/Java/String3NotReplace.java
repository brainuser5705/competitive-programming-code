public String notReplace(String str) {
  
  String[] words = str.split("[^a-zA-Z]");
  
  String[] spaces = str.split("[a-zA-Z]{1,}");
  
  String finalStr = "";
  for (int i = 0; i < words.length; i++){
    
    if (i < spaces.length){
      finalStr += spaces[i];
    }
    
    finalStr += words[i];
    if (words[i].equals("is")){
      finalStr += " not";
    }
    
  }
  
  return finalStr;
  
}
