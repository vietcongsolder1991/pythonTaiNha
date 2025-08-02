numbers = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
total = 0
ToNhat = -1000000000000
for number in numbers:
    if max(number)>ToNhat:
        ToNhat=max(number)
    for i in number:
        total = total +i
print(total)
print(ToNhat)
