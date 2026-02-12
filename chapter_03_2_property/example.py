"""
Chapter 3-2: Getter와 Setter, @property
파이썬스러운 속성 접근 방법을 학습한다.
"""


# ========================================
# 1. Java 스타일 Getter/Setter (Before)
# ========================================

class PersonJavaStyle:
    """Java 스타일의 Getter/Setter를 사용하는 클래스"""
    
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name
    
    def get_age(self) -> int:
        return self._age
    
    def set_age(self, age: int) -> None:
        if age < 0:
            raise ValueError("나이는 0 이상이어야 한다")
        self._age = age


# ========================================
# 2. @property 사용 (After)
# ========================================

class PersonPythonic:
    """@property를 사용하는 파이썬스러운 클래스"""
    
    def __init__(self, name: str, age: int):
        self._name = name
        self.age = age  # Setter를 통해 유효성 검사
    
    @property
    def name(self) -> str:
        """이름 Getter"""
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        """이름 Setter"""
        if not name:
            raise ValueError("이름은 비어있을 수 없다")
        self._name = name
    
    @property
    def age(self) -> int:
        """나이 Getter"""
        return self._age
    
    @age.setter
    def age(self, age: int) -> None:
        """나이 Setter - 유효성 검사 포함"""
        if age < 0:
            raise ValueError("나이는 0 이상이어야 한다")
        if age > 150:
            raise ValueError("나이는 150 이하여야 한다")
        self._age = age


# ========================================
# 3. Temperature 클래스 - 섭씨/화씨 변환
# ========================================

class Temperature:
    """온도 클래스 - 섭씨와 화씨를 자동 변환한다"""
    
    def __init__(self, celsius: float):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        """섭씨 온도"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        """섭씨 온도 설정"""
        if value < -273.15:
            raise ValueError("절대영도보다 낮을 수 없다")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """화씨 온도 (계산됨)"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """화씨 온도 설정"""
        self.celsius = (value - 32) * 5/9


# ========================================
# 4. Circle 클래스 - 읽기 전용 속성
# ========================================

class Circle:
    """원 클래스 - 반지름으로 면적과 둘레 계산"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    @property
    def radius(self) -> float:
        """반지름"""
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        """반지름 설정"""
        if value <= 0:
            raise ValueError("반지름은 0보다 커야 한다")
        self._radius = value
    
    @property
    def area(self) -> float:
        """면적 (읽기 전용)"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self) -> float:
        """둘레 (읽기 전용)"""
        return 2 * 3.14159 * self._radius


# ========================================
# 5. BankAccount 클래스 - 실전 예제
# ========================================

class BankAccount:
    """은행 계좌 클래스"""
    
    def __init__(self, owner: str, balance: int = 0):
        self._owner = owner
        self._balance = balance
        self._transaction_count = 0
    
    @property
    def owner(self) -> str:
        """계좌 소유자 (읽기 전용)"""
        return self._owner
    
    @property
    def balance(self) -> int:
        """잔액 (읽기 전용)"""
        return self._balance
    
    @property
    def transaction_count(self) -> int:
        """거래 횟수 (읽기 전용)"""
        return self._transaction_count
    
    def deposit(self, amount: int) -> None:
        """입금"""
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 한다")
        self._balance += amount
        self._transaction_count += 1
        print(f"{amount:,}원 입금 완료")
    
    def withdraw(self, amount: int) -> None:
        """출금"""
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 한다")
        if amount > self._balance:
            raise ValueError("잔액이 부족하다")
        self._balance -= amount
        self._transaction_count += 1
        print(f"{amount:,}원 출금 완료")


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. Java 스타일 vs 파이썬 스타일")
    print("=" * 60)
    
    # Java 스타일
    print("\n[Java 스타일]")
    java_person = PersonJavaStyle("김철수", 25)
    print(f"이름: {java_person.get_name()}")
    print(f"나이: {java_person.get_age()}")
    java_person.set_age(30)
    print(f"변경 후 나이: {java_person.get_age()}")
    
    # 파이썬 스타일
    print("\n[파이썬 스타일 (@property)]")
    python_person = PersonPythonic("이영희", 28)
    print(f"이름: {python_person.name}")
    print(f"나이: {python_person.age}")
    python_person.age = 32
    print(f"변경 후 나이: {python_person.age}")
    
    print("\n" + "=" * 60)
    print("2. 유효성 검사")
    print("=" * 60)
    
    print("\n[유효한 값]")
    person = PersonPythonic("박민수", 25)
    print(f"생성 성공: {person.name}, {person.age}세")
    
    print("\n[유효하지 않은 값]")
    try:
        person.age = -5
    except ValueError as e:
        print(f"에러: {e}")
    
    try:
        person.age = 200
    except ValueError as e:
        print(f"에러: {e}")
    
    try:
        person.name = ""
    except ValueError as e:
        print(f"에러: {e}")
    
    print("\n" + "=" * 60)
    print("3. Temperature 클래스 - 자동 변환")
    print("=" * 60)
    
    temp = Temperature(25.0)
    print(f"\n섭씨 {temp.celsius}도")
    print(f"화씨 {temp.fahrenheit:.1f}도")
    
    print("\n[화씨로 설정]")
    temp.fahrenheit = 86.0
    print(f"화씨 {temp.fahrenheit}도")
    print(f"섭씨 {temp.celsius}도")
    
    print("\n" + "=" * 60)
    print("4. Circle 클래스 - 읽기 전용 속성")
    print("=" * 60)
    
    circle = Circle(5.0)
    print(f"\n반지름: {circle.radius}")
    print(f"면적: {circle.area:.2f}")
    print(f"둘레: {circle.circumference:.2f}")
    
    print("\n[반지름 변경]")
    circle.radius = 10.0
    print(f"반지름: {circle.radius}")
    print(f"면적: {circle.area:.2f}")
    print(f"둘레: {circle.circumference:.2f}")
    
    print("\n[읽기 전용 속성 변경 시도]")
    try:
        circle.area = 100  # type: ignore[misc]
    except AttributeError:
        print("에러: area는 읽기 전용이다")
    
    print("\n" + "=" * 60)
    print("5. BankAccount 클래스 - 실전 예제")
    print("=" * 60)
    
    account = BankAccount("최지은", 1000000)
    
    print(f"\n계좌 소유자: {account.owner}")
    print(f"초기 잔액: {account.balance:,}원")
    
    print("\n[입금]")
    account.deposit(500000)
    print(f"잔액: {account.balance:,}원")
    
    print("\n[출금]")
    account.withdraw(300000)
    print(f"잔액: {account.balance:,}원")
    
    print(f"\n거래 횟수: {account.transaction_count}회")
    
    print("\n[읽기 전용 확인]")
    try:
        account.balance = 9999999  # type: ignore[misc]
    except AttributeError:
        print("에러: balance는 읽기 전용이다")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)
    print("\n@property의 장점:")
    print("- 속성처럼 직관적으로 접근")
    print("- 유효성 검사 가능")
    print("- 읽기 전용 속성 구현 가능")
    print("- 계산된 속성 제공 가능")

