var = "1. 데이터의 중요성을 알며, 데이터 사이언스가 무엇인지 이해하여 데이터 분석에 필요한 기초 통계 지식을 알 수 있다\
2. 데이터 프레임을 만들고, 시각화를 하기 위한 패키지를 알며, 목적(Datafrmae 및 시각화)에 맞는 패키지를 활용하여 직접 실습을 진행해볼 수 있다.\
3. 인터넷 사용중 필요한 데이터를 코딩을 통하여 빠르고 쉽게 수집할 수 있다.\
4. 예측 모델 개발을 위한 기본적인 프로세스를 익히고 다양한 머신러닝 기법 소개와 동시에 Sckit-learn 패키지를 활용한 실데이터 기반 매출 예측 모델을 제작할 수 있다."

space_ps = var.replace(".","").replace(",","").split(" ")

char_frequency = {}

for char in space_ps:
    char_frequency.setdefault(char,0)
    char_frequency[char] += 1

print(char_frequency)
