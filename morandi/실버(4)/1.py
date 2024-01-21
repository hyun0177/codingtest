answer = []
while True:
    n = int(input())
    if n == 0:
        break

    student = []
    for _ in range(n):
        student.append(input())

    stack = []
    for i in range(2 * n - 1):
        a, b = input().split()
        if a in stack:
            stack.remove(a)
        else:
            stack.append(a)

    answer.append(student[int(stack[0]) - 1])

for idx, i in enumerate(answer):
    print(idx+1, i)