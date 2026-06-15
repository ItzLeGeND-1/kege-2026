from re import finditer
with open(r'24_22356.txt') as file:
    data=file.readline()

pattern=r'([1-9AB][0-9AB]*[13579B])'

matches=[match.group()for match in finditer(pattern,data)]
print(max(matches,key=lambda x: int(x,12)))
print(data.index('9BB200831629754013654089270916572830406015947823017328604590726108439503251640897095740682310273940168500024B'))


