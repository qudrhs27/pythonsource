# 영어타자 프로그램

# word.txt 읽어서
# 섞는다 random.shuffle()
# 임의로 하나 추출 random.choice()

# Q1)then
# input()
# input 결과에 따라 정답!! or 오타!!

# start = time.time()
# 문제 5문제 출제
# 정답 개수
# end = time.time()

# 게임시간 출력
# 출력문 => 게임시간 : 10초, 정답개수 : 3개
# 3개 이상 정답인 경우 합격 or 불합격

import random, time

with open("./ch1/data/word.txt", "r", encoding="utf-8") as f:
    words = f.readlines()

start = time.time()
problem_cnt = 0
correct_cnt = 0
while True:
    problem_cnt += 1
    random.shuffle(words)
    word = random.choice(words).strip()
    print(f"Q{problem_cnt}")
    print(word)
    answer = input("정답을 입력하세요 : ").strip()

    if word == answer:
        print("정답!!")
        print()
        correct_cnt += 1
    else:
        print("오답!!")
        print()

    if problem_cnt == 5:
        break

end = time.time()
et = end - start
et = format(et, ".3f")
print(f"게임시간 : {et}초, 정답개수 : {correct_cnt}개")
if correct_cnt >= 3:
    print("합격")
else:
    print("불합격")
    
    





