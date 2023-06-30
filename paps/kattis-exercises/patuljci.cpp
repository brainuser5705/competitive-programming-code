#include <iostream>

using namespace std;

int inputDwarves[9];

int* findDwarves(int array[], int numDwarves, int total){

    if (total == 100){
        return array;
    }else{
        for (int i = numDwarves; i < 9; i++){
            array[numDwarves] = inputDwarves[i];
            total += inputDwarves[i];
            return findDwarves(array, numDwarves + 1, total);
        }
    }
    
}

int main(){
    // using backtracking...
    for (int i = 0; i < 9; i++){
        cin >> inputDwarves[i];
    }

    int actualDwarves[7];
    findDwarves(actualDwarves, 0, 0);
    for (int i = 0; i < 7; i++){
        cout << actualDwarves[i] << endl;
    }
}