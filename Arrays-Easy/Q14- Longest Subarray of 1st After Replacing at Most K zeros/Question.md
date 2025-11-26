# Longest Subarray of 1s After Replacing at Most K Zeros

This is LeetCode #1004 — asked in Amazon, Meta, Google.

## 📌 Problem Statement

Given a binary array (only 0s and 1s), you can replace at most k zeros with 1s.
Find the length of the longest subarray that contains all 1s after at most k replacements.

### 🧩 Example 1
arr = [1,1,1,0,0,1,1,0,1,1]
k = 2
Output: 6


Explanation:

Replacing two zeros (positions 3 and 4):

[1,1,1,1,1,1]


Length = 6

### 🧩 Example 2
arr = [0,0,1,1,0,1,0]
k = 1
Output: 3


Explanation:

Window [1,1,0] (replace last zero)