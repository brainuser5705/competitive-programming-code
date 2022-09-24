#include <iostream>

using namespace std;

int main(){

    int i, n, temp, count = 0;
    cin >> n;

    for (i = 0; i < n; i++){
        cin >> temp;
        if (temp < 0)
            count++;
    }

    cout << count;
}