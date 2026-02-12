# Chapter 2-3: 매직 메서드 (Magic Methods)

## 학습 목표

- 매직 메서드(특별 메서드)의 개념을 이해한다
- 객체의 문자열 표현을 제어하는 `__str__`과 `__repr__`을 구분한다
- 연산자 오버로딩을 통해 직관적인 코드를 작성한다
- 자주 사용되는 매직 메서드들을 활용한다

## 핵심 개념

### 1. 매직 메서드란?

매직 메서드(Magic Method)는 **더블 언더스코어(`__`)**로 시작하고 끝나는 특별한 메서드다. 던더(Dunder) 메서드라고도 부른다.

이들은 파이썬의 내장 동작을 커스터마이징할 수 있게 해준다.

```python
class MyClass:
    def __init__(self):  # 생성자 매직 메서드
        pass
```

### 2. 객체 표현 매직 메서드

#### `__str__`

사용자 친화적인 문자열 표현을 반환한다. `print()` 함수나 `str()` 함수가 호출한다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age}세)"

person = Person("홍길동", 25)
print(person)  # "홍길동 (25세)"
```

#### `__repr__`

개발자를 위한 명확한 문자열 표현을 반환한다. 가능하면 객체를 재생성할 수 있는 코드 형태로 반환한다.

```python
def __repr__(self):
    return f"Person(name='{self.name}', age={self.age})"

# Person(name='홍길동', age=25)
```

### 3. 연산자 오버로딩

#### 산술 연산자

- `__add__(self, other)`: `+` 연산자
- `__sub__(self, other)`: `-` 연산자
- `__mul__(self, other)`: `*` 연산자
- `__truediv__(self, other)`: `/` 연산자

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
v3 = v1 + v2  # __add__ 호출
```

#### 비교 연산자

- `__eq__(self, other)`: `==` 연산자
- `__ne__(self, other)`: `!=` 연산자
- `__lt__(self, other)`: `<` 연산자
- `__le__(self, other)`: `<=` 연산자
- `__gt__(self, other)`: `>` 연산자
- `__ge__(self, other)`: `>=` 연산자

```python
def __eq__(self, other):
    return self.x == other.x and self.y == other.y
```

### 4. 컨테이너 매직 메서드

- `__len__(self)`: `len()` 함수
- `__getitem__(self, key)`: `obj[key]` 인덱싱
- `__setitem__(self, key, value)`: `obj[key] = value` 대입
- `__contains__(self, item)`: `in` 연산자

### 5. 기타 유용한 매직 메서드

- `__call__(self)`: 객체를 함수처럼 호출
- `__bool__(self)`: `bool()` 함수, `if` 문에서의 참/거짓
- `__hash__(self)`: `hash()` 함수, 딕셔너리 키로 사용

## 실습 예제

example.py에서는 다음을 학습한다:

1. **`__str__`과 `__repr__`**
   - 두 메서드의 차이
   - 각각의 활용 시기

2. **Vector2D 클래스**
   - 2차원 벡터 표현
   - 벡터 덧셈, 뺄셈 (`__add__`, `__sub__`)
   - 벡터 비교 (`__eq__`)
   - 벡터 크기 (`__abs__`)

3. **연산자 오버로딩**
   - 직관적인 연산자 사용
   - 체이닝 연산

4. **커스텀 리스트 클래스**
   - 컨테이너 메서드 구현

## 자주 사용되는 매직 메서드

| 메서드 | 설명 | 호출 방식 |
|--------|------|-----------|
| `__init__` | 생성자 | `obj = MyClass()` |
| `__str__` | 문자열 표현 | `str(obj)`, `print(obj)` |
| `__repr__` | 개발자용 표현 | `repr(obj)` |
| `__add__` | 덧셈 | `obj1 + obj2` |
| `__eq__` | 동등 비교 | `obj1 == obj2` |
| `__len__` | 길이 | `len(obj)` |
| `__getitem__` | 인덱싱 | `obj[key]` |

## 주의사항

- 매직 메서드는 명확한 의미를 가져야 한다
- `__add__`는 반드시 덧셈의 의미를 가져야 한다
- 예상치 못한 동작을 하도록 구현하면 안 된다
- `__repr__`은 가능하면 `eval(repr(obj))`로 객체를 재생성할 수 있어야 한다

## 다음 챕터

[Chapter 3-1: 접근 제어의 이해](../chapter_03_1_access_control/)에서는 캡슐화를 배운다.

