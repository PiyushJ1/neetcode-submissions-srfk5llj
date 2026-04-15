class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        kv = defaultdict(list)

        for s in strs:
            k = "".join(sorted(s))
            kv[k].append(s)
        
        return list(kv.values())