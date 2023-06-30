#include <iostream>

using namespace std;

// must be declared before main
void change(int &val){
    val = 0;
}

int main(){
    int variable = 100;
    cout << "Variable is " << variable << endl;
    change(variable);
    cout << "Variable is " << variable << endl;
}