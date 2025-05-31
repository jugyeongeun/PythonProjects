#각 난이도 별로 단어와 뜻을 모아둔 사전(dictionary)입니다.
#나중에 퀴즈 출제할 때 여기서 가져다 씁니다.
#각 단어는 key로, 뜻은 value로 저장되어 있습니다.

word_dict = {
    'easy': {
        'apple': '사과',
        'banana': '바나나',
        'grape': '포도',
        'orange': '오렌지',
        'peach': '복숭아',
        'pear': '배',
        'kiwi': '키위',
        'melon': '멜론',
        'mango': '망고',
        'lemon': '레몬'
    },
    'normal': {
        'strawberry': '딸기',
        'blueberry': '블루베리',
        'watermelon': '수박',
        'pineapple': '파인애플',
        'cherry': '체리',
        'coconut': '코코넛',
        'papaya': '파파야',
        'pomegranate': '석류',
        'raspberry': '라즈베리',
        'blackberry': '블랙베리'
    },
    # 추가적인 단어를 여기에 넣을 수 있습니다.
    'hard': {
        'avocado': '아보카도',
        'dragonfruit': '용과',
        'jackfruit': '잭프루트',
        'lychee': '리치',
        'passionfruit': '패션프루트',
        'tangerine': '귤',
        'clementine': '클레멘타인',
        'bloodorange': '블러드오렌지',
        'starfruit': '별과일',
        'durian': '두리안'
    }
}