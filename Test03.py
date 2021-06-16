class Account:
    def __init__(self,account="",account_name="",f_money=0):
        self.account = account
        self.account_name = account_name
        self.f_money = f_money
def ui():
    return f""" -----------------------------------
    1. 계좌생성 | 2. 계좌목록 | 3. 예금 | 4. 출금 | 5. 송금
    6. 내역조회 | 7. 종료
    -----------------------------------------------
    선택> """
account_list = []

class Account_Manage(Account):
    def pick1(self):
        global account_list
        self.account = input("계좌번호 : ")
        self.account_name = input("계좌주 : ")
        self.f_money = int(input("초기입금액 : "))
        account_list.append(Account(self.account,self.account_name,self.f_money))
        print("결과 : 계좌가 생성되었습니다.")

    def pick2(self):
        for i in account_list:
            print(f"계좌번호 : {i.account}, 계좌주 : {i.account_name}, 초기입금액 : {i.f_money} ")

    def pick3(self):
        search = input("계좌번호 : ")
        add_money = int(input("예금액 : "))
        for i in account_list:
            if search == i.account:
                i.f_money+=add_money
                print("결과 : 예금이 성공되었습니다.")
            else:
                print("잘못입력하셨습니다.")

    def pick4(self):
        search = input("계좌번호 : ")
        add_money = int(input("출금액 : "))
        for i in account_list:
            if search == i.account:
                i.f_money-=add_money
                print("결과 : 출금이 성공되었습니다.")
            else:
                print("잘못입력하셨습니다.")

send ={}
class Add_menu(Account_Manage):
    def pick5(self):
        global send
        search = input("계좌번호 : ")
        other_search = input("받는 사람 계좌 번호 : ")
        send_money = int(input("송금액 : "))
        for i in account_list:
            if search == i.account:
                i.f_money -= send_money
                send[search] = -send_money
            else:
                print("잘못입력하셨습니다.")
        for j in account_list:
            if other_search == j.account:
                j.f_money += send_money
                send[other_search] = +send_money
                print(f"결과 : {other_search} 계좌로 {send_money}원 송금되었습니다.")
            else:
                print("잘못입력하셨습니다.")


    def pick6(self):
        search = input("계좌번호 : ")
        for i in account_list:
            if search == i.account:
                print(f"요청하신 거래내역은{send[search]}입니다.")

manage = Account_Manage()
add = Add_menu()
run = True
while (run):
    pick = int(input(ui()))

    if pick == 1:
        manage.pick1()
    elif pick == 2:
        manage.pick2()
    elif pick == 3:
        manage.pick3()
    elif pick == 4:
        manage.pick4()
    elif pick == 5:
        add.pick5()
    elif pick == 6:
        add.pick6()
    elif pick == 7:
        run = False
    else:
        print("잘못 입력되었습니다.")
else:
    print("프로그램을 종료합니다.")
