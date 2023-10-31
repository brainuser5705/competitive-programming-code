class Solution {
public:
    bool isSubsequence(string s, string t) {
        
        int sSize = s.size();
        int tSize = t.size();

        // subsequence cannot have a greater length than original string
        if (sSize > tSize) return false;

        int sPtr = 0;
        int tPtr = -1; // will be incremented first before comparison

        char c = s[sPtr];
        while (sPtr < sSize){
            
            tPtr++;

            if (t[tPtr] == c){
                sPtr++;
                c = s[sPtr];    
            }else if (tPtr == tSize){
                return false;
            }

        }

        return true;

    }
};
