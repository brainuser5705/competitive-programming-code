class Solution {
public:
    int compress(vector<char>& chars) {
        int charsLen = chars.size();
        
        char currChar = chars[0];
        int ptr = 0;
        int count = 1;
        ostringstream os;

        int i = 1;
        while (i < charsLen){
            if (chars[i] != currChar){
                chars[ptr] = currChar;
                if (count > 1 && count < 10){
                    chars[ptr + 1] = count + 48; // ASCII 48 = '0'
                    ptr += 2;
                }else if (count >= 10){
                    int j = 1;
                    os.str(""); // resets the string
                    os << count;
                    for (char digit : os.str()){
                        chars[ptr + j] = digit;
                        j += 1;
                    }
                    ptr += j;
                }else{ // move on if count == 1
                    ptr += 1;
                }
                count = 0;
                currChar = chars[i];
            }else{
                count += 1;
                i++;
            }
        }

        // for last character
        chars[ptr] = currChar;
        if (count > 1 && count < 10){
            chars[ptr + 1] = count + 48; // ASCII 48 = '0'
            ptr += 2;
        }else if (count >= 10){
            int j = 1;
            os.str("");
            os << count;
            for (char digit : os.str()){
                cout << digit << "\n";
                cout << ptr + j << "\n";
                chars[ptr + j] = digit;
                j += 1;
            }
            ptr += j;
        }else{
            ptr += 1;
        }

        return ptr;
    }
};
