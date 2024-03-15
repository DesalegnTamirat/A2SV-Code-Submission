class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def extract_revisions(version):
            revisions = version.split(".")
            return [int(revision) for revision in revisions]
        
        revisions1 = extract_revisions(version1)
        revisions2 = extract_revisions(version2)
        n, m = len(revisions1), len(revisions2)

        for i in range(max(n, m)):
            if i >= n:
                one = 0
            else:
                one = revisions1[i]
            
            if i >= m:
                two = 0
            else:
                two = revisions2[i]
            
            if one < two:
                return -1
            elif one > two:
                return 1
        
        return 0