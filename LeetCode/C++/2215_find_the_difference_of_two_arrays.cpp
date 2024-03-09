#include <algorithm> // set_difference
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {

            // need to get distinct number first since set_difference keeps multiple instances of number
            set<int> distinct1(nums1.begin(), nums1.end());
            set<int> distinct2(nums2.begin(), nums2.end());

            // must size otherwise runtime error with NULL
            vector<int> difference1(nums1.size()), difference2(nums2.size());

            // present in first set but not second set
            auto it1 = set_difference(distinct1.begin(), distinct1.end(), distinct2.begin(), distinct2.end(), difference1.begin());
            auto it2 = set_difference(distinct2.begin(), distinct2.end(), distinct1.begin(), distinct1.end(), difference2.begin());

            // otherwise answer will contain digit 0
            difference1.resize(it1 - difference1.begin());
            difference2.resize(it2 - difference2.begin());

            return (vector<vector<int>>){difference1, difference2};

    }
};