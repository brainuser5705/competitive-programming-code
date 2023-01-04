// put all the numbers in an array
// do a double for loop to see if the sum will be 100

#include <iostream>
using namespace std;

int * identify(int nums[], int total){
    int indices[2];

    for (int i = 0; i < 8; i++){
        for (int j = i+1; j < 9; j++){
            int copy = total;
            if ((total - nums[i] - nums[j]) == 100){
                indices[0] = i;
                indices[1] = j;
                return indices;
            }
        }
    }
}

int main(){

    int dwarves[9];
    int total = 0;

    for (int i = 0; i < 9; i++){
        int num;
        cin >> num;
        dwarves[i] = num;
        total += num;
    }

    int* indices = identify(dwarves, total);

    for (int i = 0; i < 9; i++){
        if (i != *(indices + 0) && i != *(indices + 1)){
            cout << dwarves[i] << endl;
        }
    }

}