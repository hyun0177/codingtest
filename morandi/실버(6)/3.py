# 출력 형식이 잘못되었습니다. // 정규표현식 더 자세히 보기

import re

def clean_and_compare_strings(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    s1 = re.sub(r'[\[\{]', '(', s1)
    s2 = re.sub(r'[\[\{]', '(', s2)

    s1 = re.sub(r'[\]\}]', ')', s1)
    s2 = re.sub(r'[\]\}]', ')', s2)

    s1 = re.sub(r';', ',', s1)
    s2 = re.sub(r';', ',', s2)

    s1 = re.sub(r'[\s\t]+', ' ', s1)
    s2 = re.sub(r'[\s\t]+', ' ', s2)

    s1 = re.sub(r'\s?\(\s?', '(', s1)
    s2 = re.sub(r'\s?\(\s?', '(', s2)

    s1 = re.sub(r'\s?\)\s?', ')', s1)
    s2 = re.sub(r'\s?\)\s?', ')', s2)

    s1 = re.sub(r'\s?\.\s?', '.', s1)
    s2 = re.sub(r'\s?\.\s?', '.', s2)

    s1 = re.sub(r'\s?\,\s?', ',', s1)
    s2 = re.sub(r'\s?\,\s?', ',', s2)

    s1 = re.sub(r'\s?\:\s?', ':', s1)
    s2 = re.sub(r'\s?\:\s?', ':', s2)

    return s1 == s2

def main():
    N = int(input())
    for k in range(1, N + 1):
        s1 = input().strip()
        s2 = input().strip()

        result = "equal" if clean_and_compare_strings(s1, s2) else "not equal"
        print(f"Data Set {k}: {result}\n")

if __name__ == "__main__":
    main()