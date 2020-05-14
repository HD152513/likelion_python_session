import sys

class Info:
    def __init__(self, account_num, name, save):
        self.account_num = account_num
        self.name = name
        self.save = save


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
        account_num = int(input("계좌번호: "))
        name = input("이름: ")
        save = int(input("예금: "))
        if self.check(account_num):
            print("중복된 계좌입니다. ")
            self.new_account()
        else:
            account = Info(account_num, name, save)
            self.account_list.append(account)
            print("##계좌개설을 완료하였습니다##")
            print("===================\n")

    def deposit(self):
        print("\n======입금하기======")
        account_num = int(input("입금하실 계좌번호를 입력해주세요: "))
        for i in range(len(self.account_list)):
            if self.account_list[i].account_num == account_num:
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
        print("===================\n")


    def withdraw(self):
        print("\n======출금하기======")
        account_num = int(input("출금하실 계좌번호를 입력해주세요: "))
        for i in range(len(self.account_list)):
            if self.account_list[i].account_num == account_num:
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

    def earnmoney(self):
        print("\n======적금하기======")
        account_num = int(input("적금하실 계좌번호를 입력해주세요: "))
        for i in range(len(self.account_list)):
            if self.account_list[i].account_num == account_num:
                print("계좌이름:", self.account_list[i].name)
                while True:
                    money = int(input("1년동안 매월 적금하실 금액을 입력해주세요: "))
                    if money <= 0:
                        print("적금은 1원 이상부터입니다. ")
                        continue
                    else:
                        break
                    
                self.account_list[i].save += money*((1.1)**12)
                print("금리는 10% 입니다")
                print("1년 후 잔액:", int(self.account_list[i].save), "원")
                print("##적금이 완료되었습니다##")
                
                
        print("===================\n")


if __name__ == "__main__":
    a = Menu()
    while True:
        print("======Bank Menu=====")
        print("1. 계좌개설")
        print("2. 입금하기")
        print("3. 출금하기")
        print("4. 전체조회")
        print("5. 프로그램 종료")
        print("6. 적금하기")
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
        elif num == "6":
            a.earnmoney()
        else:
            print("\n**잘못 입력하셨습니다**\n")
