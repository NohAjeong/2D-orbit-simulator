import numpy as np

#학생 점수 예제
math_list =[ 85, 90, 78, 92, 88 ]
math_array = np.array(math_list) #배열은 연산이 곧바로 가

print("math_array:", math_array)
print("타입:", type(math_array))
      
english_array = np.array([80, 85, 88, 75, 90])

#더하기
total_scores = math_array + english_array
print("총점:", total_scores)

#빼기
diff_scores = math_array - english_array
print("점수 차이:", diff_scores)

#곱하기
prod_scores = math_array * 2
print("2배 점수:", prod_scores)

#모든 학생 점수 +5점
bonus = math_array + 5
print("보너스 점수:", bonus)

#10프로 증가
increase = math_array * 1.1
print("10%증가:", increase)

#수학 평균 점수
average_scores = math.array.mean()
print("수학평균:", average_scores)

#최고점 & 최저점
print("최고점:", math_array.max())
print("최저점:", math_array.min())
