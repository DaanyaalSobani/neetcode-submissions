class Solution:
    encoded = []
    def encode(self, strs: List[str]) -> str:
        self.encoded = strs
        return ""

    def decode(self, s: str) -> List[str]:
        return self.encoded