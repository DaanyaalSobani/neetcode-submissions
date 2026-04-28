class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(w)}#{w}" for w in strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        i = 0
        current_length = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            print(f"j:{j}, i:{i},s[i]:{s[i]},s[j]:{s[j]},s[i:j]={s[i:j]}")
            current_length = int(s[i:j])
            result.append(s[j+1:j+1+current_length])
            i = j+1+current_length
        return result
            
            