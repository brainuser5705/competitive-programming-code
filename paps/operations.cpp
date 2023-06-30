#include <iostream>

using namespace std;

int main(){
    int a = 1;
    int b = 1;

    //cin >> a >> b;

    // if b is 0, then a runtime error will occur
    // remainder is negative is a is negative
    cout << "Remainder: " << (a%b) << endl;
    cout << "Quotient: " << (a/b) << endl;

    // to bypass integer divison, one of the operands must be a double
    int c = 6;
    int d = 4;
    cout << (c/d) << endl;

    double aa = 6.0;
    double bb = 4.0;
    cout << (aa/bb) << endl;

    int e; // assigns a random address
    cout << e << endl;
}