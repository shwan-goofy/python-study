"""
Chapter 4-3: 추상 클래스와 인터페이스
abc 모듈을 사용하여 추상 클래스를 작성한다.
"""

from abc import ABC, abstractmethod


# ========================================
# 1. 추상 클래스
# ========================================

class Animal(ABC):
    """추상 동물 클래스"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def speak(self) -> str:
        """반드시 구현해야 하는 추상 메서드"""
        pass
    
    def introduce(self) -> str:
        """구체적 메서드"""
        return f"나는 {self.name}이다"


class Dog(Animal):
    """개 클래스"""
    
    def speak(self) -> str:
        return "멍멍"


class Cat(Animal):
    """고양이 클래스"""
    
    def speak(self) -> str:
        return "야옹"


# ========================================
# 2. Payment 추상 클래스
# ========================================

class Payment(ABC):
    """결제 추상 클래스"""
    
    @abstractmethod
    def pay(self, amount: int) -> bool:
        """결제 처리"""
        pass
    
    @abstractmethod
    def refund(self, amount: int) -> bool:
        """환불 처리"""
        pass


class CreditCard(Payment):
    """신용카드 결제"""
    
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def pay(self, amount: int) -> bool:
        print(f"신용카드로 {amount:,}원 결제")
        return True
    
    def refund(self, amount: int) -> bool:
        print(f"신용카드로 {amount:,}원 환불")
        return True


class Cash(Payment):
    """현금 결제"""
    
    def pay(self, amount: int) -> bool:
        print(f"현금으로 {amount:,}원 결제")
        return True
    
    def refund(self, amount: int) -> bool:
        print(f"현금으로 {amount:,}원 환불")
        return True


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. 추상 클래스")
    print("=" * 60)
    
    dog = Dog("바둑이")
    cat = Cat("나비")
    
    print(f"\n{dog.introduce()}: {dog.speak()}")
    print(f"{cat.introduce()}: {cat.speak()}")
    
    print("\n" + "=" * 60)
    print("2. Payment 추상 클래스")
    print("=" * 60)
    
    payments: list[Payment] = [
        CreditCard("1234-5678-9012-3456"),
        Cash()
    ]
    
    print("\n[결제]")
    for payment in payments:
        payment.pay(10000)
    
    print("\n[환불]")
    for payment in payments:
        payment.refund(5000)
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)

