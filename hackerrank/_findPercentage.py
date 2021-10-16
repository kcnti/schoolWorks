n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = list(map(float, scores))
    student_marks[name] = scores
query_name = input()
query_scores = student_marks[query_name]

#print(sum(query_scores))
#print(len(list(query_scores)))

print("%.2f"%(sum(query_scores)/len(query_scores)))