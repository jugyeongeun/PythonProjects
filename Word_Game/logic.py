import random # 단어를 랜덤으로 선택하기 위해 random 모듈을 import 합니다.
from word_data import word_dict # 단어 사전을 가져옵니다.

# 오답 리스트를 저장하는 공간(틀린 단어 기록용)
wrong_list = [] # 틀린 단어를 저장할 리스트입니다.

# 문제를 출제하는 함수입니다.
def get_question(level):
    return random.choice(word_dict[level]) # 주어진 난이도에 맞는 단어를 랜덤으로 선택합니다.

#정답확인하는 함수
def check_answer(correct, user_input):
    is_correct = correct == user_input # 사용자가 입력한 답과 정답을 비교합니다.

    if not is_correct: # 정답이 아닐 경우
        wrong_list.append(correct, user_input) # 틀린 단어를 wrong_list에 추가합니다.

    return is_correct # 정답 여부를 반환합니다.