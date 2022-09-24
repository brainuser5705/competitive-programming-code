#include <iostream>

using namespace std;

int main(){

    int x, n, m, total;
    cin >> x >> n;

    total = (n+1) * x;
    for (int i = 0; i < n; i++){
        cin >> m;
        total -= m;
    }

    cout << total;
}