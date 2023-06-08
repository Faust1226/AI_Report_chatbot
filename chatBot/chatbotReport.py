#레벤슈타인 패키지 설치 터미널에 pip install python-Levenshtein

#필요한 라이브러이 임포트
import pandas as pd
import numpy as np
from Levenshtein import distance  # 레벤슈타인 거리를 계산할 수 있는 함수


# 챗봇 클래스
class SimpleChatBot:
    # 데이터를 불러와 질문-답변을 저장
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    # CSV파일을 Pandas 데이터 프레임으로 로드하고 각각의 열을 리스트로 변환하여 반환
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    # 레벤슈타인 거리 계산
    def find_best_answer(self, input_text):
        levenshtein_distance = [distance(input_text, question) for question in self.questions]
        # 가장 적합한 답변의 인덱스 찾기
        best_matching_index = np.argmin(levenshtein_distance)
        # 적합한 인덱스의 답변 반환
        return self.answers[best_matching_index]



    # CSV 파일 경로
filepath = 'ChatbotData.csv'
    # 챗봇 객체 생성
chatbot = SimpleChatBot(filepath)

    # 채팅 루프 시작
print("대화를 시작합니다(종료를 원하시면 '종료'를 입력하세요)")

while True:
    #입력 부분
    input_sentence = input("You: ")

    # 종료
    if input_sentence.lower() == "종료":
            break

    # 레벤슈타인 거리 기반 적절한 답변 검색
    response = chatbot.find_best_answer(input_sentence) # 이 부분이 잘못되어 있었습니다.

        # 답변 출력
    print("Chatbot: " + response)


