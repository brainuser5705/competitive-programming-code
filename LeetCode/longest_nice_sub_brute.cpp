class Solution {
public:
    string longestNiceSubstring(string s) {

        string longestSub = "";
        int longestLen = 0;

        for (int i = 0; i < s.length()-1; i++){

            string sub(1, s[i]);

            for (int j = i+1; j < s.length(); j++){
                sub += s[j];
                if (isNice(sub) && sub.length() > longestLen){
                    longestSub = sub;
                    longestLen = sub.length();
                }
            }

        }

        return longestSub;

    }

    bool isNice(string sub){

        std::unordered_map<char, bool> cs;

        for (int i = 0; i < sub.length(); i++){

            char c = sub[i];

            // if pair has been encountered already
            if (cs.find(c) != cs.end() && cs[c]){
                continue;
            }else{
                char niceC = c ^ (1 << 5); // gets character in the opposite case

                // opposite case already encountered
                if (cs.find(niceC) != cs.end()){
                    cs[niceC] = true; // set both cases to true
                    cs[c] = true;
                }else{
                    cs[c] = false;
                }
            }

        }

        // all entries in map will have true values if nice
        for (auto it = cs.begin(); it != cs.end(); it++){
            if (!(it->second)){
                return false;
            }
        }

        return true;

    }

};
