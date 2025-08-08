class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        self.dicts = [None for i in range(len(strs))]
        groups = []
        covered = [0 for i in range(len(strs))]
        for i in range(len(strs)):
            if covered[i] == 1: continue
            covered[i] = 1
            w1_cc = self.dictify(strs[i], i)
            anagrams = [strs[i]]
            for j in range(len(strs)):
                if covered[j] == 1 or i == j or len(strs[i]) != len(strs[j]):
                    continue
                w2_cc = self.dictify(strs[j], j)
                failed = False
                for key in w2_cc:
                    if w1_cc.get(key) != w2_cc.get(key):
                        failed = True
                        break
                if failed:
                    continue
                else:
                    covered[j] = 1
                    anagrams.append(strs[j])
            groups.append(anagrams)
        return groups
            
    def dictify(self, w, i):
        if self.dicts[i] is not None:
            return self.dicts[i]
        d = {}
        for c in w:
            if not d.get(c):
                d[c] = 0
            d[c] += 1
        self.dicts[i] = d
        return d
        