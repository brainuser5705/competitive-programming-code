#include <iostream>

using namespace std;

int main(){

    int h;
    int m;

    cin >> h >> m;

    if ((m -= 45) < 0){
        if (h == 0){
            h = 23;
        }else{
            h -= 1;
        }
        m = 60 + m;
    }

    cout << h << " " << m;

}