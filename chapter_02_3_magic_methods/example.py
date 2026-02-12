"""
Chapter 2-3: 매직 메서드 (Magic Methods)
특별한 메서드들을 사용하여 객체의 동작을 커스터마이징한다.
"""

import math
from typing import Any


# ========================================
# 1. __str__과 __repr__
# ========================================

class Person:
    """사람 클래스 - 문자열 표현 메서드를 구현한다"""
    
    def __init__(self, name: str, age: int):
        """
        Person 인스턴스를 초기화한다
        
        Args:
            name: 이름
            age: 나이
        """
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        """
        사용자 친화적인 문자열 표현
        print() 함수가 호출한다
        
        Returns:
            사용자용 문자열
        """
        return f"{self.name} ({self.age}세)"
    
    def __repr__(self) -> str:
        """
        개발자를 위한 명확한 문자열 표현
        객체를 재생성할 수 있는 형태가 이상적이다
        
        Returns:
            개발자용 문자열
        """
        return f"Person(name='{self.name}', age={self.age})"


# ========================================
# 2. Vector2D 클래스 - 연산자 오버로딩
# ========================================

class Vector2D:
    """2차원 벡터 클래스 - 다양한 매직 메서드를 구현한다"""
    
    def __init__(self, x: float, y: float):
        """
        Vector2D 인스턴스를 초기화한다
        
        Args:
            x: x 좌표
            y: y 좌표
        """
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """사용자 친화적인 문자열 표현"""
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """개발자용 문자열 표현"""
        return f"Vector2D(x={self.x}, y={self.y})"
    
    def __add__(self, other: "Vector2D") -> "Vector2D":
        """
        벡터 덧셈 (+)
        
        Args:
            other: 더할 벡터
        
        Returns:
            새로운 벡터
        """
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Vector2D") -> "Vector2D":
        """
        벡터 뺄셈 (-)
        
        Args:
            other: 뺄 벡터
        
        Returns:
            새로운 벡터
        """
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> "Vector2D":
        """
        스칼라 곱셈 (*)
        
        Args:
            scalar: 스칼라 값
        
        Returns:
            새로운 벡터
        """
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other: object) -> bool:
        """
        동등 비교 (==)
        
        Args:
            other: 비교할 객체
        
        Returns:
            동등 여부
        """
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other: object) -> bool:
        """
        부등 비교 (!=)
        
        Args:
            other: 비교할 객체
        
        Returns:
            부등 여부
        """
        return not self.__eq__(other)
    
    def __abs__(self) -> float:
        """
        벡터의 크기 (abs())
        
        Returns:
            벡터의 크기
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __neg__(self) -> "Vector2D":
        """
        벡터의 부호 반전 (-)
        
        Returns:
            부호가 반전된 벡터
        """
        return Vector2D(-self.x, -self.y)


# ========================================
# 3. Money 클래스 - 비교 연산자
# ========================================

class Money:
    """돈을 표현하는 클래스 - 비교 연산자를 구현한다"""
    
    def __init__(self, amount: int, currency: str = "KRW"):
        """
        Money 인스턴스를 초기화한다
        
        Args:
            amount: 금액
            currency: 통화 (기본값: KRW)
        """
        self.amount = amount
        self.currency = currency
    
    def __str__(self) -> str:
        """사용자 친화적인 문자열 표현"""
        return f"{self.amount:,} {self.currency}"
    
    def __repr__(self) -> str:
        """개발자용 문자열 표현"""
        return f"Money(amount={self.amount}, currency='{self.currency}')"
    
    def __add__(self, other: "Money") -> "Money":
        """돈을 더한다"""
        if self.currency != other.currency:
            raise ValueError("통화가 다르면 더할 수 없다")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other: "Money") -> "Money":
        """돈을 뺀다"""
        if self.currency != other.currency:
            raise ValueError("통화가 다르면 뺄 수 없다")
        return Money(self.amount - other.amount, self.currency)
    
    def __eq__(self, other: object) -> bool:
        """동등 비교"""
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other: "Money") -> bool:
        """작다 비교 (<)"""
        if self.currency != other.currency:
            raise ValueError("통화가 다르면 비교할 수 없다")
        return self.amount < other.amount
    
    def __le__(self, other: "Money") -> bool:
        """작거나 같다 비교 (<=)"""
        if self.currency != other.currency:
            raise ValueError("통화가 다르면 비교할 수 없다")
        return self.amount <= other.amount
    
    def __gt__(self, other: "Money") -> bool:
        """크다 비교 (>)"""
        if self.currency != other.currency:
            raise ValueError("통화가 다르면 비교할 수 없다")
        return self.amount > other.amount
    
    def __ge__(self, other: "Money") -> bool:
        """크거나 같다 비교 (>=)"""
        if self.currency != other.currency:
            raise ValueError("통화가 다르면 비교할 수 없다")
        return self.amount >= other.amount


# ========================================
# 4. CustomList 클래스 - 컨테이너 매직 메서드
# ========================================

class CustomList:
    """커스텀 리스트 클래스 - 컨테이너 매직 메서드를 구현한다"""
    
    def __init__(self):
        """CustomList 인스턴스를 초기화한다"""
        self._items: list[Any] = []
    
    def append(self, item: Any) -> None:
        """
        아이템을 추가한다
        
        Args:
            item: 추가할 아이템
        """
        self._items.append(item)
    
    def __len__(self) -> int:
        """
        길이를 반환한다 (len())
        
        Returns:
            리스트 길이
        """
        return len(self._items)
    
    def __getitem__(self, index: int) -> Any:
        """
        인덱스로 아이템을 가져온다 (obj[index])
        
        Args:
            index: 인덱스
        
        Returns:
            해당 인덱스의 아이템
        """
        return self._items[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        """
        인덱스에 아이템을 설정한다 (obj[index] = value)
        
        Args:
            index: 인덱스
            value: 설정할 값
        """
        self._items[index] = value
    
    def __contains__(self, item: Any) -> bool:
        """
        아이템 포함 여부를 확인한다 (item in obj)
        
        Args:
            item: 확인할 아이템
        
        Returns:
            포함 여부
        """
        return item in self._items
    
    def __iter__(self):
        """
        이터레이터를 반환한다 (for 루프 지원)
        
        Returns:
            이터레이터
        """
        return iter(self._items)
    
    def __str__(self) -> str:
        """사용자 친화적인 문자열 표현"""
        return f"CustomList({self._items})"
    
    def __repr__(self) -> str:
        """개발자용 문자열 표현"""
        return f"CustomList(items={self._items})"


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. __str__과 __repr__")
    print("=" * 60)
    
    person = Person("홍길동", 25)
    
    print(f"\nprint() 사용 (__str__ 호출):")
    print(person)
    
    print(f"\nrepr() 사용 (__repr__ 호출):")
    print(repr(person))
    
    print(f"\n리스트에 담으면 __repr__이 사용된다:")
    people = [person, Person("김철수", 30)]
    print(people)
    
    print("\n" + "=" * 60)
    print("2. Vector2D 클래스 - 연산자 오버로딩")
    print("=" * 60)
    
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"\nv1 = {v1}")
    print(f"v2 = {v2}")
    
    # 덧셈
    v3 = v1 + v2
    print(f"\nv1 + v2 = {v3}")
    
    # 뺄셈
    v4 = v1 - v2
    print(f"v1 - v2 = {v4}")
    
    # 스칼라 곱셈
    v5 = v1 * 2
    print(f"v1 * 2 = {v5}")
    
    # 크기
    print(f"\n|v1| = {abs(v1):.2f}")
    print(f"|v2| = {abs(v2):.2f}")
    
    # 부호 반전
    v6 = -v1
    print(f"-v1 = {v6}")
    
    # 비교
    print(f"\nv1 == v2: {v1 == v2}")
    print(f"v1 != v2: {v1 != v2}")
    
    v7 = Vector2D(3, 4)
    print(f"v1 == v7: {v1 == v7}")
    
    # 체이닝 연산
    print(f"\n[체이닝 연산]")
    result = v1 + v2 - Vector2D(1, 1)
    print(f"v1 + v2 - (1, 1) = {result}")
    
    print("\n" + "=" * 60)
    print("3. Money 클래스 - 비교 연산자")
    print("=" * 60)
    
    money1 = Money(10000)
    money2 = Money(20000)
    money3 = Money(10000)
    
    print(f"\nmoney1 = {money1}")
    print(f"money2 = {money2}")
    print(f"money3 = {money3}")
    
    # 산술 연산
    print(f"\n[산술 연산]")
    print(f"money1 + money2 = {money1 + money2}")
    print(f"money2 - money1 = {money2 - money1}")
    
    # 비교 연산
    print(f"\n[비교 연산]")
    print(f"money1 == money2: {money1 == money2}")
    print(f"money1 == money3: {money1 == money3}")
    print(f"money1 < money2: {money1 < money2}")
    print(f"money1 <= money3: {money1 <= money3}")
    print(f"money2 > money1: {money2 > money1}")
    print(f"money2 >= money1: {money2 >= money1}")
    
    # 정렬
    money_list = [Money(50000), Money(10000), Money(30000), Money(20000)]
    sorted_money = sorted(money_list)
    print(f"\n[정렬]")
    print(f"정렬 전: {[str(m) for m in money_list]}")
    print(f"정렬 후: {[str(m) for m in sorted_money]}")
    
    print("\n" + "=" * 60)
    print("4. CustomList 클래스 - 컨테이너 매직 메서드")
    print("=" * 60)
    
    custom_list = CustomList()
    
    # 아이템 추가
    custom_list.append(10)
    custom_list.append(20)
    custom_list.append(30)
    
    print(f"\n{custom_list}")
    
    # 길이
    print(f"\n길이: {len(custom_list)}")
    
    # 인덱싱
    print(f"\n[인덱싱]")
    print(f"custom_list[0] = {custom_list[0]}")
    print(f"custom_list[1] = {custom_list[1]}")
    
    # 아이템 설정
    print(f"\n[아이템 설정]")
    custom_list[1] = 25
    print(f"custom_list[1] = 25 실행 후: {custom_list}")
    
    # 포함 여부
    print(f"\n[포함 여부]")
    print(f"10 in custom_list: {10 in custom_list}")
    print(f"40 in custom_list: {40 in custom_list}")
    
    # 반복
    print(f"\n[반복]")
    for i, item in enumerate(custom_list):
        print(f"  {i}: {item}")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)
    print("\n매직 메서드의 장점:")
    print("- 직관적인 연산자 사용 가능")
    print("- 파이썬 내장 함수들과 자연스럽게 통합")
    print("- 코드의 가독성 향상")

