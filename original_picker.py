import random


# 처음 입력받는 함수
def get_settings():
    num1 = int(input("모든 사람 수 입력 (명 제외): "))
    num2 = int(input("발표자 수 입력 (명 제외): "))
    num3 = input("제외할 번호 입력 (공백 또는 쉼표로 구분): ")

    # 제외할 번호 처리
    exclude_number = set(map(int, num3.replace(',', ' ').split()))

    # 전체 사람 번호
    total_numbers = set(range(1, num1 + 1))

    # 제외 번호 제거
    allowed_numbers = list(total_numbers - exclude_number)

    return num1, num2, allowed_numbers


# 발표자 뽑기 함수
def select_speakers(num2, allowed_numbers):
    if len(allowed_numbers) >= num2:
        selected_speakers = random.sample(allowed_numbers, num2)

        # 보기 좋게 정렬해서 출력
        print(f"\n🎉 당첨된 발표자 번호: {sorted(selected_speakers)}")

    else:
        print(
            f"\n❌ 에러: 남은 사람 수({len(allowed_numbers)}명)가 "
            f"발표자 수({num2}명)보다 적어서 뽑을 수 없습니다."
        )


# 처음 설정
num1, num2, allowed_numbers = get_settings()


# 게임 시작
game = True

while game:

    # 발표자 뽑기
    select_speakers(num2, allowed_numbers)

    while True:

        selection = int(input(
            "\n다시 뽑을까요? (1: 다시 뽑기 / 2: 초기화): "
        ))

        # 1을 입력하면 같은 조건으로 다시 뽑기
        if selection == 1:
            break

        # 2를 입력하면 처음부터 다시 입력
        elif selection == 2:
            num1, num2, allowed_numbers = get_settings()
            break

        # 3 이상 또는 0 이하를 입력하면 에러
        else:
            print("\n❌ 에러: 1 또는 2만 입력해주세요.")

