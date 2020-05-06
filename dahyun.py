import sys
from menu import *

if __name__ == "__main__":
    a = Menu()
    while True:
        print("======Bank Menu=====")
        print("1. 계좌개설")
        print("2. 입금하기")
        print("3. 출금하기")
        print("4. 전체조회")
        print("5. 프로그램 종료")
        print("====================")
        num = input("입력: ")
        if num == "1":
            a.new_account()
        elif num == "2":
            a.deposit()
        elif num == "3":
            a.withdraw()
        elif num == "4":
            a.all_account()
        elif num == "5":
            print("\n##프로그램을 종료합니다##")
            sys.exit()
        else:
            print("\n**잘못 입력하셨습니다**\n")