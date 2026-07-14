# LeetCode Mastery Curriculum

A pattern-based curriculum for going from "I can follow solutions" to "I recognize the shape and solve it myself."
Built July 2026, starting from ~35 solved problems (mostly Easy arrays/strings/math).

---

## The Core Philosophy

**LeetCode is not 3000 problems. It's ~15 patterns wearing 3000 costumes.**

Interview-level skill = recognizing which pattern a problem is + fluently executing that pattern.
Neither comes from randomly grinding. Both come from studying **one pattern at a time until it's reflex**, then moving on.

---

## The Study Protocol (follow this for EVERY problem)

1. **Attempt honestly for 25–30 min.** Always write at least the brute force. Say the approach out loud before coding.
2. **Stuck? Read the solution guilt-free** — but *actively*: trace it on paper with a real example before moving on.
3. **File the pattern.** Say it explicitly: *"longest substring with a condition → sliding window."* Write one sentence in the solution file's comment about which pattern it is and what the trigger was.
4. **Re-solve from blank** — 2 days later, then 2 weeks later. A problem isn't "done" until it comes out of your own fingers cold. Keep a re-solve queue (see bottom).
5. **One problem done deeply beats five done shallowly.** Never binge. 1–2 problems/day, ~5 days/week is the sweet spot.

**The magic question when stuck:** write the brute force, then ask *"what work am I repeating, and what could I remember to skip it?"* That question derives most optimal solutions.

---

## Pattern Recognition Cheat Sheet (the "shelf")

