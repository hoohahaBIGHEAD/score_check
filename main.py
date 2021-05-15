성적 = {1111:("이철수",100,100,100,100),2222:("박은경",90,90,90,90),
      3333:("김순희",80,80,80,80),4444:("최영희",70,70,70,70),5555:("이별엽",60,60,60,60)}

avg = []
total_avg = 0

for key, value in 성적.items():
    name,국어,수학,영어,과학 = value
    total = 국어 + 수학 + 영어 + 과학
    avg.append(total / 4)

for i in avg:
    total_avg += i
total_avg /= len(avg)

max_score = max(avg)
min_score = min(avg)

학번 = int(input("학번을 입력하세요 :"))

name,국어,수학,영어,과학 = 성적[학번]
total = 국어 + 수학 + 영어 + 과학

print("이름 :",name,"총점 :",total,"평균 :",total/4)
print("==========================================")
print("전체평균 :",total_avg)
print("최대값 :",max_score)
print("최소값 :",min_score)