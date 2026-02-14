"""
Chapter 5-3: LSP (리스코프 치환 원칙)
자식 클래스는 부모 클래스를 완벽히 대체할 수 있어야 한다.
"""

from abc import ABC, abstractmethod


# ========================================
# Before: LSP 위반
# ========================================

class Rectangle:
    """직사각형"""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def set_width(self, width: int) -> None:
        self.width = width
    
    def set_height(self, height: int) -> None:
        self.height = height
    
    def get_area(self) -> int:
        return self.width * self.height


class Square(Rectangle):
    """정사각형 (나쁜 예 - LSP 위반)"""
    
    def set_width(self, width: int) -> None:
        self.width = width
        self.height = width  # 부모와 다른 동작
    
    def set_height(self, height: int) -> None:
        self.width = height  # 부모와 다른 동작
        self.height = height


# ========================================
# After: LSP 준수
# ========================================

class Shape(ABC):
    """도형 추상 클래스"""
    
    @abstractmethod
    def get_area(self) -> int:
        pass


class RectangleGood(Shape):
    """직사각형"""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def get_area(self) -> int:
        return self.width * self.height


class SquareGood(Shape):
    """정사각형"""
    
    def __init__(self, side: int):
        self.side = side
    
    def get_area(self) -> int:
        return self.side * self.side


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("LSP (리스코프 치환 원칙)")
    print("=" * 60)
    
    print("\n[After: LSP 준수]")
    shapes: list[Shape] = [
        RectangleGood(4, 5),
        SquareGood(4)
    ]
    
    for shape in shapes:
        print(f"면적: {shape.get_area()}")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)

