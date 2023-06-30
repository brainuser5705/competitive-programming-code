#include <iostream>

using namespace std;

int main(){

    int numArticles;
    int i;

    cin >> numArticles >> i;

    /* 
    Since the impact factor is always rounded up (ceiling) if decimal,
    we can find impact factor - 1 and add an additional citation 
    so that it will round up. 
    */
    cout << (i-1) * numArticles + 1;
}