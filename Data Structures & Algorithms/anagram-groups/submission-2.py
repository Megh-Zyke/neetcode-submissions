class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collections = {}
        for s in strs:
            code = [0] * 26
            for word in s:
                code[ord(word) - ord("a")] += 1
            key = "#".join(str(x) for x in code)
            if key not in collections:
                collections[key] = []
            collections[key].append(s)

        return list(collections.values())