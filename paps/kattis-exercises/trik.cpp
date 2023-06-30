#include <iostream>

using namespace std;

int main(){

    string moves, letter;
    cin >> moves;

    int ball = 1;
    for (int i = 0; i < moves.size(); i++){
        letter = moves[i];
        if (letter == "A"){
            if (ball == 1){
                ball = 2;
            }else if (ball == 2){
                ball = 1;
            }
        }else if (letter == "B"){
            if (ball == 2){
                ball = 3;
            }else if (ball == 3){
                ball = 2;
            }
        }else if (letter == "C"){
            if (ball == 1){
                ball = 3;
            }else if (ball == 3){
                ball = 1;
            }
        }
    }
    cout << ball;
    
}