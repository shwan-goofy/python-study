# Chapter 4-1: 상속 (Inheritance) - Is-a 관계

## 학습 목표

- 상속의 개념과 Is-a 관계를 이해한다
- 부모 클래스와 자식 클래스를 작성한다
- `super()`를 활용하여 부모 메서드를 호출한다
- 메서드 오버라이딩을 구현한다
- 다형성을 활용한다

## 핵심 개념

### 1. 상속 (Inheritance)

기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는 것이다.

```python
class Animal:  # 부모 클래스
    def speak(self):
        pass

class Dog(Animal):  # 자식 클래스
    def speak(self):
        return "멍멍"
```

### 2. Is-a 관계

"Dog **is a** Animal" - 개는 동물이다.

상속은 Is-a 관계를 나타낸다.

## 다음 챕터

[Chapter 4-2: 합성/집약 (Has-a)](../chapter_04_2_composition/)에서는 Has-a 관계를 배운다.

