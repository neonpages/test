# keyword_chatbot.py
# 키워드 기반 챗봇 - 간단한 규칙 기반 응답 시스템

def get_response(user_input):
    """사용자 입력에서 키워드를 찾아 응답을 반환하는 함수"""
    
    # 소문자로 변환해서 대소문자 구분 없이 비교
    text = user_input.lower()

    # 키워드 → 응답 규칙 정의
    rules = [
        # 인사
        (["안녕", "hi", "hello", "반가워", "ㅎㅇ"],
         "안녕하세요! 무엇을 도와드릴까요? 😊"),

        # 날씨
        (["날씨", "weather", "비", "맑음", "흐림"],
         "날씨 정보는 제가 실시간으로 알 수 없어요. 기상청 앱을 확인해보세요! 🌤️"),

        # 이름/정체
        (["이름", "누구", "뭐야", "who are you", "name"],
         "저는 키워드 기반 챗봇이에요! 간단한 규칙으로 동작합니다. 🤖"),

        # 도움말
        (["도움", "help", "뭐 할 수 있어", "기능"],
         "날씨, 인사, 농담, 시간 등에 대해 물어보세요!"),

        # 시간
        (["시간", "몇 시", "time"],
         "죄송해요, 저는 실시간 시간을 모르지만 핸드폰 시계를 확인해보세요! ⏰"),

        # 농담
        (["농담", "웃겨", "재미", "joke"],
         "왜 개미는 컴퓨터를 잘 할까요? 바이트(byte)를 이미 알고 있으니까요! 🐜😄"),

        # 고마움
        (["고마워", "감사", "thank", "thanks"],
         "천만에요! 도움이 됐다니 기쁘네요 😄"),

        # 작별
        (["bye", "잘 있어", "안녕히", "바이", "종료", "끝"],
         "안녕히 가세요! 또 이야기해요~ 👋"),
    ]

    # 키워드 매칭
    for keywords, response in rules:
        for keyword in keywords:
            if keyword in text:
                return response

    # 아무 키워드도 매칭되지 않은 경우
    return "음... 잘 모르겠어요. 다르게 질문해볼 수 있을까요? 🤔"


def main():
    print("=" * 40)
    print("   🤖 키워드 기반 챗봇에 오신 걸 환영합니다!")
    print("   종료하려면 '종료' 또는 'bye'를 입력하세요.")
    print("=" * 40)

    while True:
        user_input = input("\n나: ").strip()

        if not user_input:
            print("챗봇: 입력이 없어요. 뭔가 물어봐주세요!")
            continue

        response = get_response(user_input)
        print(f"챗봇: {response}")

        # 종료 조건
        if any(word in user_input.lower() for word in ["bye", "잘 있어", "안녕히", "바이", "종료", "끝"]):
            break


if __name__ == "__main__":
    main()
