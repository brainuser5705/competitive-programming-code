#include <iostream>

using namespace std;

int main(){

    int r;
    int c;

    cin >> r >> c;

    // full radius minus the crust length
    double cheese = r - c;

    printf("%.6f", (cheese*cheese) / (r*r) * 100); 

}