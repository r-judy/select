import random
import sys


# 처음 입력받는 함수
def get_settings():
    print("\n" + "=" * 40)
    print("        ⚙️ 발표자 뽑기 설정")
    print("=" * 40)
    
    # 1. 모든 사람 수 입력
    while True:
        try:
            val = input("모든 사람 수 입력 (명 제외): ").strip()
            num1 = int(val)
            if num1 < 1:
                print("❌ 1명 이상 입력해주세요.")
                continue
            break
        except ValueError:
            print("❌ 숫자만 입력해주세요.")

    # 2. 발표자 수 입력
    while True:
        try:
            val = input("발표자 수 입력 (명 제외): ").strip()
            num2 = int(val)
            if num2 < 1:
                print("❌ 1명 이상 입력해주세요.")
                continue
            if num2 > num1:
                print(f"❌ 발표자 수({num2}명)는 전체 인원({num1}명)보다 많을 수 없습니다.")
                continue
            break
        except ValueError:
            print("❌ 숫자만 입력해주세요.")

    # 3. 제외할 번호 입력
    while True:
        num3 = input("제외할 번호 입력 (공백 또는 쉼표로 구분, 없으면 엔터): ").strip()
        if not num3:
            exclude_number = set()
            break
        try:
            exclude_number = set(map(int, num3.replace(',', ' ').split()))
            break
        except ValueError:
            print("❌ 제외할 번호는 숫자만 입력해주세요 (예: 3 7 또는 3, 7).")

    # 전체 사람 번호
    total_numbers = set(range(1, num1 + 1))

    # 제외 번호 제거
    allowed_numbers = list(total_numbers - exclude_number)

    print(f"\n✅ 설정 완료: 전체 {num1}명 중 {num2}명 추첨 (대상 후보: {len(allowed_numbers)}명)")
    return num1, num2, allowed_numbers


# 발표자 뽑기 함수 (뽑힌 번호가 원본 리스트에서 제거되지 않음)
def select_speakers(num2, allowed_numbers):
    if len(allowed_numbers) >= num2:
        # allowed_numbers 원본을 수정하지 않고 random.sample 실행 (다음 뽑기 때도 대상에 포함됨)
        selected_speakers = random.sample(allowed_numbers, num2)

        # 보기 좋게 정렬해서 출력
        print(f"\n🎉 당첨된 발표자 번호: {sorted(selected_speakers)}")
    else:
        print(
            f"\n❌ 에러: 남은 사람 수({len(allowed_numbers)}명)가 "
            f"발표자 수({num2}명)보다 적어서 뽑을 수 없습니다."
        )


def main():
    # 처음 설정
    num1, num2, allowed_numbers = get_settings()

    # 게임 시작
    game = True

    while game:
        # 발표자 뽑기 (딜레이/애니메이션 없이 즉시 결과 출력)
        select_speakers(num2, allowed_numbers)

        while True:
            selection = input(
                "\n선택해주세요 (1: 다시 뽑기 / 2: 초기화 / 3: 종료): "
            ).strip()

            # 1을 입력하면 같은 조건으로 다시 뽑기 (기존 당첨 번호도 그대로 포함)
            if selection == '1':
                break

            # 2를 입력하면 처음부터 다시 입력
            elif selection == '2':
                num1, num2, allowed_numbers = get_settings()
                break

            # 3 또는 종료 입력 시 프로그램 종료
            elif selection in ('3', 'q', 'Q', 'exit'):
                print("\n👋 프로그램을 종료합니다.")
                game = False
                break

            # 그 외 입력 시 에러
            else:
                print("❌ 에러: 1, 2, 3 중 하나만 입력해주세요.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다.")
        sys.exit(0)
