s = "dvdf"

seen = {}
start = 0
lens = 0

for i in range(len(s)):
    if s[i] in seen and start <= seen[s[i]]:
        start = seen[s[i]]+1
    else:
        if lens <= len(s[start:i])+1:
            lens = len(s[start:i])+1
    seen[s[i]] = i

print(lens)
        
