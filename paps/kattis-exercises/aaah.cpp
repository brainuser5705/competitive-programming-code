#include <iostream>

using namespace std;

int main(){

    string jon;
    string doc;

    cin >> jon >> doc;

    if (jon.size() < doc.size()){
        cout << "no";
    }else{
        cout << "go";
    }

}