class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def do_split(v, n):
            cnt = Counter(v)
            o, c = cnt['('], cnt[')']
            if c == o == n:
                res.append(v)
            
            if o <= n:
                if c < o:
                    do_split(v+'(', n), do_split(v+')', n)
                else:
                    do_split(v+'(', n)
        do_split('', n)
        return res