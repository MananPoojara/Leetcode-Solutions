class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word)) # "eat" -> "aet" soted() creat list so we have to join it 

            # res["aet"] -> "eat","tea","ate"
            #when next word come like tea in strs 1 -> sort (aet) now we have aet key so it just append "tea"
            res[sorted_word].append(word) 
        
        return list(res.values())


        