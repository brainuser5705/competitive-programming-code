#include <iostream>

// give certain types new names;
typedef long long ll;

using namespace std;

int main(){
    int five = 5;
    cout << five << endl;
    int seven = 7;
    cout << seven << endl;

    five = seven + 2;
    cout << five << endl;

    seven = 0;
    cout << five << endl;
    cout << 5 << endl;

    // 5 7 9 9 5


    // constat values with modifier `const`
    // immutable values
    const int FIVE = 5;

    // 8 22 0
    int a = 4;
    int b = 2;
    int c = 7;

    b = a + c;
    c = b - 2;
    a = a + a;
    b = b * 2;
    c = c - c;

    cout << a << "\n" << b << "\n" << c;

    // performs integer divison
    cout << (5/3) << endl;
    cout << (15 / 5) << endl;
    cout << (2 / 2) << endl;
    cout << (7 / 2) << endl;
    cout << (-7 / 2) << endl;
    cout << (7 / -2) << endl;

    char letter = '@';
    cout << letter << endl;

    int number = 7;
    cout << number << endl;

    long long largeNumber = 888888888888LL;
    cout << largeNumber << endl;

    // double for decimals
    // there is also float but double can represent more decimal numbers/higher precision
    double decimalNumber = 513.23;
    cout << decimalNumber << endl;

    bool thisisfalse = false;
    bool thisistrue = true;
    // will output 1 and 0
    cout << thisistrue << " and " << thisisfalse << endl;

    string text = "\\\"";
    cout << text << endl;

    int maxInt = INT_MAX;
    int minInt = INT_MIN;

    cout << "Max Int: " << endl;
    maxInt += 1;
    // this will now be the minInt
    cout << maxInt << endl;

    double maxDouble = __DBL_MAX__;
    cout << maxDouble << endl;

    // if typedefining the type is too long'
    // then use auto which assigns value at the same time the type is inferred
    auto str = "a string";
}