"""
Chapter 2-1: 클래스 정의와 인스턴스화
클래스를 정의하고 객체를 생성하는 방법을 학습한다.
"""


# ========================================
# 1. 기본 클래스 정의
# ========================================

class EmptyClass:
    """아무 것도 없는 빈 클래스"""
    pass


class SimpleClass:
    """간단한 속성이 있는 클래스"""
    message: str = "안녕하세요"  # 클래스 레벨 속성


# ========================================
# 2. 생성자 __init__
# ========================================

class Person:
    """사람을 표현하는 클래스"""
    
    def __init__(self, name: str, age: int):
        """
        Person 인스턴스를 초기화한다
        
        Args:
            name: 사람의 이름
            age: 사람의 나이
        """
        # self.name은 인스턴스 변수
        # name은 매개변수
        self.name = name
        self.age = age
        print(f"Person 객체 생성: {self.name} ({self.age}세)")


class Book:
    """책을 표현하는 클래스"""
    
    def __init__(self, title: str, author: str, pages: int, price: int):
        """
        Book 인스턴스를 초기화한다
        
        Args:
            title: 책 제목
            author: 저자
            pages: 페이지 수
            price: 가격
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


# ========================================
# 3. 인스턴스 메서드
# ========================================

class PersonWithMethods:
    """메서드가 있는 Person 클래스"""
    
    def __init__(self, name: str, age: int, email: str):
        """
        인스턴스를 초기화한다
        
        Args:
            name: 이름
            age: 나이
            email: 이메일
        """
        self.name = name
        self.age = age
        self.email = email
    
    def greet(self) -> str:
        """
        인사 메시지를 반환한다
        
        Returns:
            인사 메시지
        """
        return f"안녕하세요! 저는 {self.name}이고, {self.age}세입니다."
    
    def get_info(self) -> str:
        """
        상세 정보를 반환한다
        
        Returns:
            상세 정보 문자열
        """
        return f"이름: {self.name}, 나이: {self.age}, 이메일: {self.email}"
    
    def celebrate_birthday(self) -> None:
        """
        나이를 1 증가시킨다 (생일 축하!)
        """
        self.age += 1
        print(f"{self.name}님, 생일 축하합니다! 이제 {self.age}세입니다.")
    
    def update_email(self, new_email: str) -> None:
        """
        이메일을 업데이트한다
        
        Args:
            new_email: 새로운 이메일 주소
        """
        old_email = self.email
        self.email = new_email
        print(f"이메일 변경: {old_email} → {new_email}")


# ========================================
# 4. 기본값이 있는 생성자
# ========================================

class Product:
    """상품을 표현하는 클래스"""
    
    def __init__(
        self,
        name: str,
        price: int,
        quantity: int = 0,
        category: str = "기타"
    ):
        """
        Product 인스턴스를 초기화한다
        
        Args:
            name: 상품명
            price: 가격
            quantity: 수량 (기본값: 0)
            category: 카테고리 (기본값: "기타")
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def get_total_value(self) -> int:
        """
        총 가치를 계산한다 (가격 × 수량)
        
        Returns:
            총 가치
        """
        return self.price * self.quantity
    
    def display(self) -> None:
        """상품 정보를 출력한다"""
        print(f"[{self.category}] {self.name}: {self.price:,}원 (재고: {self.quantity}개)")


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. 기본 클래스 정의")
    print("=" * 60)
    
    # 빈 클래스 인스턴스 생성
    empty_obj = EmptyClass()
    print(f"\nEmptyClass 인스턴스 생성: {empty_obj}")
    print(f"타입: {type(empty_obj)}")
    
    # 간단한 클래스 인스턴스 생성
    simple_obj = SimpleClass()
    print(f"\nSimpleClass 메시지: {simple_obj.message}")
    
    print("\n" + "=" * 60)
    print("2. 생성자 __init__")
    print("=" * 60)
    
    # Person 인스턴스 생성
    print("\n[Person 인스턴스 생성]")
    person1 = Person("김철수", 25)
    person2 = Person("이영희", 30)
    
    # 속성 접근
    print(f"\nperson1 정보: {person1.name}, {person1.age}세")
    print(f"person2 정보: {person2.name}, {person2.age}세")
    
    # Book 인스턴스 생성
    print("\n[Book 인스턴스 생성]")
    book1 = Book("파이썬 코딩의 기술", "브렛 슬라킨", 400, 30000)
    book2 = Book("클린 코드", "로버트 C. 마틴", 584, 33000)
    
    print(f"\nbook1: {book1.title} - {book1.author} ({book1.pages}쪽)")
    print(f"book2: {book2.title} - {book2.author} ({book2.pages}쪽)")
    
    print("\n" + "=" * 60)
    print("3. 인스턴스의 독립성")
    print("=" * 60)
    
    # 각 인스턴스는 독립적인 데이터를 가진다
    person_a = PersonWithMethods("홍길동", 28, "hong@example.com")
    person_b = PersonWithMethods("김유신", 32, "kim@example.com")
    
    print(f"\n[초기 상태]")
    print(f"person_a: {person_a.get_info()}")
    print(f"person_b: {person_b.get_info()}")
    
    # person_a의 나이만 증가
    print(f"\n[person_a의 생일]")
    person_a.celebrate_birthday()
    
    print(f"\n[변경 후]")
    print(f"person_a: {person_a.get_info()}")
    print(f"person_b: {person_b.get_info()}")  # 변경 안됨!
    
    # 인스턴스 비교
    print(f"\n[인스턴스 비교]")
    print(f"person_a == person_b: {person_a == person_b}")  # False (다른 객체)
    print(f"person_a is person_b: {person_a is person_b}")  # False (다른 객체)
    
    person_c = person_a  # 같은 객체를 참조
    print(f"person_a is person_c: {person_a is person_c}")  # True (같은 객체)
    
    print("\n" + "=" * 60)
    print("4. 인스턴스 메서드 활용")
    print("=" * 60)
    
    user = PersonWithMethods("박민수", 26, "park@example.com")
    
    print(f"\n[초기 정보]")
    print(user.get_info())
    
    print(f"\n[인사]")
    greeting = user.greet()
    print(greeting)
    
    print(f"\n[이메일 변경]")
    user.update_email("minsu.park@newmail.com")
    
    print(f"\n[생일 축하]")
    user.celebrate_birthday()
    
    print(f"\n[최종 정보]")
    print(user.get_info())
    
    print("\n" + "=" * 60)
    print("5. 기본값이 있는 생성자")
    print("=" * 60)
    
    # 모든 인자 전달
    product1 = Product("노트북", 1500000, 5, "전자제품")
    product1.display()
    
    # 일부 인자만 전달 (기본값 사용)
    product2 = Product("마우스", 30000)
    product2.display()
    
    # 키워드 인자로 일부만 지정
    product3 = Product("키보드", 80000, category="전자제품")
    product3.display()
    
    print(f"\n[총 가치 계산]")
    print(f"{product1.name} 총 가치: {product1.get_total_value():,}원")
    print(f"{product2.name} 총 가치: {product2.get_total_value():,}원")
    
    print("\n" + "=" * 60)
    print("6. 여러 인스턴스 관리")
    print("=" * 60)
    
    # 리스트로 여러 인스턴스 관리
    people = [
        PersonWithMethods("김철수", 25, "kim@example.com"),
        PersonWithMethods("이영희", 30, "lee@example.com"),
        PersonWithMethods("박민수", 28, "park@example.com")
    ]
    
    print("\n[전체 사용자 목록]")
    for i, person in enumerate(people, 1):
        print(f"{i}. {person.get_info()}")
    
    print("\n[모두에게 인사]")
    for person in people:
        print(f"  - {person.greet()}")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)
    print("\nself의 역할:")
    print("- self는 현재 인스턴스 자신을 가리킨다")
    print("- 메서드 호출 시 자동으로 전달된다")
    print("- 인스턴스 변수에 접근할 때 self.를 사용한다")

