// 136. Single Number
// https://leetcode.com/problems/single-number/
// Difficulty: Easy | Language: cpp | Runtime: 0 ms | Memory: 20.7 MB

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0; 
        for (int i = 0; i < nums.size(); i++){
            result ^= nums[i];
        }
        return result;
    }
};
