class Solution {
public:

    int tribRec (int n, std::vector<int>& results){

        if (n <= 2){
            return results[n];
        }else if (results[n] != 0){
            return results[n];
        }else{
            results[n] = tribRec(n-1, results) + tribRec(n-2, results) + tribRec(n-3, results);
            return results[n];
        }

    }

    int tribonacci(int n) {
        std::vector<int> results(n+1);

        if (n <= 1){
            return n;
        }else if (n == 2){
            return 1;
        }else{
            results[0] = 0;
            results[1] = 1;
            results[2] = 1;
            return tribRec(n, results);
        }

    }

};
