from info import *


class Menu:
    def __init__(self):
        self.account_list = []

    def check(self, account_num):
        for i in range(len(self.account_list)):
            if self.account_list[i].account_num == account_num:
                return True
        return False

    def new_account(self):
        print("\n======계좌개설======")
        account_num = input("계좌번호: ")
        name = input("이름: ")
        save = input("예금: ")
        flag = 1
        if name == "":
            print("이름은 공백일 수 없습니다.")
            flag = 0
        if self.check(account_num):
            print("중복된 계좌입니다. ")
            flag = 0
        if account_num == "" or account_num.isalpha() or int(account_num) < 0:
            print("올바르지 않은 계좌번호입니다. 공백, 문자, 마이너스 안됨")
            flag = 0
        if save == "" or save.isalpha():
            print("예금을 잘못입력했습니다. 공백, 문자, 마이너스 안됨")
            flag = 0
        if flag == 0:
            print("계좌 개설을 다시 합니다.")
            self.new_account()
        else:
            account_num = int(account_num)
            save = int(save)
            account = Info(account_num, name, save)
            self.account_list.append(account)
            print("##계좌개설을 완료하였습니다##")
            print("===================\n")

    def deposit(self):
        print("\n======입금하기======")
        flag = 1
        account_num = int(input("입금하실 계좌번호를 입력해주세요: "))
        for i in range(len(self.account_list)):
            if self.account_list[i].account_num == account_num:
                flag = 0
                print("계좌이름:", self.account_list[i].name)
                print("계좌잔고:", self.account_list[i].save, "원")
                while True:
                    money = int(input("입금하실 금액을 입력해주세요: "))
                    if money <= 0:
                        print("입금은 1원 이상부터입니다. ")
                        continue
                    else:
                        break
                self.account_list[i].save += money
                print("##계좌잔고:", self.account_list[i].save, "원##")
                print("##입금이 완료되었습니다##")
        if flag == 1:
            print("존재하지 않는 계좌입니다. ")
            self.deposit()
        else:
            print("===================\n")

    def withdraw(self):
        print("\n======출금하기======")
        flag = 1
        account_num = int(input("출금하실 계좌번호를 입력해주세요: "))
        for i in range(len(self.account_list)):
            if self.account_list[i].account_num == account_num:
                flag = 0
                print("계좌이름:", self.account_list[i].name)
                print("계좌잔고:", self.account_list[i].save, "원")
                while True:
                    money = int(input("출금하실 금액을 입력해주세요: "))
                    if money <= 0:
                        print("출금은 1원 이상부터입니다. ")
                        continue
                    else:
                        if self.account_list[i].save >= money:
                            self.account_list[i].save -= money
                            break
                        else:
                            print("##잔고가 부족하여 출금에 실패하였습니다.##")
                            continue
                print("##계좌잔고:", self.account_list[i].save, "원##")
                print("##출금이 완료되었습니다##")
        if flag == 1:
            print("존재하지 않는 계좌입니다. ")
            self.withdraw()
        else:
            print("===================\n")

    def all_account(self):
        print("\n======전체조회======")
        if len(self.account_list) == 0:
            print("조회할 계좌가 없습니다. ")
        else:
            for i in range(len(self.account_list)):
                print("계좌번호:", self.account_list[i].account_num, "/ 이름:",
                      self.account_list[i].name, "/ 잔액:", self.account_list[i].save, "원")
        print("===================\n")
