#include <iostream>
#include <set>

using namespace std;

int main() {

    int x, n;
    cin >> x >> n;

    set<int> positions{0, x};
    multiset<int> dists{x};

    int p;
    for (int i = 0; i < n; i++){
        cin >> p;
        auto right = positions.upper_bound(p);
        auto left = prev(right, 1);

        dists.erase(dists.find(*right - *left)); // remove only one instance
        dists.insert(*right - p);
        dists.insert(p - *left);

        positions.insert(p);

        cout << *prev(dists.end(), 1) << " ";
    }


}

// backwards removal
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {

    int x, n;
    cin >> x >> n;

    vector<int> positions;
    set<int> sortedPositions{0, x};

    int in;
    for (int i = 0; i < n; i++){
        cin >> in;
        positions.push_back(in);
        sortedPositions.insert(in);
    }

    // finding the max gap when all traffic lights have been set
    int prevP = 0;
    int maxGap = 0;
    for (int p : sortedPositions){
        maxGap = max(maxGap, p - prevP);
        prevP = p;
    }

    vector<int> gaps;
    gaps.push_back(maxGap);
    for (int i = n-1; i >= 0; i--){ // need to remove positions backwards from input
        int p = positions[i];
        // remove the position
        sortedPositions.erase(p);
        // find the new gap created and replace maxGap is necessary
        auto right = sortedPositions.upper_bound(p);
        auto left = prev(right, 1);
        maxGap = max(maxGap, *right - *left);
        gaps.push_back(maxGap);
    }

    for (int i = n-1; i >= 0; i--){
        cout << gaps[i] << " ";
    }



}
