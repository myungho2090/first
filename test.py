# if문----------------------------------------------

# su =int(input("숫자를 입력하세요."))
# if su % 2 == 0 :
#     print(su,"(은)는 짝수이다.")
#     print(su, "하하하")

# else :
#     print(su,"(은)는 홀수 입니다.")

# if문 합격코드-------------------------------------------

# pa = 80
# score=int(input("당신의 점수를 입력하세요."))
# if score >= pa :
#     print("합격입니다.")
# else :
#     print("불합격입니다.")

# import와 random모듈------------------------------------

# import random
# print(random.random())

# import random
# print(f"선택한 수는: {random.randint(0, 5)} 입니다.")

# import random
# a = random.uniform(1.14, 36.5)
# print(f"1.14와 36.5 사이의 선택한수는 {a}입니다.")

# import random
# a = random.randrange(5,20)
# print(f"5와20 사이의 선택한수는 {a}입니다.")

# import random
# a = ["apple", "book", "cat", "dog", "bat"]
# random.shuffle(a) #순서를바꾸는것.(shuffle)
# print(f"{a}입니다.")


# import random
# a = ["apple", "book", "cat", "dog", "bat"]
# print(f"{random.choice(a)}입니다.")

# import random
# a=random.choices([1,2,3,4,5],[10,10,20,20,5])
# print(f"{a}입니다.")

# import random
# a=[1,2,3,4,5,6,7,8,9,10]
# b=random.sample(a, 3)
# print(f"{b}입니다.")

# 숫자 맞추는게임-------------------------------------------
# import random
# print("컴퓨터가 선택한 숫자를 맞춰 보세요.")
# value=int(input("1부터 10까지 숫자 중 한개를 선택해 주세요."))
# computer = random.randint(1, 10)
# if computer == value:
#     print("성공입니다.!!")
# else :
#     print("실패하셨습니다.컴퓨터가 선택한 숫자는",computer,"입니다.")


# elif문 이용하여 햄버거 주문프로그램 만들기---------------------------

###############################

# store="""buger"""
# menu="""
# 불고기 버거 : 5,500원
# 치즈 버거 : 4,500원
# 에그 버거 : 4,000원
# 콜라 : 2,000원
# 사이다 : 2,000원

# 각 버거 세트 메뉴 있습니다.
# 세트 메뉴 주문시에는 500원 할인됩니다."""

# print(store)
# print("#"*40)
# print(menu)
# print("#" * 40)
# burger = input("버거를 선택헤 주세요. 예)불고기,치즈,에그>>>")
# drink = input("음료를 선택해 주세요. 예)콜라,사이다>>>")
# combo = input("세트메뉴 주문하시겠습니까? 예) 네,아니오>>>")
# b_price = 0
# d_price = 0
# price = 0

# #####햄버거 주문#################

# if burger == "불고기":
#     b_price = 5500
#     print("선택한 버거는:",burger,"이며 가격은",b_price,"입니다.")
# elif burger == "치즈":
#     b_price = 4500
#     print("선택한 버거는:",burger,"이며 가격은",b_price,"입니다.")
# elif burger =="에그":
#     b_price = 4000
#     print("선택한 버거는:",burger,"이며 가격은",b_price,"입니다.")
# else:
#     print("<선택한 버거는 메뉴에 없습니다.>")


# if drink == "콜라":
#     d_price = 2000
#     print("선택한 음료는:",drink,"이며 가격은",d_price,"입니다.")
# elif drink == "사이다":
#     d_price = 2000
#     print("선택한 음료는:",drink,"이며 가격은",d_price,"입니다.")
# else:
#     print("<선택한 음료가 메뉴에 없습니다.>")
# #총금액
# if combo == "네":
#     price = b_price+d_price
#     price -=500
#     print(f"할인된 총 금액은{price}원 입니다.")
# else :
#     price = b_price+d_price
#     print(f"총 금액은 {price}원 입니다.")
    

#------- for,while문 ------------#

# for i in range(5):
#     print(i)
#     print('---------')

# for i in range(5):
#     print(i,end='')
#     print('---------')

####### 구구단 #############
# a =2 
# for i in range(1,10):
#     print(f"{a}*{i}={a*i}")

######   while ##########

# a = 2
# while a < 10 :
#     for i in range(1,10):
#         print(f"{a}*{i}={a*i}")
#     a += 1
    
##### 원하는 구구단 출력하기 #######

# gugudan = int(input("몇 단을 출력할까요?"))
# i = 1
# while i < 10:
#     i += 1
#     print(f"{gugudan}*{i}={gugudan*i}")
    
# print("while문 끝")

####-----break-----------#####
# for i in range(10):
#     print(i)
#     if i == 1:
#         print("정지")
#         break

##########숫자 맞히기 게임 만들기 ##############

import random
quiz="""퀴즈"""
print(quiz)
print("1~5 사이의 숫자가 있습니다.")
print()

computer_ho = random.randint(1, 5)
user_ho = 0
count = 0

while computer_ho != user_ho:
    user_ho = int(input("컴퓨터가 뽑은 숫자는 무엇일까요?"))
    count += 1
    
    if computer_ho > user_ho:
        print("더 큰수 입니다.")
    elif computer_ho < user_ho:
        print("더 작은 수 입니다.")
    if count == 5:
        print(f"5회 초과입니다. 정답은{computer_ho}입니다.")
    print()
    
print(f"정답입니다! 컴퓨터가 선택한 숫자는{computer_ho}입니다.")
print(f"총{count}회만에 맞추셨습니다.")
