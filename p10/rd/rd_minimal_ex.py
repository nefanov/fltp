# Example (Python): for strings a^nb^n, n>=0: S->aSb|eps

def RD(w):
    def S(w):
        if len(w)==0:
            return (True,w)
        if (w.startswith("a")):
            res = S(w[1:-1])
            if res[0] and w.endswith('b'):
                return (True, res[1][1:])
            else:
                return (False, res[1])
        else:
            return (False, w)

    return S(w) # starting from production with S in the left side
        
if __name__=="__main__":  
    print(RD("aaabb")[0])
    print(RD("aaaaabbbbb")[0])
    print(RD("")[0])
    print(RD("abab")[0])
