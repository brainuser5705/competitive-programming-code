#include <iostream>
using namespace std;

int main(){

    int numTests, numCities, count;
    string city;
    cin >> numTests;

    for (int i = 0; i < numTests; i++){

        count = 0;
        cin >> numCities;
        string cities[numCities];

        // for each city in the test case
        for (int j = 0; j < numCities; j++){

            cin >> city;

            // search visited cities array up to the number of cities visited so far
            int k = 0;
            for (; k < j; k++){
                // if city is already visited
                if (cities[k] == city){
                    break;
                }
            }
            // check if the entire array was searched, if so then it is a new city
            if (k == j){
                cities[j] = city;
                count += 1;
            }
        }

        cout << count << endl;
    }

}