| When you see... | Think... |
|---|---|
| Longest/shortest/count of **contiguous** subarray/substring with a condition | Sliding window |
| Pair/triplet in a **sorted** array; comparing from both ends | Two pointers |
| "Have I seen this before?" / counting / grouping | Hash map |
| Running totals, "sum of subarray between i and j" | Prefix sum |
| Sorted data, "find the smallest/largest X such that..." / minimize a maximum | Binary search (maybe on the answer) |
| Nested structure, matching pairs, "most recent thing" | Stack |
| Top K / Kth largest / "streaming" min/max | Heap |
| Tree problems, "for each node combine children's answers" | DFS recursion |
| Level-by-level, shortest path in unweighted graph | BFS |
| Connectivity, "number of islands/components" | DFS/BFS flood fill or Union-Find |
| Ordering with prerequisites/dependencies | Topological sort |
| "All possible combinations/permutations/subsets" | Backtracking |
| Count the ways / min cost to reach the end / "can it be done" with choices at each step | Dynamic programming |
| Overlapping ranges, meetings, merging | Intervals (sort by start!) |
| Optimize by always taking the best available piece | Greedy (must justify why it's safe) |

---

## Phase 0 — Foundations (Week 1, alongside Phase 1)

Not problems — the underlying fluency. Skim, don't marathon.

- [ ] **Big-O for real**: be able to state the complexity of every solution you write. Know why dict/set lookup is O(1), why string concatenation in a loop is O(n²), why sorting is O(n log n).
- [ ] **Python tools of the trade** (learn by using them in Phase 1, not by reading docs):
  - `enumerate`, `zip`, `sorted(key=...)`, slicing, `''.join(list)`
  - `collections.Counter`, `collections.defaultdict`, `collections.deque`
  - `heapq` (min-heap; negate values for max-heap)
  - List comprehensions; `set` operations
- [ ] **Recursion warm-up**: write factorial, fibonacci, reverse-a-string recursively. You must be comfortable with "the function calls itself and I trust it" before trees (Phase 3).

Resource for theory when a concept feels shaky: *NeetCode's videos* (pattern-focused) or *Grokking-style pattern write-ups*. Videos explain a pattern once; the reps below make it yours.

---

## Phase 1 — Arrays, Hashing, Two Pointers, Sliding Window (Weeks 1–3)

You have a head start here. Goal: turn familiarity into pattern fluency.

### Hashing
- [x] 1. Two Sum *(solved — re-solve cold as a warm-up)*
- [x] 217. Contains Duplicate *(solved 2026-07-10 — clean first try, early return included)*
- [x] 242. Valid Anagram *(solved 2026-07-09 — first curriculum problem! Hand-rolled tally; revisit with Counter)*
- [x] 49. Group Anagrams *(solved 2026-07-10 — first Medium! Fingerprint-as-key; hints only, own code)*
- [ ] 347. Top K Frequent Elements
- [ ] 128. Longest Consecutive Sequence

### Two Pointers
- [x] 283. Move Zeroes *(solved)*
- [x] 345. Reverse Vowels *(solved)*
- [ ] 125. Valid Palindrome
- [ ] 167. Two Sum II (sorted input — see why sorted changes the tool)
- [x] 15. 3Sum *(solved — re-solve; this one is a rite of passage)*
- [ ] 11. Container With Most Water

### Sliding Window
- [ ] 3. Longest Substring Without Repeating Characters *(you studied this — now re-solve cold)*
- [ ] 121. Best Time to Buy and Sell Stock
- [ ] 643. Maximum Average Subarray I
- [ ] 424. Longest Repeating Character Replacement
- [ ] 567. Permutation in String

### Prefix Sum
- [ ] 303. Range Sum Query - Immutable
- [ ] 238. Product of Array Except Self
- [ ] 560. Subarray Sum Equals K (prefix sum + hash map — beautiful combo)

**Phase exit test:** open 424 or 560 cold and solve it in under 35 min. If not, do 2 more problems from that pattern before moving on.

---

## Phase 2 — Stack, Linked List, Binary Search (Weeks 4–5)

### Stack
- [x] 20. Valid Parentheses *(solved)*
- [ ] 155. Min Stack
- [ ] 739. Daily Temperatures (monotonic stack — a new sub-pattern, important)
- [ ] 150. Evaluate Reverse Polish Notation

### Linked List
- [x] 21. Merge Two Sorted Lists *(solved)*
- [x] 83. Remove Duplicates from Sorted List *(solved)*
- [ ] 206. Reverse Linked List (THE fundamental — re-solve until effortless)
- [ ] 141. Linked List Cycle (fast/slow pointers)
- [ ] 19. Remove Nth Node From End
- [ ] 143. Reorder List

### Binary Search
- [x] 35. Search Insert Position *(solved)*
- [x] 69. Sqrt(x) *(solved)*
- [ ] 704. Binary Search (get the template bulletproof: `lo, hi`, mid, off-by-ones)
- [ ] 74. Search a 2D Matrix
- [ ] 153. Find Minimum in Rotated Sorted Array
- [ ] 875. Koko Eating Bananas (binary search **on the answer** — mind-expanding)

**Phase exit test:** 153 and 739 cold.

---

## Phase 3 — Trees & Heaps (Weeks 6–8)

The biggest gap in your history — nothing solved here yet. Trees are where recursion clicks. Go slow; this phase pays for itself in every later phase.

### Binary Trees (DFS recursion)
- [ ] 104. Maximum Depth of Binary Tree (the "hello world" of tree recursion)
- [ ] 226. Invert Binary Tree
- [ ] 100. Same Tree
- [ ] 110. Balanced Binary Tree
- [ ] 543. Diameter of Binary Tree
- [ ] 235. Lowest Common Ancestor of a BST

### BFS / Level Order
- [ ] 102. Binary Tree Level Order Traversal
- [ ] 199. Binary Tree Right Side View

### BST Property
- [ ] 98. Validate Binary Search Tree (classic; the naive attempt fails — instructive)
- [ ] 230. Kth Smallest Element in a BST

### Heaps
- [x] 215. Kth Largest Element in an Array *(solved — redo with heapq and explain the complexity)*
- [ ] 703. Kth Largest Element in a Stream
- [ ] 973. K Closest Points to Origin
- [ ] 621. Task Scheduler

**The tree mantra:** *"Assume the recursive call already works on the children. What do I do with their answers at this node?"* Every tree problem is that sentence.

**Phase exit test:** 543 and 973 cold.

---## Phase 4 — Graphs & Backtracking (Weeks 9–11)

### Graphs
- [ ] 200. Number of Islands (THE graph starter — flood fill)
- [ ] 695. Max Area of Island
- [ ] 133. Clone Graph
- [ ] 994. Rotting Oranges (multi-source BFS)
- [ ] 207. Course Schedule (topological sort / cycle detection)
- [ ] 323. Number of Connected Components (do it twice: DFS, then Union-Find)

### Backtracking
- [ ] 78. Subsets (the template — master this one deeply)
- [ ] 46. Permutations
- [ ] 39. Combination Sum
- [ ] 79. Word Search
- [ ] 17. Letter Combinations of a Phone Number

**The backtracking mantra:** *choose → explore → un-choose.* Every backtracking problem is that loop.

**Phase exit test:** 994 and 39 cold.

---

## Phase 5 — Dynamic Programming, Greedy, Intervals (Weeks 12–15)

DP is the boss level. It is NOT magic — it's recursion + remembering answers. Always derive in this order: brute-force recursion → notice repeated subproblems → add memoization → (optionally) convert to bottom-up table.

### 1-D DP
- [ ] 70. Climbing Stairs (start here; it's fibonacci in a costume)
- [ ] 746. Min Cost Climbing Stairs
- [ ] 198. House Robber
- [ ] 213. House Robber II
- [ ] 322. Coin Change
- [ ] 300. Longest Increasing Subsequence

### 2-D / String DP
- [ ] 62. Unique Paths
- [ ] 1143. Longest Common Subsequence
- [ ] 72. Edit Distance *(you have a commit named "Add 72" — revisit and re-derive it from scratch)*

### Greedy
- [ ] 53. Maximum Subarray (Kadane's — greedy/DP hybrid)
- [ ] 55. Jump Game
- [ ] 134. Gas Station

### Intervals
- [ ] 56. Merge Intervals
- [ ] 57. Insert Interval
- [ ] 435. Non-overlapping Intervals

**Phase exit test:** 322 and 56 cold.

---

## Phase 6 — Consolidation & Interview Simulation (Weeks 16+)

- [ ] Drain the re-solve queue to empty.
- [ ] Mixed random practice: pick problems WITHOUT knowing the topic (this is the real skill — recognition without hints). NeetCode 150 or a shuffled list of everything above.
- [ ] Timed sessions: 35 min hard stop, talking out loud, no running code until you believe it's right.
- [ ] Revisit your old outlier solves (312 Burst Balloons, 15 3Sum) — they'll feel completely different now.

---

## Re-solve Queue

Add every problem you needed the solution for. Re-solve 2 days later, then 2 weeks later. Delete when it comes out cold.

| Problem | First seen | Re-solve #1 | Re-solve #2 |
|---|---|---|---|
| 3. Longest Substring Without Repeating | 2026-07-08 | 2026-07-10 (scaffolded — stuck on the check + jump; redo ~07-12) | |
| 67. Add Binary | 2026-07-08 | | |
| 12. Integer to Roman | 2026-07-09 | | |
| 273. Integer to English Words (helper fn) | 2026-07-09 | | |

---

## Session Protocol (how Claude coaches)

When Milad starts a session, Claude should drive, in this order:

1. **Check the re-solve queue first.** Anything due (2 days / 2 weeks old)? That's the warm-up — re-solves beat new problems.
2. **Recommend the next new problem** from the current phase, matched to the learning goal — don't wait to be asked. One problem, with a one-line reason ("this one teaches the monotonic stack sub-pattern").
3. **Teach in coach mode:** Milad attempts first (25–30 min); Claude gives escalating hints (pattern trigger → approach nudge → pseudocode) before ever showing code. Full solutions only when asked or after a real attempt.
4. **Close the loop:** after each solve, name the pattern out loud, update the checkbox here, and add solution-assisted problems to the re-solve queue with today's date.
   Then report back to azadi: update `../azadi/coaching/leetcode-memory.md` (refresh NOW, prepend a LOG entry) so /coach and /interview see real DSA progress, not just solve counts.
5. **Track phase exits.** When the current phase's exit-test problems pass cold, celebrate it and open the next phase.

Current phase: **Phase 1 — Arrays, Hashing, Two Pointers, Sliding Window** (+ Phase 0 foundations alongside).

---

## Rules of Engagement

1. **Patterns in order.** Don't jump to DP because it's famous. Each phase uses the previous ones.
2. **Brute force is always step one.** Never stare at a blank editor hunting for the clever answer.
3. **Trace before you run.** Walk your code on paper with a small input before executing. This builds the debugging eye.
4. **Every solution file gets a comment**: which pattern, what the trigger was, complexity.
5. **Stuck 30 min = read the solution.** Struggling past that point teaches frustration, not algorithms.
6. **Never end a session on a failure.** Finish with an easy win or a clean re-solve.
