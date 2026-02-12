# Chapter 2-2: 필드(Fields)와 메서드(Methods)

## 학습 목표

- 인스턴스 변수(Instance Variable)와 클래스 변수(Class Variable)의 차이를 이해한다
- 인스턴스 메서드, 클래스 메서드, 정적 메서드를 구분한다
- 각 변수와 메서드의 적절한 사용 시기를 배운다
- 실전 예제(BankAccount)로 메서드를 활용한다

## 핵심 개념

### 1. 인스턴스 변수 (Instance Variable)

각 인스턴스마다 독립적으로 존재하는 변수다. `__init__` 내에서 `self.`로 정의한다.

```python
class Person:
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
```

### 2. 클래스 변수 (Class Variable)

클래스에 속하며 모든 인스턴스가 공유하는 변수다. 클래스 본문에 직접 정의한다.

```python
class Person:
    species = "Homo sapiens"  # 클래스 변수
    
    def __init__(self, name):
        self.name = name
```

### 3. 인스턴스 변수 vs 클래스 변수

| 구분 | 인스턴스 변수 | 클래스 변수 |
|------|---------------|-------------|
| 소속 | 각 인스턴스 | 클래스 |
| 공유 | 독립적 | 모든 인스턴스가 공유 |
| 정의 위치 | `__init__` 내부 | 클래스 본문 |
| 접근 | `self.변수명` | `클래스명.변수명` 또는 `self.변수명` |

### 4. 인스턴스 메서드 (Instance Method)

가장 일반적인 메서드다. 첫 번째 매개변수로 `self`를 받는다.

```python
class BankAccount:
    def deposit(self, amount):  # 인스턴스 메서드
        self.balance += amount
```

- 인스턴스 변수에 접근 가능
- 클래스 변수에도 접근 가능
- 특정 인스턴스의 상태를 변경할 때 사용

### 5. 클래스 메서드 (Class Method)

`@classmethod` 데코레이터를 사용하고, 첫 번째 매개변수로 `cls`를 받는다.

```python
class BankAccount:
    interest_rate = 0.03
    
    @classmethod
    def set_interest_rate(cls, rate):  # 클래스 메서드
        cls.interest_rate = rate
```

- 클래스 변수에 접근 가능
- 인스턴스 변수에는 접근 불가
- 팩토리 메서드 패턴에 자주 사용

### 6. 정적 메서드 (Static Method)

`@staticmethod` 데코레이터를 사용하고, `self`나 `cls`를 받지 않는다.

```python
class BankAccount:
    @staticmethod
    def validate_amount(amount):  # 정적 메서드
        return amount > 0
```

- 인스턴스 변수와 클래스 변수 모두 접근 불가
- 유틸리티 함수로 사용
- 클래스와 논리적으로 관련은 있지만 상태를 변경하지 않는 기능

## 실습 예제

example.py에서는 다음을 학습한다:

1. **인스턴스 변수 vs 클래스 변수**
   - 독립성과 공유 확인
   - 클래스 변수의 변경이 모든 인스턴스에 영향

2. **BankAccount 클래스**
   - 잔액 관리 (인스턴스 변수)
   - 입금/출금 메서드
   - 잔액 조회

3. **클래스 메서드 활용**
   - 팩토리 메서드
   - 클래스 변수 관리

4. **정적 메서드 활용**
   - 유효성 검사
   - 유틸리티 함수

## 언제 무엇을 사용할까?

### 인스턴스 변수
- 각 객체마다 다른 값을 가져야 할 때
- 예: 사람의 이름, 계좌의 잔액

### 클래스 변수
- 모든 인스턴스가 공유해야 하는 값
- 예: 종(species), 이자율, 인스턴스 개수

### 인스턴스 메서드
- 특정 인스턴스의 상태를 조회하거나 변경할 때
- 예: 입금, 출금, 정보 조회

### 클래스 메서드
- 클래스 변수를 조회하거나 변경할 때
- 대체 생성자(팩토리 메서드)를 만들 때
- 예: 이자율 설정, from_dict() 생성자

### 정적 메서드
- 클래스나 인스턴스의 상태와 무관한 유틸리티 함수
- 예: 유효성 검사, 포맷 변환

## 주의사항

- 클래스 변수를 변경할 때는 `self.변수명`이 아닌 `클래스명.변수명`을 사용한다
- `self.클래스변수 = 값`은 인스턴스 변수를 새로 만드는 것이다
- 메서드 내에서 인스턴스 변수에 접근하려면 반드시 `self.`를 사용한다

## 다음 챕터

[Chapter 2-3: 매직 메서드](../chapter_02_3_magic_methods/)에서는 특별한 메서드들을 배운다.

