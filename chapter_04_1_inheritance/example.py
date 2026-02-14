"""
Chapter 4-1: 상속 (Inheritance) - Is-a 관계
상속을 통해 코드를 재사용하고 확장한다.
"""


# ========================================
# 1. 기본 상속
# ========================================

class Animal:
    """동물 클래스 (부모)"""
    
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return "..."
    
    def introduce(self) -> str:
        return f"나는 {self.name}이다"


class Dog(Animal):
    """개 클래스 (자식)"""
    
    def speak(self) -> str:
        """메서드 오버라이딩"""
        return "멍멍"


class Cat(Animal):
    """고양이 클래스 (자식)"""
    
    def speak(self) -> str:
        """메서드 오버라이딩"""
        return "야옹"


# ========================================
# 2. super() 활용
# ========================================

class Employee:
    """직원 클래스 (부모)"""
    
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
    
    def get_info(self) -> str:
        return f"{self.name} - {self.salary:,}원"


class Manager(Employee):
    """관리자 클래스 (자식)"""
    
    def __init__(self, name: str, salary: int, team_size: int):
        super().__init__(name, salary)  # 부모 생성자 호출
        self.team_size = team_size
    
    def get_info(self) -> str:
        """메서드 확장"""
        base_info = super().get_info()
        return f"{base_info}, 팀원 {self.team_size}명"


# ========================================
# 3. 다형성 (Polymorphism)
# ========================================

def animal_sound(animal: Animal) -> None:
    """다형성 - 같은 인터페이스로 다른 동작"""
    print(f"{animal.name}: {animal.speak()}")


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. 기본 상속")
    print("=" * 60)
    
    dog = Dog("바둑이")
    cat = Cat("나비")
    
    print(f"\n{dog.introduce()}")
    print(f"{dog.speak()}")
    
    print(f"\n{cat.introduce()}")
    print(f"{cat.speak()}")
    
    print("\n" + "=" * 60)
    print("2. super() 활용")
    print("=" * 60)
    
    employee = Employee("김철수", 40000000)
    manager = Manager("이영희", 60000000, 5)
    
    print(f"\n직원: {employee.get_info()}")
    print(f"관리자: {manager.get_info()}")
    
    print("\n" + "=" * 60)
    print("3. 다형성")
    print("=" * 60)
    
    animals: list[Animal] = [
        Dog("바둑이"),
        Cat("나비"),
        Dog("멍멍이")
    ]
    
    print()
    for animal in animals:
        animal_sound(animal)
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)

