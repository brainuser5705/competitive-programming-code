class Solution {
public:
    string longestNiceSubstring(string s) {

        // special case of single character
        if (s.length() == 1){
            return "";
        }

        for (int i = 0; i < s.length(); i++){

            char niceCase = s[i] ^ (1 << 5); // get opposite case of character

            // if opposite case is not in the string
            if (s.find(niceCase) == string::npos){
                // divide at the character
                string s1 = longestNiceSubstring(s.substr(0, i));
                string s2 = longestNiceSubstring(s.substr(i+1));
                if (s1.length() < s2.length()){
                    return s2;
                }else{
                    return s1; // return earliest occurence if lengths are equal
                }
            }
        }

        // return the full string if all the characters have opposite cases
        return s;

    }

};
