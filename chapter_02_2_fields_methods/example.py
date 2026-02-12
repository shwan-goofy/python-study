"""
Chapter 2-2: 필드(Fields)와 메서드(Methods)
인스턴스 변수, 클래스 변수, 그리고 다양한 메서드를 학습한다.
"""

from typing import Optional


# ========================================
# 1. 인스턴스 변수 vs 클래스 변수
# ========================================

class Counter:
    """카운터 클래스 - 클래스 변수와 인스턴스 변수를 비교한다"""
    
    # 클래스 변수: 모든 인스턴스가 공유
    total_count: int = 0
    
    def __init__(self, name: str):
        """
        Counter 인스턴스를 초기화한다
        
        Args:
            name: 카운터 이름
        """
        # 인스턴스 변수: 각 인스턴스마다 독립적
        self.name = name
        self.count = 0
        
        # 클래스 변수 증가
        Counter.total_count += 1
    
    def increment(self) -> None:
        """개별 카운터를 증가시킨다"""
        self.count += 1
    
    def get_info(self) -> str:
        """카운터 정보를 반환한다"""
        return f"{self.name}: {self.count} (전체: {Counter.total_count})"


# ========================================
# 2. BankAccount 클래스 - 인스턴스 메서드
# ========================================

class BankAccount:
    """은행 계좌 클래스"""
    
    # 클래스 변수: 이자율 (모든 계좌에 동일 적용)
    interest_rate: float = 0.03
    
    def __init__(self, owner: str, balance: int = 0):
        """
        BankAccount 인스턴스를 초기화한다
        
        Args:
            owner: 계좌 소유자
            balance: 초기 잔액 (기본값: 0)
        """
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: int) -> None:
        """
        입금한다
        
        Args:
            amount: 입금액
        """
        if amount <= 0:
            print("입금액은 0보다 커야 한다")
            return
        
        self.balance += amount
        print(f"{amount:,}원 입금 완료. 잔액: {self.balance:,}원")
    
    def withdraw(self, amount: int) -> bool:
        """
        출금한다
        
        Args:
            amount: 출금액
        
        Returns:
            출금 성공 여부
        """
        if amount <= 0:
            print("출금액은 0보다 커야 한다")
            return False
        
        if amount > self.balance:
            print(f"잔액 부족. 현재 잔액: {self.balance:,}원")
            return False
        
        self.balance -= amount
        print(f"{amount:,}원 출금 완료. 잔액: {self.balance:,}원")
        return True
    
    def get_balance(self) -> int:
        """
        잔액을 조회한다
        
        Returns:
            현재 잔액
        """
        return self.balance
    
    def apply_interest(self) -> None:
        """이자를 적용한다"""
        interest = int(self.balance * self.interest_rate)
        self.balance += interest
        print(f"이자 {interest:,}원 적용. 잔액: {self.balance:,}원")
    
    def get_info(self) -> str:
        """
        계좌 정보를 반환한다
        
        Returns:
            계좌 정보 문자열
        """
        return f"[{self.owner}] 잔액: {self.balance:,}원"


# ========================================
# 3. 클래스 메서드 (@classmethod)
# ========================================

class Person:
    """사람 클래스 - 클래스 메서드를 활용한다"""
    
    # 클래스 변수
    population: int = 0
    
    def __init__(self, name: str, age: int):
        """
        Person 인스턴스를 초기화한다
        
        Args:
            name: 이름
            age: 나이
        """
        self.name = name
        self.age = age
        Person.population += 1
    
    @classmethod
    def get_population(cls) -> int:
        """
        총 인구를 반환한다 (클래스 메서드)
        
        Returns:
            총 인구
        """
        return cls.population
    
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        """
        출생 연도로부터 Person 인스턴스를 생성한다 (팩토리 메서드)
        
        Args:
            name: 이름
            birth_year: 출생 연도
        
        Returns:
            Person 인스턴스
        """
        current_year = 2024
        age = current_year - birth_year
        return cls(name, age)
    
    def get_info(self) -> str:
        """개인 정보를 반환한다"""
        return f"{self.name} ({self.age}세)"


