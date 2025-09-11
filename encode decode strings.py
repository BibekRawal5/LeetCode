class Solution:

    def encode(self, strs: List[str]) -> str:
        newchar = '!'
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + newchar + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        newchar = '!'
        decoded_strs = []
        cur = 0
        while cur < len(s):
            i = cur
            while s[i] != '!':
                i += 1
            l = int(s[cur:i])
            i += 1
            cur = i + l
            decoded_strs.append(s[i: cur])

        return decoded_strs
