# Chapter 2-1: 클래스 정의와 인스턴스화

## 학습 목표

- 클래스(Class)와 객체(Object)의 개념을 이해한다
- 클래스를 정의하고 인스턴스를 생성하는 방법을 배운다
- `__init__` 생성자의 역할을 이해한다
- `self` 키워드의 의미를 명확히 이해한다
- 여러 인스턴스를 생성하고 각각 독립적임을 확인한다

## 핵심 개념

### 1. 클래스(Class)란?

클래스는 객체를 만들기 위한 **설계도**이다. 데이터(속성)와 기능(메서드)을 하나로 묶는다.

```python
class Person:
    pass  # 빈 클래스
```

### 2. 객체(Object)와 인스턴스(Instance)

- **객체(Object)**: 클래스로부터 만들어진 실체
- **인스턴스(Instance)**: 특정 클래스로부터 만들어진 객체

예를 들어, "Person 클래스의 인스턴스"라고 말한다.

```python
person1 = Person()  # Person 클래스의 인스턴스 생성
```

### 3. `__init__` 생성자

객체가 생성될 때 자동으로 호출되는 특별한 메서드다. 객체의 초기 상태를 설정한다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- 첫 번째 매개변수는 항상 `self`다
- 나머지 매개변수는 객체 생성 시 전달받는 값이다

### 4. `self` 키워드

`self`는 **현재 인스턴스 자신**을 가리킨다.

- 인스턴스 변수를 정의할 때: `self.name = name`
- 인스턴스 메서드를 호출할 때: `self.method()`
- 메서드의 첫 번째 매개변수는 관례적으로 `self`다

파이썬은 메서드 호출 시 자동으로 `self`에 현재 인스턴스를 전달한다.

```python
person = Person("Alice", 25)
# 내부적으로 Person.__init__(person, "Alice", 25) 호출
```

### 5. 클래스 네이밍 컨벤션

- **클래스 이름**: PascalCase (각 단어의 첫 글자 대문자)
  - 좋은 예: `Person`, `BankAccount`, `UserProfile`
  - 나쁜 예: `person`, `bank_account`, `userProfile`

### 6. 인스턴스의 독립성

각 인스턴스는 독립적인 데이터를 가진다.

```python
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
# person1과 person2는 완전히 별개의 객체
```

## 실습 예제

example.py에서는 다음을 학습한다:

1. **기본 클래스 정의**
   - 빈 클래스
   - 속성이 있는 클래스

2. **생성자 `__init__`**
   - 매개변수 받기
   - 인스턴스 변수 초기화

3. **여러 인스턴스 생성**
   - 각 인스턴스의 독립성 확인
   - 인스턴스 비교

4. **실전 예제: Person 클래스**
   - 이름, 나이, 이메일 속성
   - 인사 메서드
   - 나이 증가 메서드

## 클래스 vs 인스턴스

| 구분 | 클래스 | 인스턴스 |
|------|--------|----------|
| 정의 | 설계도, 틀 | 설계도로 만든 실체 |
| 개수 | 하나 | 여러 개 가능 |
| 예시 | `Person` | `person1`, `person2` |

## 주의사항

- `__init__`에서 `self` 매개변수를 빼먹으면 안 된다
- 인스턴스 변수는 반드시 `self.`를 붙여야 한다
- 클래스 이름은 PascalCase를 사용한다
- 메서드의 첫 번째 매개변수는 항상 `self`다 (관례)

## 다음 챕터

[Chapter 2-2: 필드와 메서드](../chapter_02_2_fields_methods/)에서는 인스턴스 변수와 클래스 변수의 차이를 배운다.

