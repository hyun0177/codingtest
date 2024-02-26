# PCCE기출 10번 lv1 14분 //

# 처음 풀이: 새로운 배열인 result를 만들지 않고 data 배열로만 처리 시도 -> 실패
# result 배열을 만들어서 분류 기준값으로 분류된 배열 생성 후 sort로 정렬 시도

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"


def solution(data, ext, val_ext, sort_by):
    seq = {"code":0,
           "date":1,
           "maximum":2,
           "remain":3
           }
    ext = seq[ext]
    sort_by = seq[sort_by]

    result = [ d for d in data if d[ext] < val_ext ]
    result.sort(key=lambda x: x[sort_by])

    return result

print(solution(data, ext, val_ext, sort_by))