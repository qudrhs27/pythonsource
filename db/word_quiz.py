# csv 파일의 내용을 테이블에 insert 하기(단, 테이블이 비어 있는 경우만 삽입)

# 테이블의 내용을 읽어서 무작위로 추출 후 문제 내기
# Question #1 : 'apple'의 뜻은?
# 1. 버스
# 2. 남편
# 3. 수줍은
# 4. 사과

# 테이블의 내용을 읽어서 섞은 후 문제 내기
# apple => 사과

# 결과 : 3 / 5 정답

# 결과를 테이블에 저장하기
# total,corect,regdate
import oracledb
from datetime import datetime

conn = oracledb.connect(user="python_user",password="54321",dsn="localhost/xe")
cursor = conn.cursor()

def load_words_from_csv():
    '''csv 파일을 읽어서 튜플 리스트로 반환'''

    # [(wife,아내),(apple,사과)]


def seed_words_if_empty():
    '''words 테이블이 비어 있으면 csv 파일 내용을 읽어서 넣기'''
    # insert


def run_quiz():
    '''
    1) all_words = words 테이블 읽기
    2) 무작위 문제 추출 random.sample()
    3) all_words 문제를 제외한 내용을 섞은 후 거기서 틀린 meaning 추출
    4) 답변입력반은 후 정답 맞는지 확인
    5) 최종 결과 입력
    '''


if __name__ == "__main__":
    try:
        seed_words_if_empty()
        run_quiz()
    finally:
        cursor.close()
        conn.close()
