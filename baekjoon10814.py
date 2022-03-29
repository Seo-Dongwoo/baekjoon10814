N = int(input())
word = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    word.append((age, name))

word.sort(key=lambda x: x[0])

for i in word:
    print(i[0], i[1])
