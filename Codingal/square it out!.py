start = int(input())
end = int(input())

odd = []
even = []

for i in range(start, end + 1):
    sq = i * i
    if sq % 2 == 0:
        even.append(sq)
    else:
        odd.append(sq)

print(odd)
print(even)