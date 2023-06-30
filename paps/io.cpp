#include <iostream>

using namespace std;

int main(){

    // pressing enter allows the program to read

    // program only reads text until the first whitespace
    // the next cin will continue reading from the whitespace\

    string name;
    cout << "What's your first name?" << endl;
    cin >> name;

    int age;
    cout << "How old are you?" << endl;
    // gets read as a string (stores as 0)
    cin >> age; 

    cout << "Hi, " << name << "!" << endl;
    cout << "You are " << age << " years old." << endl;

    // to read the entire line, use getline
    // does not work if there was cin before
    string line;
    cout << "Type some text, and press enter: " << endl;
    getline(cin, line);
    cout << "You typed: " << line << endl;

}


