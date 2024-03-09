#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {

    int n, m, k;
    cin >> n >> m >> k;

    multiset<int> desired;
    int in;
    for (int i = 0; i < n; i++){
        cin >> in;
        desired.insert(in);
    }

    multiset<int> sizes;
    for (int i = 0; i < m; i++){
        cin >> in;
        sizes.insert(in);
    }

    int count = 0;
    for (int d : desired){
        auto it = sizes.lower_bound(d - k);
        if (it != sizes.end() && *it <= (d + k)){
            sizes.erase(it);
            count++;
        }
    }

    cout << count;




}
