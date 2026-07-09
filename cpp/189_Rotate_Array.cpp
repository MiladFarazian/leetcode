// 189. Rotate Array
// https://leetcode.com/problems/rotate-array/
// Difficulty: Medium | Language: cpp | Runtime: 0 ms | Memory: 29.7 MB

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (n == 0) return;

        k %= n;
        if (k == 0) return;
        
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};
