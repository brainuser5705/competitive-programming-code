#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {

    int n, m;
    cin >> n >> m;

    multiset<int> prices;
    int in;
    for (int i = 0; i < n; i++){
        cin >> in;
        prices.insert(in);
    }

    for (int i = 0; i < m; i++){
        cin >> in;

        // either gets the max price, or a price greater than max
        auto low = prices.lower_bound(in);

        if (low != prices.begin() || *low == in) {
            // the case that either not the first element, or it is and the price is equal to max
            if (*low != in) {
                // only checks in the case that low is not the first element
                --low;
            }
            cout << *low;
            prices.erase(low);
        }else{
            // the case that low is the first element and price is greater than max
            cout << -1;
        }
        
        cout << endl;
    }


}

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
 
 
using namespace std;
 
int main() {
 
    int numTickets, numCustomers;
    multiset<int> ticketPrices;
    vector<int>  customerPrices;
    int price; // holds input
 
    cin >> numTickets >> numCustomers;
 
    for (int i = 0; i < numTickets; i++){
        cin >> price;
        ticketPrices.insert(price);
    }
 
    for (int i = 0; i < numCustomers; i++){
 
        // no more tickets left
        if (i >= numTickets){
            cout << -1 << endl;
            continue;
        }
 
        cin >> price;
        auto it = ticketPrices.lower_bound(price);
        if (it == ticketPrices.begin()){
            if (*it > price){
                cout << -1 << endl;
                continue;
            }
        }else if (it == ticketPrices.end() || *it > price){
            it = prev(it,1);
        }
        cout << *it << endl;
        ticketPrices.erase(it);
    }
 