# ========================================
# 4. 정적 메서드 (@staticmethod)
# ========================================

class MathUtils:
    """수학 유틸리티 클래스 - 정적 메서드를 활용한다"""
    
    @staticmethod
    def is_even(number: int) -> bool:
        """
        짝수인지 확인한다
        
        Args:
            number: 확인할 숫자
        
        Returns:
            짝수 여부
        """
        return number % 2 == 0
    
    @staticmethod
    def is_positive(number: int) -> bool:
        """
        양수인지 확인한다
        
        Args:
            number: 확인할 숫자
        
        Returns:
            양수 여부
        """
        return number > 0
    
    @staticmethod
    def calculate_average(numbers: list[int]) -> float:
        """
        평균을 계산한다
        
        Args:
            numbers: 숫자 리스트
        
        Returns:
            평균값
        """
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)


# ========================================
# 5. 모든 메서드를 활용하는 클래스
# ========================================

class Employee:
    """직원 클래스 - 인스턴스/클래스/정적 메서드를 모두 활용한다"""
    
    # 클래스 변수
    company_name: str = "테크 코퍼레이션"
    employee_count: int = 0
    min_salary: int = 30000000
    
    def __init__(self, name: str, position: str, salary: int):
        """
        Employee 인스턴스를 초기화한다
        
        Args:
            name: 이름
            position: 직급
            salary: 연봉
        """
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1
    
    # 인스턴스 메서드
    def give_raise(self, amount: int) -> None:
        """
        연봉을 인상한다
        
        Args:
            amount: 인상액
        """
        self.salary += amount
        print(f"{self.name}의 연봉이 {amount:,}원 인상되었다")
    
    def get_info(self) -> str:
        """직원 정보를 반환한다"""
        return f"{self.name} ({self.position}) - {self.salary:,}원"
    
    # 클래스 메서드
    @classmethod
    def get_employee_count(cls) -> int:
        """
        총 직원 수를 반환한다
        
        Returns:
            총 직원 수
        """
        return cls.employee_count
    
    @classmethod
    def set_company_name(cls, name: str) -> None:
        """
        회사명을 변경한다
        
        Args:
            name: 새 회사명
        """
        cls.company_name = name
        print(f"회사명이 '{name}'으로 변경되었다")
    
    # 정적 메서드
    @staticmethod
    def validate_salary(salary: int) -> bool:
        """
        연봉이 유효한지 확인한다
        
        Args:
            salary: 확인할 연봉
        
        Returns:
            유효 여부
        """
        return salary >= Employee.min_salary
    
    @staticmethod
    def calculate_tax(salary: int) -> int:
        """
        세금을 계산한다 (간소화된 버전)
        
        Args:
            salary: 연봉
        
        Returns:
            세금
        """
        tax_rate = 0.1  # 10%
        return int(salary * tax_rate)


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. 인스턴스 변수 vs 클래스 변수")
    print("=" * 60)
    
    counter1 = Counter("카운터1")
    counter2 = Counter("카운터2")
    counter3 = Counter("카운터3")
    
    print(f"\n[초기 상태]")
    print(f"총 카운터 개수: {Counter.total_count}")
    print(f"{counter1.get_info()}")
    print(f"{counter2.get_info()}")
    print(f"{counter3.get_info()}")
    
    print(f"\n[카운터1만 증가]")
    counter1.increment()
    counter1.increment()
    print(f"{counter1.get_info()}")
    print(f"{counter2.get_info()}")  # 영향 없음
    
    print("\n" + "=" * 60)
    print("2. BankAccount 클래스 - 인스턴스 메서드")
    print("=" * 60)
    
    # 계좌 생성
    account1 = BankAccount("김철수", 1000000)
    account2 = BankAccount("이영희")
    
    print(f"\n[초기 상태]")
    print(account1.get_info())
    print(account2.get_info())
    
    # 입금
    print(f"\n[김철수 계좌 입금]")
    account1.deposit(500000)
    
    # 출금
    print(f"\n[김철수 계좌 출금]")
    account1.withdraw(300000)
    
    # 출금 실패
    print(f"\n[잔액 부족]")
    account1.withdraw(2000000)
    
    # 이자 적용
    print(f"\n[이자 적용]")
    account1.apply_interest()
    
    # 이영희 계좌 입금
    print(f"\n[이영희 계좌 입금]")
    account2.deposit(2000000)
    
    print(f"\n[최종 상태]")
    print(account1.get_info())
    print(account2.get_info())
    
    print("\n" + "=" * 60)
    print("3. 클래스 메서드 (@classmethod)")
    print("=" * 60)
    
    # 일반 생성자
    person1 = Person("김철수", 30)
    person2 = Person("이영희", 25)
    
    # 팩토리 메서드 (클래스 메서드)
    person3 = Person.from_birth_year("박민수", 1995)
    
    print(f"\n[생성된 사람들]")
    print(f"1. {person1.get_info()}")
    print(f"2. {person2.get_info()}")
    print(f"3. {person3.get_info()}")
    
    # 클래스 메서드로 총 인구 확인
    print(f"\n[총 인구]")
    print(f"총 인구: {Person.get_population()}명")
    
    print("\n" + "=" * 60)
    print("4. 정적 메서드 (@staticmethod)")
    print("=" * 60)
    
    # 인스턴스 생성 없이 사용 가능
    print(f"\n[짝수 확인]")
    print(f"10은 짝수? {MathUtils.is_even(10)}")
    print(f"7은 짝수? {MathUtils.is_even(7)}")
    
    print(f"\n[양수 확인]")
    print(f"5는 양수? {MathUtils.is_positive(5)}")
    print(f"-3은 양수? {MathUtils.is_positive(-3)}")
    
    print(f"\n[평균 계산]")
    numbers = [10, 20, 30, 40, 50]
    avg = MathUtils.calculate_average(numbers)
    print(f"{numbers}의 평균: {avg}")
    
    print("\n" + "=" * 60)
    print("5. 모든 메서드를 활용하는 클래스")
    print("=" * 60)
    
    # 직원 생성
    emp1 = Employee("김철수", "대리", 40000000)
    emp2 = Employee("이영희", "과장", 50000000)
    emp3 = Employee("박민수", "부장", 60000000)
    
    print(f"\n[직원 목록]")
    print(f"회사: {Employee.company_name}")
    print(f"1. {emp1.get_info()}")
    print(f"2. {emp2.get_info()}")
    print(f"3. {emp3.get_info()}")
    
    # 클래스 메서드
    print(f"\n[클래스 메서드 활용]")
    print(f"총 직원 수: {Employee.get_employee_count()}명")
    
    Employee.set_company_name("글로벌 테크")
    print(f"변경된 회사명: {Employee.company_name}")
    
    # 정적 메서드
    print(f"\n[정적 메서드 활용]")
    test_salary = 35000000
    print(f"연봉 {test_salary:,}원은 유효? {Employee.validate_salary(test_salary)}")
    print(f"세금: {Employee.calculate_tax(test_salary):,}원")
    
    # 인스턴스 메서드
    print(f"\n[연봉 인상]")
    emp1.give_raise(5000000)
    print(f"인상 후: {emp1.get_info()}")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)
    print("\n메서드 종류:")
    print("- 인스턴스 메서드: self를 받음, 인스턴스 상태에 접근")
    print("- 클래스 메서드: cls를 받음, 클래스 변수에 접근")
    print("- 정적 메서드: self/cls 없음, 유틸리티 함수")

