class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string using the Length-Prefix pattern.
        
        Format: <length>#<string_content>
        Example: ["neet","code"] -> "4#neet4#code"
        
        Time Complexity: O(N) where N is the total number of characters across all strings.
        Space Complexity: O(N) for the output string builder.
        """
        # Using list comprehension and join() to avoid O(N^2) memory reallocation bottleneck
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back to a list of original strings.
        
        Time Complexity: O(N) linear scan through the encoded string.
        Space Complexity: O(N) to store the reconstructed list of strings.
        """
        res: List[str] = []
        i = 0
        n = len(s)

        while i < n:
            # 1. Find the delimiter '#' to parse the length of the upcoming string
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length number (handles multi-digit lengths like "125#...")
            length = int(s[i:j])
            
            # 2. Shift pointer to the start of the actual string content
            start_idx = j + 1
            end_idx = start_idx + length
            
            # Slice the exact chunk based on the pre-parsed length
            res.append(s[start_idx:end_idx])
            
            # 3. Move the main pointer to the start of the next length prefix
            i = end_idx

        return res