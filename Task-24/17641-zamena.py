from re import *
with open(r'.\files\24_17641.txt') as data:
       data=data.readline()

num=r'([1-9][0-9]*|0)'
pattern=rf'({num}[+*])+{num}'

matches=[match.group()for match in finditer(pattern,data)]
ans=0
for match in matches:
    len_match=len(match)
    if eval(match)==0:
        ans=max(ans,len(match))
    else:
        for l in range(len_match):
            if match[l]in'*+':continue
            if match[l]=='0' and match[l+1]
            for r in range(len_match-1,l,-1):
                if match[r] in '*+': continue
                new_match=match[l:r+1].lstrip('+*')
                if eval(new_match)==0:
                    ans=max(ans,len(new_match))
print(ans)