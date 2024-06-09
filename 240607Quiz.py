def display_menu():
    print("메뉴를 선택해주세요:")
    print("1. 냉면")
    print("2. 볶음밥")
    print("3. 피자")
    print("4. 짜장면")

def get_user_choice():
    while True:
        choice = input("메뉴 번호를 입력해주세요: ")
        if choice.isdigit():  # 입력이 숫자인지 확인
            choice = int(choice)
            if 1 <= choice <= 4:  # 입력이 1부터 4 사이인지 확인
                return choice
            else:
                print("잘못된 메뉴 번호입니다. 1부터 4까지의 숫자를 입력해주세요.")
        else:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")

def main():
    menu = ["냉면", "볶음밥", "피자", "짜장면"]
    display_menu()
    user_choice = get_user_choice()
    print("선택하신 메뉴는 {}입니다.".format(menu[user_choice - 1]))

if __name__ == "__main__":
    main()
