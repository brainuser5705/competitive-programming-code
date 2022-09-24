#include <iostream>

using namespace std;

int main(){

    int x, y, n;
    cin >> x >> y >> n;

    for (int i = 1; i <= n; i++){
        if(!(i % x)){
            cout << "Fizz";
        }
        if (!(i % y)){
            cout << "Buzz";
        }else if (i % x){
            cout << i;
        }

        cout << "\n";
    }

}