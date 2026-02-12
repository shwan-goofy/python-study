"""
Chapter 5-4: ISP (인터페이스 분리 원칙)
클라이언트는 사용하지 않는 인터페이스에 의존하지 않아야 한다.
"""

from abc import ABC, abstractmethod


# ========================================
# Before: ISP 위반
# ========================================

class WorkerBad(ABC):
    """작업자 인터페이스 (나쁜 예)"""
    
    @abstractmethod
    def work(self) -> None:
        pass
    
    @abstractmethod
    def eat(self) -> None:
        pass


# ========================================
# After: ISP 준수
# ========================================

class Workable(ABC):
    """일하는 인터페이스"""
    
    @abstractmethod
    def work(self) -> None:
        pass


class Eatable(ABC):
    """먹는 인터페이스"""
    
    @abstractmethod
    def eat(self) -> None:
        pass


class Human(Workable, Eatable):
    """사람"""
    
    def work(self) -> None:
        print("사람이 일한다")
    
    def eat(self) -> None:
        print("사람이 먹는다")


class Robot(Workable):
    """로봇 - 일만 한다"""
    
    def work(self) -> None:
        print("로봇이 일한다")


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("ISP (인터페이스 분리 원칙)")
    print("=" * 60)
    
    print("\n[After: ISP 준수]")
    human = Human()
    robot = Robot()
    
    human.work()
    human.eat()
    robot.work()
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)

