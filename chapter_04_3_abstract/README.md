# Chapter 4-3: 추상 클래스와 인터페이스

## 학습 목표

- 추상 클래스의 개념을 이해한다
- abc 모듈을 사용하여 추상 클래스를 작성한다
- 인터페이스로서의 클래스 역할을 이해한다

## 핵심 개념

### 1. 추상 클래스

인스턴스를 생성할 수 없는 클래스다. 설계도 역할을 한다.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: int) -> bool:
        pass
```

## 다음 챕터

[Chapter 5-1: SRP (단일 책임 원칙)](../chapter_05_1_srp/)에서는 SOLID 원칙을 배운다.

