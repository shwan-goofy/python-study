# Chapter 3-1: 접근 제어의 이해

## 학습 목표

- 파이썬의 접근 제어 방식을 이해한다
- Public, Protected, Private의 차이를 배운다
- Name Mangling의 동작 원리를 이해한다
- 파이썬에서 진정한 'Private'이 없는 이유와 철학을 배운다

## 핵심 개념

### 1. 파이썬의 접근 제어

파이썬은 Java나 C++처럼 엄격한 접근 제어자(`public`, `private`, `protected`)가 없다. 대신 **명명 규칙**을 통해 접근 수준을 나타낸다.

### 2. Public 속성/메서드

일반적인 이름을 가진다. 어디서든 자유롭게 접근 가능하다.

```python
class Person:
    def __init__(self):
        self.name = "홍길동"  # Public
```

### 3. Protected 속성/메서드

언더스코어 하나(`_`)로 시작한다. "내부 구현이니 건드리지 않는 것이 좋다"는 약속이다.

```python
class Person:
    def __init__(self):
        self._age = 25  # Protected (관례상)
```

- 기술적으로는 여전히 접근 가능하다
- 개발자 간의 **약속**이다
- "내부 구현이 변경될 수 있으니 주의하라"는 의미

### 4. Private 속성/메서드

언더스코어 두 개(`__`)로 시작한다. Name Mangling이 적용된다.

```python
class Person:
    def __init__(self):
        self.__ssn = "123456-1234567"  # Private
```

- `_ClassName__attribute` 형태로 이름이 변경된다
- 외부에서 접근하기 어렵게 만든다
- 하지만 **완전히 막지는 못한다**

### 5. Name Mangling

Private 속성은 내부적으로 이름이 변경된다.

```python
class BankAccount:
    def __init__(self):
        self.__password = "1234"

account = BankAccount()
# account.__password  # AttributeError
# account._BankAccount__password  # 접근 가능 (하지만 하지 말 것!)
```

Name Mangling의 목적:
- 자식 클래스에서 실수로 같은 이름을 사용하는 것을 방지
- 진정한 보안 장치가 아님

### 6. 파이썬의 철학: "We are all consenting adults"

파이썬은 "우리는 모두 책임감 있는 성인"이라는 철학을 가진다.

- 개발자를 믿는다
- 강제하기보다는 **관례**로 가이드한다
- 필요하다면 내부 구현에 접근할 수 있는 유연성을 제공한다

### 7. 접근 제어 정리

| 형태 | 의미 | 예시 | 접근 가능 여부 |
|------|------|------|----------------|
| `name` | Public | `self.name` | 어디서든 가능 |
| `_name` | Protected | `self._name` | 가능 (하지만 하지 말 것) |
| `__name` | Private | `self.__name` | 가능 (Name Mangling) |

## 실습 예제

example.py에서는 다음을 학습한다:

1. **Public, Protected, Private 비교**
   - 각 접근 수준의 속성 정의
   - 외부에서 접근 시도

2. **Name Mangling 확인**
   - Private 속성의 실제 이름
   - `dir()` 함수로 속성 확인

3. **Employee 클래스**
   - 공개 정보 (이름, 부서)
   - 내부 정보 (연봉)
   - 민감 정보 (주민번호)

4. **상속 시 Name Mangling**
   - 부모와 자식 클래스에서 같은 이름 사용

## 권장 사항

### Public 사용
- 외부에서 사용하도록 의도된 API
- 문서화된 인터페이스
- 변경 시 하위 호환성 고려 필요

### Protected 사용 (`_`)
- 내부 구현 세부사항
- 하위 클래스에서 사용할 수 있는 속성/메서드
- 외부에서는 사용하지 않는 것이 좋음

### Private 사용 (`__`)
- 클래스 외부에서 절대 접근하지 말아야 할 것
- 이름 충돌을 피하고 싶을 때
- 남용하지 말 것 (대부분 Protected로 충분)

## 주의사항

- Private은 보안 장치가 아니다
- Name Mangling을 우회하여 접근 가능하다
- 과도한 Private 사용은 테스트와 디버깅을 어렵게 만든다
- 대부분의 경우 Protected(`_`)로 충분하다

## 다음 챕터

[Chapter 3-2: Getter와 Setter, @property](../chapter_03_2_property/)에서는 파이썬스러운 속성 접근 방법을 배운다.

