"""
Chapter 3-1: 접근 제어의 이해
파이썬의 Public, Protected, Private 속성을 학습한다.
"""


# ========================================
# 1. Public, Protected, Private 비교
# ========================================

class AccessLevelDemo:
    """접근 수준을 보여주는 데모 클래스"""
    
    def __init__(self):
        """다양한 접근 수준의 속성을 초기화한다"""
        # Public: 어디서든 접근 가능
        self.public_var = "누구나 접근 가능"
        
        # Protected: 내부 구현 (관례상 접근 자제)
        self._protected_var = "내부 구현 (접근 자제)"
        
        # Private: Name Mangling 적용
        self.__private_var = "Private (Name Mangling)"
    
    def get_all_vars(self) -> dict[str, str]:
        """
        모든 변수에 접근하여 반환한다
        클래스 내부에서는 모두 접근 가능하다
        
        Returns:
            모든 변수 딕셔너리
        """
        return {
            "public": self.public_var,
            "protected": self._protected_var,
            "private": self.__private_var
        }


# ========================================
# 2. Employee 클래스
# ========================================

class Employee:
    """직원 클래스 - 다양한 접근 수준의 정보를 가진다"""
    
    def __init__(self, name: str, department: str, salary: int, ssn: str):
        """
        Employee 인스턴스를 초기화한다
        
        Args:
            name: 이름 (공개 정보)
            department: 부서 (공개 정보)
            salary: 연봉 (내부 정보)
            ssn: 주민번호 (민감 정보)
        """
        # Public: 공개 정보
        self.name = name
        self.department = department

        # Protected: 내부 정보 (외부에서 접근 자제)
        self._salary = salary
        
        # Private: 민감 정보 (Name Mangling 적용)
        self.__ssn = ssn
    
    def get_public_info(self) -> str:
        """
        공개 가능한 정보를 반환한다
        
        Returns:
            공개 정보 문자열
        """
        return f"{self.name} - {self.department}"
    
    def get_salary_info(self) -> str:
        """
        연봉 정보를 반환한다 (내부 메서드)
        
        Returns:
            연봉 정보 문자열
        """
        return f"연봉: {self._salary:,}원"
    
    def _calculate_tax(self) -> int:
        """
        세금을 계산한다 (내부 메서드)
        
        Returns:
            세금
        """
        return int(self._salary * 0.1)
    
    def __verify_identity(self, input_ssn: str) -> bool:
        """
        신원을 확인한다 (Private 메서드)
        
        Args:
            input_ssn: 입력받은 주민번호
        
        Returns:
            인증 성공 여부
        """
        return self.__ssn == input_ssn
    
    def authenticate(self, input_ssn: str) -> bool:
        """
        인증을 수행한다 (Public 인터페이스)
        
        Args:
            input_ssn: 입력받은 주민번호
        
        Returns:
            인증 성공 여부
        """
        return self.__verify_identity(input_ssn)


# ========================================
# 3. 상속 시 Name Mangling
# ========================================

class Parent:
    """부모 클래스"""
    
    def __init__(self):
        """부모 클래스를 초기화한다"""
        self.public = "부모의 Public"
        self._protected = "부모의 Protected"
        self.__private = "부모의 private"

    
    def get_private(self) -> str:
        """
        Private 변수를 반환한다

        Returns:
            Private 변수
        """
        return self.__private


class Child(Parent):
    """자식 클래스"""
    
    def __init__(self):
        """자식 클래스를 초기화한다"""
        super().__init__()
        # 자식에서 같은 이름의 Private 변수 정의
        self.__private = "자식의 Private"
    
    def get_child_private(self) -> str:
        """
        자식의 Private 변수를 반환한다
        
        Returns:
            자식의 Private 변수
        """
        return self.__private
    
    def get_protected(self) -> str:
        """
        부모의 Protected 변수에 접근한다
        
        Returns:
            Protected 변수
        """
        return self._protected


# ========================================
# 4. BankAccount 클래스
# ========================================

