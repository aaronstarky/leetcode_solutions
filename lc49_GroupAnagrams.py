'''
First solution

runtime: O(n^2m) with n as the number of words and m being the length of the longest word
space: O(nm) with n being the number of words and m being the length of the longest word
'''
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

'''
Second solution that uses sorting like I wanted to originally

run: O(n^2 log n)
space: O(nm)
'''    
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = {}
        for i in range(len(strs)):
            srtd = "".join(sorted(strs[i]))
            if srtd not in words:
                words[srtd] = []
            words[srtd].append(strs[i])
        result = []
        for key in words:
            result.append(words[key])
        return result
    
    
'''
this is a random solution that was minimizing space
'''
class Solution(object):
    def anagram(self,a,b):
        m1 = {}
        m2 = {}
        for i in range(len(a)):
            m1[a[i]]=m1.get(a[i],0)+1
            m2[b[i]]=m2.get(b[i],0)+1
        return m1==m2
    def groupAnagrams(self, strs):
        ana=[[strs[0]]]
        for i in range(1,len(strs)):
            for w in range(len(ana)):
                if (len(strs[i])==len(ana[w][0])) and (set(strs[i])==set(ana[w][0])):
                    if self.anagram(strs[i],ana[w][0]):
                        #print(strs[i],ana[w])
                        temp=ana[w]
                        temp.append(strs[i])
                        ana[w]=temp
                        break
            else:
                ana.append([strs[i]])
        return ana