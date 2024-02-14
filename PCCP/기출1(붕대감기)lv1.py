# 프로그래머스 PCCP기출1 lv1 붕대 감기 // 24분

def solution(bandage, health, attacks):
    total_time = attacks[-1][0]
    hill_time = 0
    max_health = health

    for i in range(1, total_time + 1):
        if i == attacks[0][0]:
            health -= attacks[0][1]
            if health < 0:
                return -1
            attacks.pop(0)
            hill_time = 0
        else:
            health += bandage[1]
            hill_time += 1

            if hill_time == bandage[0]:
                health += bandage[2]
                hill_time = 0

            if health > max_health:
                health = max_health

    return health


b = [1, 1, 1]
h = 5
a = [[1, 2], [3, 2]]

print(solution(b, h, a))