class BankAccount:
    """은행 계좌 클래스 - 적절한 캡슐화 예제"""
    
    def __init__(self, owner: str, initial_balance: int, password: str):
        """
        BankAccount 인스턴스를 초기화한다
        
        Args:
            owner: 계좌 소유자
            initial_balance: 초기 잔액
            password: 비밀번호
        """
        # Public: 계좌 소유자 (공개 정보)
        self.owner = owner
        
        # Protected: 잔액 (내부에서 관리)
        self._balance = initial_balance
        
        # Private: 비밀번호 (민감 정보)
        self.__password = password
    
    def deposit(self, amount: int) -> None:
        """
        입금한다
        
        Args:
            amount: 입금액
        """
        if amount > 0:
            self._balance += amount
            print(f"{amount:,}원 입금 완료")
    
    def withdraw(self, amount: int, password: str) -> bool:
        """
        출금한다 (비밀번호 확인 필요)
        
        Args:
            amount: 출금액
            password: 비밀번호
        
        Returns:
            출금 성공 여부
        """
        if not self.__check_password(password):
            print("비밀번호가 틀렸다")
            return False
        
        if amount > self._balance:
            print("잔액이 부족하다")
            return False
        
        self._balance -= amount
        print(f"{amount:,}원 출금 완료")
        return True
    
    def get_balance(self, password: str) -> int | None:
        """
        잔액을 조회한다 (비밀번호 확인 필요)
        
        Args:
            password: 비밀번호
        
        Returns:
            잔액 또는 None (인증 실패 시)
        """
        if not self.__check_password(password):
            print("비밀번호가 틀렸다")
            return None
        return self._balance
    
    def __check_password(self, password: str) -> bool:
        """
        비밀번호를 확인한다 (Private 메서드)
        
        Args:
            password: 확인할 비밀번호
        
        Returns:
            비밀번호 일치 여부
        """
        return self.__password == password


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. Public, Protected, Private 비교")
    print("=" * 60)
    
    demo = AccessLevelDemo()
    
    # Public 접근
    print(f"\n[Public 접근]")
    print(f"demo.public_var = {demo.public_var}")
    
    # Protected 접근 (가능하지만 권장하지 않음)
    print(f"\n[Protected 접근 - 가능하지만 권장하지 않음]")
    print(f"demo._protected_var = {demo._protected_var}")
    
    # Private 접근 시도
    print(f"\n[Private 직접 접근 시도]")
    try:
        print(demo.__private_var)
    except AttributeError as e:
        print(f"에러 발생: {e}")
    
    # Name Mangling을 통한 접근 (가능하지만 절대 하지 말 것!)
    print(f"\n[Name Mangling을 통한 접근 - 절대 하지 말 것!]")
    print(f"demo._AccessLevelDemo__private_var = {demo._AccessLevelDemo__private_var}")  # type: ignore[attr-defined]
    
    # 클래스 내부에서는 모두 접근 가능
    print(f"\n[클래스 내부 메서드를 통한 접근]")
    all_vars = demo.get_all_vars()
    for key, value in all_vars.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("2. Name Mangling 확인")
    print("=" * 60)
    
    print(f"\n[dir()로 속성 확인]")
    attrs = [attr for attr in dir(demo) if not attr.startswith('__') or attr.endswith('__')]
    filtered_attrs = [attr for attr in attrs if 'var' in attr.lower() or 'private' in attr.lower()]
    for attr in filtered_attrs:
        print(f"  - {attr}")
    
    print(f"\nPrivate 변수의 실제 이름:")
    print(f"  _AccessLevelDemo__private_var")
    
    print("\n" + "=" * 60)
    print("3. Employee 클래스")
    print("=" * 60)
    
    employee = Employee("김철수", "개발팀", 50000000, "123456-1234567")
    
    # Public 정보 접근
    print(f"\n[Public 정보 접근]")
    print(f"이름: {employee.name}")
    print(f"부서: {employee.department}")
    print(f"공개 정보: {employee.get_public_info()}")
    
    # Protected 정보 접근 (가능하지만 권장하지 않음)
    print(f"\n[Protected 정보 접근 - 가능하지만 권장하지 않음]")
    print(f"연봉: {employee._salary:,}원")
    print(f"세금: {employee._calculate_tax():,}원")
    
    # Private 정보 접근 시도
    print(f"\n[Private 정보 직접 접근 시도]")
    try:
        print(employee.__ssn)
    except AttributeError as e:
        print(f"에러 발생: AttributeError")
    
    # Public 인터페이스를 통한 인증
    print(f"\n[Public 인터페이스를 통한 인증]")
    print(f"올바른 주민번호: {employee.authenticate('123456-1234567')}")
    print(f"잘못된 주민번호: {employee.authenticate('000000-0000000')}")
    
    print("\n" + "=" * 60)
    print("4. 상속 시 Name Mangling")
    print("=" * 60)
    
    child = Child()
    
    print(f"\n[Public과 Protected는 상속됨]")
    print(f"child.public = {child.public}")
    print(f"child._protected = {child.get_protected()}")
    
    print(f"\n[Private는 Name Mangling으로 분리됨]")
    print(f"부모의 Private: {child.get_private()}")
    print(f"자식의 Private: {child.get_child_private()}")
    
    print(f"\n[Name Mangling 확인]")
    private_attrs = [attr for attr in dir(child) if 'private' in attr.lower()]
    for attr in private_attrs:
        print(f"  - {attr}")
    
    print("\n" + "=" * 60)
    print("5. BankAccount 클래스 - 적절한 캡슐화")
    print("=" * 60)
    
    account = BankAccount("이영희", 1000000, "1234")
    
    print(f"\n[공개 정보]")
    print(f"계좌 소유자: {account.owner}")
    
    print(f"\n[잔액 조회 - 비밀번호 필요]")
    balance = account.get_balance("1234")
    if balance is not None:
        print(f"현재 잔액: {balance:,}원")
    
    # 잘못된 비밀번호
    print(f"\n[잘못된 비밀번호]")
    balance = account.get_balance("0000")
    
    print(f"\n[입금]")
    account.deposit(500000)
    
    print(f"\n[출금 - 비밀번호 필요]")
    account.withdraw(300000, "1234")
    
    print(f"\n[최종 잔액]")
    balance = account.get_balance("1234")
    if balance is not None:
        print(f"현재 잔액: {balance:,}원")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)
    print("\n파이썬의 접근 제어 철학:")
    print("- Public: 자유롭게 사용")
    print("- Protected (_): 내부 구현, 접근 자제")
    print("- Private (__): Name Mangling, 신중히 사용")
    print("- '우리는 모두 책임감 있는 성인이다'")

