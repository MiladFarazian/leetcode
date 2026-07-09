// 136. Single Number
// https://leetcode.com/problems/single-number/
// Difficulty: Easy | Language: java | Runtime: 248 ms | Memory: 40.2 MB

class Solution {
    public int singleNumber(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) { 
            int j; 
            for (j = 0; j < n; j++) 
                if (i != j && nums[i] == nums[j]) 
                    break; 
            if (j == n) 
                return nums[i]; 
        }
        return -1;
    }
}
