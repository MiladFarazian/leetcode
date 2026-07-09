# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
# Difficulty: Hard | Language: python3 | Runtime: 3 ms | Memory: 19.5 MB

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        # 1–19: the irregulars. Index = the number itself (index 0 is a placeholder).
        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        # Tens: index = tens digit, so tens[2] = "Twenty", tens[9] = "Ninety".
        # Indices 0 and 1 are placeholders — numbers under 20 use the table above.
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        # Scale words: index = which 3-digit chunk you're on, counting from the right.
        # Chunk 0 gets no label, chunk 1 is Thousand, etc.
        scales = ["", "Thousand", "Million", "Billion"]

        def helper(n):
                # converts 1-999 to a list of words
                words = []
                if n >= 100:
                    words.append(below_20[n // 100])
                    words.append("Hundred")
                    n %= 100
                if n >= 20:
                    words.append(tens[n // 10])
                    n %= 10
                if n >= 1:
                    words.append(below_20[n])
                return words

        parts = []
        chunk_index = 0                      # 0 = ones, 1 = thousands, 2 = millions...
        while num > 0:
            chunk = num % 1000               # peel off the rightmost 3 digits
            if chunk != 0:
                piece = helper(chunk)
                if scales[chunk_index]:
                    piece.append(scales[chunk_index])
                parts.append(piece)
            num //= 1000                     # chop those 3 digits off
            chunk_index += 1

        parts.reverse()                      # we built right-to-left; English reads left-to-right
        return ' '.join(word for piece in parts for word in piece)
