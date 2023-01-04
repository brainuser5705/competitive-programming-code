#include <iostream>
using namespace std;

bool insertIfExists(int numTrips, string arr[], string value){
    int i = 0;
    for (; i < numTrips; i++){
        if (arr[i] == value){
            return true;
        }
    }
    arr[i] = value;
    return false;
}

int main(){
    int numTests, numTrips;
    cin >> numTests;

    for (int i = 0; i < numTests; i++){
        cin >> numTrips;

        string arr[numTrips];
        string trip;

        int count = 0;

        for (int j = 0; j < numTrips; j++){
            cin >> trip;
            if (!insertIfExists(j, arr, trip)) count++;
        }

        cout << count << endl;
    }

    return 0;
}