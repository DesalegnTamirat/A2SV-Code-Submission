class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int length = 0;
        for (int num: nums) {
            length++;
        }

        int count = 0;
        for(int i = 0; i < length; i++) {
            for(int j = i + 1; j < length; j++) {
                if(nums[i] == nums[j]) {
                    count++;
                }
            }
        }
        return count;
        }
    };