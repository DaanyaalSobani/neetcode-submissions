class Solution:
    delimeter = "#|#"
    empty = 'EMPTY'
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.empty
        return self.delimeter.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.empty:
            return []
        return s.split(self.delimeter)