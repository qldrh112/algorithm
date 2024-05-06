# def show_grade(arr, N, k):
#     """
#     param(arr): 학생들의 점수 리스트
#     param(N): 학생의 수 
#     param(k): 처음 받은 리스트에서 몇 번째 학생의 등급을 반환할 것인지

#     학생의 점수를 리스트로 받아, 기준에 따라 총점을 만들고,
#     인덱스를 키로 점수를 딕셔너리로 만듭니다. 
#     이후, 학생들의 점수를 내림차순으로 배열해 등급을 부여합니다.
#     학생들의 점수와 등급을 튜플로 묶습니다.
#     그리고 원하는 인덱스로 등급을 뽑아내 반환합니다.

#     {인덱스: 점수}, (점수, 등급) -> 인덱스(k)를 통해 점수를 얻어내고, 그 점수로 등급을 얻어내는 원리
#     """
    
#     gpa_list = []
#     for i in range(len(arr)):
#         gpa = sum(map(lambda x, y: x * y, arr[i], [0.35, 0.45, 0.2]))
#         gpa_list.append(gpa)

#     idx_gpa = {}
#     for i, gpa in enumerate(gpa_list):
#         idx_gpa.update({i : gpa})

#     grade_list = []
#     for i in (['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']):
#         for j in range(N//10):
#             grade_list.append(i)

#     print(grade_list)

#     sorted_gpa_list = sorted(gpa_list, reverse=True)
#     gpa_grade_list = zip(sorted_gpa_list, grade_list)

#     for tup in gpa_grade_list:
#         gpa, grade = tup
#         if gpa  == idx_gpa.get(k+1):
#             return grade
        

# T = int(input())
# for t in range(T):
#     N, k = map(int, input().split())
#     input_list = [0] * N
#     for n in range(N):
#         input_list[n] = list(map(int, input().split()))
#     print(f'#{t+1} {show_grade(input_list, N, k)}')

"""
1. 점수 변환
2. k번째 학생의 등급 출력
"""

def make_score(mid, end, homework):
    """
    mid: 중간 점수
    end: 마지막 점수
    homework: 과제 점수
    return: 성적 산출 점수
    """
    return 0.35 * mid + 0.45 * end + 0.2 * homework


def student_grade(lst):
    """
    lst: 학생들의 점수(1차원 리스트[int])
    return: K번째 학생의 등급
    """
    grade_dict = {
        0: 'A+',
        1: 'A0',
        2: 'A-',
        3: 'B+',
        4: 'B0',
        5: 'B-',
        6: 'C+',
        7: 'C0',
        8: 'C-',
        9: 'D0',
    }
    score = lst[K-1]
    # 내림차순은 reverse를 뒤집어야 함
    ranking = sorted(lst, reverse=True).index(score)
    return grade_dict.get(ranking // (N//10))

T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    # 성적 산출 점수로 변환
    scores = [0] * N
    for i in range(N):
        mid, end, homework = map(int, input().split())
        scores[i] = make_score(mid, end, homework)

    # 출력합니다.
    print(f'#{t+1} {student_grade(scores)}')