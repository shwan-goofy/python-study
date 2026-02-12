# Chapter 1-2: Type Hinting (Annotation) 기초

## 학습 목표

- 동적 타이핑 언어에서 Type Hinting의 필요성을 이해한다
- 변수, 함수 파라미터, 반환값에 타입을 명시하는 방법을 배운다
- typing 모듈의 주요 타입(List, Dict, Optional, Union)을 활용한다
- mypy를 사용하여 타입 체크를 수행한다

## 핵심 개념

### 1. Type Hinting이란?

파이썬은 동적 타이핑 언어지만, 코드의 가독성과 유지보수성을 높이기 위해 타입을 명시할 수 있다.

```python
# Type Hinting 없이
def add(a, b):
    return a + b

# Type Hinting 사용
def add(a: int, b: int) -> int:
    return a + b
```

Type Hinting은 **런타임에 영향을 주지 않는다**. 즉, 타입을 잘못 명시해도 실행은 가능하다. 하지만 mypy 같은 정적 타입 체커를 사용하면 타입 오류를 미리 발견할 수 있다.

### 2. 기본 타입 명시

```python
name: str = "Alice"
age: int = 25
height: float = 170.5
is_student: bool = True
```

### 3. 함수 타입 명시

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def calculate(x: int, y: int) -> int:
    return x + y

# 반환값이 없는 경우
def print_message(msg: str) -> None:
    print(msg)
```

### 4. typing 모듈

복잡한 타입을 표현하기 위해 typing 모듈을 사용한다.

#### List, Dict, Tuple

```python
from typing import List, Dict, Tuple

numbers: List[int] = [1, 2, 3]
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
coordinate: Tuple[float, float] = (37.5, 127.0)
```

#### Optional

값이 있거나 None일 수 있는 경우 사용한다.

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    # 사용자를 찾으면 이름을 반환, 못 찾으면 None 반환
    if user_id == 1:
        return "Alice"
    return None
```

`Optional[str]`은 `Union[str, None]`과 동일하다.

#### Union

여러 타입 중 하나를 받을 수 있는 경우 사용한다.

```python
from typing import Union

def process_id(id_value: Union[int, str]) -> str:
    return str(id_value)
```

Python 3.10부터는 `int | str` 문법도 사용 가능하다.

### 5. mypy로 타입 체크

```bash
mypy example.py
```

mypy는 코드를 실행하지 않고 타입 오류를 검사한다.

## 실습 예제

example.py에서는 다음을 학습한다:

1. **기본 타입 명시**
   - 변수 타입 명시
   - 함수 파라미터 및 반환값 타입

2. **typing 모듈 활용**
   - List, Dict, Tuple
   - Optional, Union

3. **학생 성적 관리 시스템**
   - 학생 정보 타입 정의
   - 성적 계산 함수
   - 최고 점수 학생 찾기

## Type Hinting의 장점

1. **코드 가독성 향상**: 함수가 무엇을 받고 무엇을 반환하는지 명확하다
2. **IDE 지원**: 자동완성, 타입 힌트 등이 더 정확하다
3. **버그 조기 발견**: mypy로 실행 전에 타입 오류를 발견할 수 있다
4. **문서화**: 별도의 문서 없이도 타입 정보를 전달한다
5. **리팩토링 안전성**: 타입이 변경되면 영향받는 코드를 쉽게 찾을 수 있다

## 주의사항

- Type Hinting은 런타임에 강제되지 않는다
- 과도한 타입 명시는 코드를 복잡하게 만들 수 있다
- 주요 함수의 인터페이스(public API)에 우선적으로 적용한다
