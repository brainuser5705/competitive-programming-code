#include <iostream>

using namespace std;

int main(){

    int r, n, line;
    cin >> r >> n;

    // boolean pointer
    bool* rooms = new bool[r+1];

    for (int i = 1; i <= n; i++){
        cin >> line;
        rooms[line] = true;
    }

    int i = 1;
    while (i <= r){
        if (!(rooms[i])){
            cout << i << endl;
            return 0;
        }
        i++;
    }

    cout << "too late" << endl;

}