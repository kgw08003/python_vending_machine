from menu import MENU

# 재고 기본 값, 입력 받은 메뉴 재고 확인하기
ingredients = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# 리포트 출력 함수
def report_ingredients():
    water = ingredients["water"]
    milk = ingredients["milk"]
    coffee = ingredients["coffee"]
    money = ingredients["money"]
    print(f"물: {water}ml")
    print(f"우유: {milk}ml")
    print(f"커피: {coffee}g")
    print(f"돈: {money}원")

# 재고 확인 함수
def comp_ingredient(select):
    select_ingredient = MENU[select]["ingredients"]
    insufficient = ""
    result = True
    if select_ingredient["water"] > ingredients["water"]:
        result = False
        insufficient += "물"
    if select == "latte" or select == "cappuccino":
        if select_ingredient["milk"] > ingredients["milk"]:
            if result:
                insufficient += "우유"
            else:
                insufficient += ", 우유"
            result = False
    if select_ingredient["coffee"] > ingredients["coffee"]:
        if result:
            insufficient += "커피"
        else:
            insufficient += ", 커피"
        result = False
    if not result:
        print(f"죄송합니다 {insufficient}이(가) 부족합니다.")
    return result

# 돈 받는 함수
def input_price():
    won_500 = int(input("500원 몇 개를 넣으실건가요?: "))
    won_100 = int(input("100원 몇 개를 넣으실건가요?: "))
    won_50 = int(input("50원 몇 개를 넣으실건가요?: "))
    won_10 = int(input("10원 몇개를 넣으실건가요?: "))
    paid_money = (won_500 * 500) + (won_100 * 100) + (won_50 * 50) + (won_10 * 10)
    return paid_money

# 가격 비교 함수
def comp_price(select, paid_money):
    result = False
    select_price = MENU[select]["cost"]
    if paid_money >= select_price:
        change = paid_money - select_price
        print(f"잔돈 {change}원 입니다.")
        print(f"여기 {select}입니다.☕ 맛있게드세요!")
        result = True
    else:
        print("액수가 부족합니다.")
    return result

# 재고 빼기 함수
def left_ingredients(select):
    select_ingredient = MENU[select]["ingredients"]
    select_price = MENU[select]["cost"]
    ingredients["water"] -= select_ingredient["water"]
    ingredients["coffee"] -= select_ingredient["coffee"]
    if select == "latte" or select == "cappuccino":
        ingredients["milk"] -= select_ingredient["milk"]
    ingredients["money"] += select_price

# 메인 함수
restart = False
while not restart:
    customer_select = input("무엇을 드시겠습니까?(espresso / latte / cappuccino): ").lower()
    if customer_select == "report":
        report_ingredients()
    elif customer_select == "off":
        restart = True
    elif customer_select == "espresso" or customer_select == "latte" or customer_select == "cappuccino":
        if comp_ingredient(customer_select):
            print("돈을 넣어주세요")
            paid_price = input_price()
            result_price_comp = comp_price(customer_select, paid_price)
            if result_price_comp:
                left_ingredients(customer_select)
    else:
        print("없는 메뉴입니다.")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 800,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 1000,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 1200,
    }
}

