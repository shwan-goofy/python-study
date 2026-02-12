"""
Chapter 4-2: 합성/집약 (Composition/Aggregation) - Has-a 관계
객체를 포함하여 기능을 구현한다.
"""


# ========================================
# 1. 합성 (Composition) - 강한 Has-a
# ========================================

class Engine:
    """엔진 클래스"""
    
    def __init__(self, horsepower: int):
        self.horsepower = horsepower
    
    def start(self) -> str:
        return f"{self.horsepower}마력 엔진 시동"


class Car:
    """자동차 클래스 - 엔진을 소유한다"""
    
    def __init__(self, model: str, horsepower: int):
        self.model = model
        self.engine = Engine(horsepower)  # 합성
    
    def start(self) -> str:
        return f"{self.model}: {self.engine.start()}"


# ========================================
# 2. 집약 (Aggregation) - 약한 Has-a
# ========================================

class Book:
    """책 클래스"""
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        return f"{self.title} - {self.author}"


class Library:
    """도서관 클래스 - 책들을 관리한다"""
    
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def list_books(self) -> None:
        print(f"\n{self.name} 소장 도서:")
        for i, book in enumerate(self.books, 1):
            print(f"  {i}. {book}")


# ========================================
# 3. 합성 vs 상속
# ========================================

# 잘못된 예: 상속 사용
class Stack(list):  # list를 상속
    """스택 (잘못된 설계)"""
    
    def push(self, item):
        self.append(item)
    
    def pop_stack(self):
        return self.pop()


# 올바른 예: 합성 사용
class StackComposition:
    """스택 (올바른 설계)"""
    
    def __init__(self):
        self._items: list = []  # 합성
    
    def push(self, item) -> None:
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. 합성 (Composition)")
    print("=" * 60)
    
    car1 = Car("소나타", 200)
    car2 = Car("그랜저", 300)
    
    print(f"\n{car1.start()}")
    print(f"{car2.start()}")
    
    print("\n" + "=" * 60)
    print("2. 집약 (Aggregation)")
    print("=" * 60)
    
    book1 = Book("파이썬 코딩의 기술", "브렛 슬라킨")
    book2 = Book("클린 코드", "로버트 C. 마틴")
    
    library = Library("중앙 도서관")
    library.add_book(book1)
    library.add_book(book2)
    
    library.list_books()
    
    print("\n" + "=" * 60)
    print("3. 합성 vs 상속")
    print("=" * 60)
    
    print("\n[합성을 사용한 Stack]")
    stack = StackComposition()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)
    print("\n상속 대신 합성을 선택하는 경우:")
    print("- Is-a 관계가 아닌 Has-a 관계일 때")
    print("- 구현의 일부만 필요할 때")
    print("- 유연성이 필요할 때")

