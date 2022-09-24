#include <iostream>
using namespace std;

/* Returns 0 if equal, -1 if name1 < name2, 1 if name1 > name2 */ 
int compare(string name1, string name2){
    
    int size1 = name1.size(), size2 = name2.size();
    int minLen = min(size1, size2);
    for (int i = 0; i < minLen; i++){
        if (name1[i] < name2[i]){
            return -1;
        }else if (name2[i] < name1[i]){
            return 1;
        }
    }

    if (size1 < size2){
        return -1;
    }else if (size2 < size1){
        return 1;
    }

    return 0;

}

int main(){

    int numNames, value, prevValue = 2;
    string prevName, name;
    bool neither = false;
    cin >> numNames;

    cin >> prevName;
    for (int i = 0; i < numNames - 1; i++){
        cin >> name;
        value = compare(prevName, name);

        // 2 is a dummy value to bypass the first iteration
        if (prevValue != 2 && value != prevValue){
            neither = true;
        }

        prevValue = value;
        prevName = name;
    }

    if (neither){
        cout << "NEITHER";
    }else if (value == 1){
        cout << "DECREASING";
    }else if (prevValue == -1){
        cout << "INCREASING";
    }else{
        cout << "NEITHER";
    }
    
}