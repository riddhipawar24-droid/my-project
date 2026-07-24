num = int(input("Enter a number: "))
seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    s = 0

    while num > 0:
        digit = num % 10
        s += digit ** 2
        num = num // 10

    num = s

if num == 1:
    print("Happy Number")
else:
    print("Sad Number")