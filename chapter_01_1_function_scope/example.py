"""
Chapter 1-1: 파이썬 함수와 스코프
파이썬의 함수 정의, 인자 전달 방식, 스코프를 학습한다.
"""


# ========================================
# 1. 기본 함수 정의와 호출
# ========================================

def greet(name):
    """간단한 인사 함수"""
    return f"안녕하세요, {name}님!"


def add_numbers(a, b):
    """두 숫자를 더하는 함수"""
    return a + b


# ========================================
# 2. Immutable vs Mutable 인자 전달
# ========================================

def try_modify_number(num):
    """
    Immutable 객체(int)를 수정 시도
    함수 내에서 값을 변경해도 원본은 변경되지 않는다
    """
    print(f"  [함수 내부] 수정 전: {num}")
    num = num + 10  # 새로운 객체를 생성하여 할당
    print(f"  [함수 내부] 수정 후: {num}")
    return num


def try_modify_list(items):
    """
    Mutable 객체(list)를 수정 시도
    함수 내에서 값을 변경하면 원본도 변경된다
    """
    print(f"  [함수 내부] 수정 전: {items}")
    items.append(4)  # 원본 객체를 직접 수정
    print(f"  [함수 내부] 수정 후: {items}")


# ========================================
# 3. 전역 변수와 지역 변수
# ========================================

# 전역 변수
global_counter = 0


def read_global():
    """전역 변수를 읽기만 하는 함수"""
    print(f"  전역 변수 읽기: {global_counter}")


def modify_local():
    """
    지역 변수를 생성하는 함수
    전역 변수와 이름이 같아도 별개의 변수다
    """
    global_counter = 100  # 이것은 지역 변수
    print(f"  지역 변수 생성: {global_counter}")


def modify_global():
    """global 키워드로 전역 변수를 수정하는 함수"""
    global global_counter
    global_counter += 1
    print(f"  전역 변수 수정: {global_counter}")


# ========================================
# 4. 실전 예제: 장바구니 총액 계산
# ========================================

def calculate_total(cart):
    """
    장바구니의 총액을 계산한다
    
    Args:
        cart: 상품 가격 리스트
    
    Returns:
        총액
    """
    total = 0
    for price in cart:
        total += price
    return total


def apply_discount(cart, discount_rate):
    """
    장바구니의 각 상품에 할인율을 적용한다
    주의: 원본 리스트를 수정한다!
    
    Args:
        cart: 상품 가격 리스트 (mutable)
        discount_rate: 할인율 (0.0 ~ 1.0)
    """
    for i in range(len(cart)):
        cart[i] = cart[i] * (1 - discount_rate)


def apply_discount_safe(cart, discount_rate):
    """
    장바구니의 각 상품에 할인율을 적용한다
    원본을 보존하기 위해 새 리스트를 반환한다
    
    Args:
        cart: 상품 가격 리스트
        discount_rate: 할인율 (0.0 ~ 1.0)
    
    Returns:
        할인이 적용된 새로운 리스트
    """
    discounted_cart = []
    for price in cart:
        discounted_cart.append(price * (1 - discount_rate))
    return discounted_cart


def calculate_tax(amount, tax_rate=0.1):
    """
    세금을 계산한다
    
    Args:
        amount: 금액
        tax_rate: 세율 (기본값 0.1 = 10%)
    
    Returns:
        세금 포함 금액
    """
    return amount * (1 + tax_rate)


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 50)
    print("1. 기본 함수 정의와 호출")
    print("=" * 50)
    
    message = greet("홍길동")
    print(message)
    
    result = add_numbers(10, 20)
    print(f"10 + 20 = {result}")
    
    print("\n" + "=" * 50)
    print("2. Immutable vs Mutable 인자 전달")
    print("=" * 50)
    
    # Immutable 객체 (int)
    print("\n[Immutable 객체 - int]")
    original_num = 5
    print(f"원본 값: {original_num}")
    returned_num = try_modify_number(original_num)
    print(f"함수 호출 후 원본: {original_num}")  # 변경 안됨!
    print(f"함수 반환값: {returned_num}")
    
    # Mutable 객체 (list)
    print("\n[Mutable 객체 - list]")
    original_list = [1, 2, 3]
    print(f"원본 리스트: {original_list}")
    try_modify_list(original_list)
    print(f"함수 호출 후 원본: {original_list}")  # 변경됨!
    
    print("\n" + "=" * 50)
    print("3. 전역 변수와 지역 변수")
    print("=" * 50)
    
    print(f"초기 전역 변수: {global_counter}")
    
    read_global()
    print(f"read_global() 호출 후: {global_counter}")
    
    modify_local()
    print(f"modify_local() 호출 후: {global_counter}")  # 변경 안됨
    
    modify_global()
    print(f"modify_global() 호출 후: {global_counter}")  # 변경됨
    
    print("\n" + "=" * 50)
    print("4. 실전 예제: 장바구니 총액 계산")
    print("=" * 50)
    
    # 장바구니 생성
    shopping_cart = [10000, 25000, 15000, 8000]
    print(f"\n장바구니: {shopping_cart}")
    
    # 총액 계산
    total = calculate_total(shopping_cart)
    print(f"총액: {total:,}원")
    
    # 할인 적용 (원본 수정)
    print("\n[할인 적용 - 원본 수정]")
    cart1 = [10000, 25000, 15000]
    print(f"할인 전: {cart1}")
    apply_discount(cart1, 0.2)  # 20% 할인
    print(f"할인 후: {cart1}")  # 원본이 변경됨!
    
    # 할인 적용 (안전한 방식)
    print("\n[할인 적용 - 안전한 방식]")
    cart2 = [10000, 25000, 15000]
    print(f"할인 전: {cart2}")
    discounted_cart = apply_discount_safe(cart2, 0.2)  # 20% 할인
    print(f"할인 후 (원본): {cart2}")  # 원본 유지
    print(f"할인 후 (새 리스트): {discounted_cart}")
    
    # 세금 계산
    print("\n[세금 계산]")
    final_amount = calculate_total(discounted_cart)
    print(f"할인 후 금액: {final_amount:,.0f}원")
    amount_with_tax = calculate_tax(final_amount)
    print(f"세금 포함 금액: {amount_with_tax:,.0f}원")
    
    # 기본값 다르게 세금 계산
    amount_with_tax_15 = calculate_tax(final_amount, 0.15)
    print(f"세금 15% 포함 금액: {amount_with_tax_15:,.0f}원")
    
    print("\n" + "=" * 50)
    print("학습 완료!")
    print("=" * 50)

