class Solution:
    def minWindow(self, s: str, t: str) -> str:
        requiredLetters = {}
        window = {}
        for i in t:
            requiredLetters[i] = 1 + requiredLetters.get(i,0)
        need = len(requiredLetters.values())
        have = 0
        minWin = []
        res = [0] * 100000
        l = 0
        for r in range(len(s)):
            minWin.append(s[r])
            if s[r] in requiredLetters:
                if s[r] not in window and s[r] in requiredLetters:
                    window[s[r]] = 1
                    if window[s[r]] == requiredLetters[s[r]]:
                        have += 1
                elif s[r] in window and s[r] in requiredLetters:
                    window[s[r]] += 1
                    if window[s[r]] == requiredLetters[s[r]]:
                        have += 1
            while have == need:
                if len(minWin) < len(res):
                    res = ''.join(minWin)
                minWin.pop(0)
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < requiredLetters[s[l]]:
                        have -= 1
                l += 1
        if len(res) == 100000:
            return ''
        return res
