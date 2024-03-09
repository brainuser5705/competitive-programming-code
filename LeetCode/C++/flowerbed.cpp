class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        
        int size = flowerbed.size();

        int i = 0;
        int count = 0;

        while (i < size){

            if (flowerbed[i] == 0){
                
                if ( ((i-1) >= 0 && flowerbed[i-1] == 1) || 
                    ((i+1) < size && flowerbed[i+1] == 1)){

                    i++;
                    continue;
                }

                count++;
                i += 2; // assume flower will be planted in this spot
                        // so there should be no adjacent flower

                continue;
            }

            i++; // if flower == 1

        }

        return count >= n;

    }
};
