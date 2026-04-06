import matplotlib.pyplot as plt

subjects = ['Pyhon', 'Math', 'English', 'AI']
scores_class1 = [85, 90, 78, 92]
scores_class2 = [80, 88, 82, 85]

average_score = (sum(scores_class1) + sum(scores_class2)) / (len(scores_class1) + len(scores_class2))
# 클래스 1 막대 
plt.bar(subjects, scores_class1, color='skyblue', alpha=10, label='Class1')
# 클레스 2 막대 (약간 오른쪽으로 이동)
plt.bar([s for s in range(len(subjects))], scores_class2, color='orange', alpha=0.6, label='Class2')
# 클래스 1 선 그래프
plt.plot(subjects, scores_class1, color='blue', marker='o', linewidth=2)
# 클래스 2 선 그래프
plt.plot(subjects, scores_class2, color='red', marker='x', linewidth=2)
#평균선 
plt.axhline(y=average_score, color='green', linestyle='--', linewidth=3, label='Overall Avg')

#제목, 축 
plt.title('Scores Comparison')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.legend()

plt.show()
