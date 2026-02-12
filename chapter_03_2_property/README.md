# Chapter 3-2: Getter와 Setter, @property

## 학습 목표

- Getter와 Setter의 필요성을 이해한다
- Java 스타일의 Getter/Setter를 작성한다
- 파이썬의 `@property` 데코레이터를 활용한다
- 유효성 검사를 추가하는 방법을 배운다

## 핵심 개념

### 1. Getter와 Setter의 필요성

직접 속성에 접근하면 유효성 검사가 불가능하다.

```python
class Person:
    def __init__(self, age):
        self.age = age  # 음수 나이도 가능해짐!
```

### 2. Java 스타일 Getter/Setter

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("나이는 0 이상이어야 한다")
        self._age = age
```

### 3. 파이썬의 @property

속성처럼 접근하되, 내부적으로는 메서드를 호출한다.

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 0 이상이어야 한다")
        self._age = age

person = Person(25)
print(person.age)  # Getter 호출
person.age = 30    # Setter 호출
```

### 4. 읽기 전용 속성

Setter를 정의하지 않으면 읽기 전용이 된다.

```python
@property
def age(self):
    return self._age
# Setter 없음 -> 읽기 전용
```
