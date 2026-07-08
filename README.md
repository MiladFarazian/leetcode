# LeetCode Solutions

This repository contains my solutions to various LeetCode problems. Each solution is written in Python.

## Index

| # | Problem | Difficulty | Topic | Solution |
|---|---------|------------|-------|----------|
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | Math, String Manipulation | [72_Reverse_Integer.py](72_Reverse_Integer.py) |
| 1404 | [Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/) | Medium | Bit Manipulation, Simulation | [1401_Num_of_Steps_Reduce_Bin_Num.py](1401_Num_of_Steps_Reduce_Bin_Num.py) |

---

## 7. Reverse Integer

**File:** [`72_Reverse_Integer.py`](72_Reverse_Integer.py) · **Difficulty:** Medium

### Problem
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing causes the value to go outside the signed 32-bit range `[-2^31, 2^31 - 1]`, return `0`.

### Approach
String-based reversal:
1. Convert the integer to a string.
2. If the number is negative, keep the leading `-` and strip it from the digits before reversing.
3. Build the reversed string by walking the digits back to front.
4. Convert back to an integer and check it against the 32-bit bounds (`-2^31` to `2^31 - 1`); return `0` on overflow.

### Complexity
- **Time:** O(d), where d is the number of digits in `x`.
- **Space:** O(d) for the string copies.

### Notes
- The overflow check happens *after* the reversal, which works in Python because its integers don't overflow — in a fixed-width language you'd need to check before each append.

---

## 1404. Number of Steps to Reduce a Number in Binary Representation to One

**File:** [`1401_Num_of_Steps_Reduce_Bin_Num.py`](1401_Num_of_Steps_Reduce_Bin_Num.py) · **Difficulty:** Medium · Solved as the daily question on 2024-05-29

### Problem
Given the binary representation of an integer as a string `s`, return the number of steps to reduce it to `1` under these rules:
- If the number is **even**, divide it by 2.
- If the number is **odd**, add 1 to it.

### Approach
Convert-then-simulate:
1. Parse the binary string into an integer manually — walk the string from the least-significant bit and add `2^i` for every `'1'`.
2. Simulate the process directly on the integer: while it isn't `1`, add 1 if odd or halve if even, counting each step.

### Complexity
- **Time:** O(n), where n is the length of the binary string — parsing is one pass, and the value shrinks by roughly one bit every one or two steps.
- **Space:** O(1) beyond the parsed integer.

### Notes
- An alternative O(n) approach works on the string directly with a carry bit (no integer conversion), which avoids big-integer arithmetic for very long inputs.
