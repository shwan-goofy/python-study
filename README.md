# 파이썬 객체지향 마스터 클래스

파이썬 초급 주니어 개발자를 위한 객체지향 프로그래밍 완전 학습 자료다.

## 학습 목표

객체지향 프로그래밍의 핵심 개념을 파이썬으로 이해하고 실무에 적용할 수 있는 능력을 기른다.

## 커리큘럼 구조

**기본기 → 구조화 → 관계 형성 → 원칙 적용**의 4단계 흐름으로 구성된다.

### 1단계: OOP를 위한 파이썬 문법 워밍업

객체를 만들기 전에 필요한 도구들을 정비하는 시간이다.

- **[Chapter 1-1: 파이썬 함수와 스코프](chapter_01_1_function_scope/)**
  - 함수 정의와 인자 전달 방식 (Call by object reference)
  - 전역 변수 vs 지역 변수

- **[Chapter 1-2: Type Hinting 기초](chapter_01_2_type_hinting/)**
  - 동적 타이핑 언어에서의 Type Hinting 필요성
  - 변수, 함수 파라미터 및 반환값 타입 명시
  - typing 모듈 소개

### 2단계: 클래스와 객체의 해부

기본적인 필드와 메서드를 작성하고, 파이썬의 독특한 객체 생성 방식을 익힌다.

- **[Chapter 2-1: 클래스 정의와 인스턴스화](chapter_02_1_class_instance/)**
  - class 키워드와 네이밍 컨벤션
  - 생성자 `__init__`과 `self` 키워드

- **[Chapter 2-2: 필드와 메서드](chapter_02_2_fields_methods/)**
  - 인스턴스 변수와 메서드 작성법
  - 클래스 변수 vs 인스턴스 변수

- **[Chapter 2-3: 매직 메서드](chapter_02_3_magic_methods/)**
  - 객체의 표현: `__str__` vs `__repr__`
  - 연산자 오버로딩

### 3단계: 캡슐화와 파이썬스러운 접근

Java 등 타 언어와 구별되는 파이썬의 Getter/Setter (Property) 방식을 다룬다.

- **[Chapter 3-1: 접근 제어의 이해](chapter_03_1_access_control/)**
  - Public vs Non-public vs Name Mangling
  - 파이썬에 진정한 'Private'이 없는 이유

- **[Chapter 3-2: Getter와 Setter, @property](chapter_03_2_property/)**
  - Java 스타일 Getter/Setter
  - 파이썬의 `@property` 데코레이터
  - 데이터 유효성 검사

### 4단계: 객체 간의 관계

Is-a와 Has-a 관계를 명확히 구분하고 구현한다.

- **[Chapter 4-1: 상속 (Inheritance) - Is-a 관계](chapter_04_1_inheritance/)**
  - 부모 클래스와 자식 클래스
  - `super()` 활용과 메서드 오버라이딩

- **[Chapter 4-2: 합성/집약 (Composition/Aggregation) - Has-a 관계](chapter_04_2_composition/)**
  - 다른 객체를 필드로 가지는 방식
  - 상속의 오용을 피하는 방법

- **[Chapter 4-3: 추상 클래스와 인터페이스](chapter_04_3_abstract/)**
  - abc 모듈 (ABC, abstractmethod)
  - 설계도로서의 클래스 역할

### 5단계: 견고한 소프트웨어를 위한 SOLID 원칙

앞서 배운 문법들이 왜 그렇게 쓰여야 하는지 철학을 배운다.

- **[Chapter 5-1: SRP (단일 책임 원칙)](chapter_05_1_srp/)**
  - 하나의 클래스는 하나의 책임만 가진다

- **[Chapter 5-2: OCP (개방-폐쇄 원칙)](chapter_05_2_ocp/)**
  - 확장에는 열려 있고, 수정에는 닫혀 있어야 한다

- **[Chapter 5-3: LSP (리스코프 치환 원칙)](chapter_05_3_lsp/)**
  - 자식 클래스는 부모 클래스의 역할을 완벽히 대체해야 한다

- **[Chapter 5-4: ISP (인터페이스 분리 원칙)](chapter_05_4_isp/)**
  - 범용 인터페이스 하나보다 구체적인 여러 개가 낫다

- **[Chapter 5-5: DIP (의존 역전 원칙)](chapter_05_5_dip/)**
  - 구체적인 것이 아닌, 추상적인 것에 의존하라

## 환경 설정

### 필요 사항

- Python 3.11 이상
- mypy (타입 체크 도구)

### 설치

```bash
pip install -r requirements.txt
```

## 학습 방법

1. 각 챕터의 README.md를 읽고 개념을 이해한다
2. example.py 코드를 읽고 분석한다
3. 코드를 직접 실행하여 결과를 확인한다
4. 코드를 수정하며 실험한다

### 예제 실행

```bash
python3 chapter_01_1_function_scope/example.py
```

### 타입 체크

```bash
mypy chapter_01_1_function_scope/example.py
```

## 전체 검증

모든 예제가 정상 동작하는지 확인한다:

```bash
# 모든 챕터 실행 검증
for dir in chapter_*/; do
    echo "Testing $dir"
    python3 "${dir}example.py" || exit 1
done

# 모든 챕터 타입 검증
for dir in chapter_*/; do
    echo "Type checking $dir"
    mypy "${dir}example.py" || exit 1
done
```

## 대상 독자

- 파이썬 기초 문법을 알고 있는 주니어 개발자
- 객체지향 프로그래밍을 체계적으로 배우고 싶은 개발자
- 파이썬의 객체지향 특성을 깊이 이해하고 싶은 개발자

## 학습 시간

- 총 15개 챕터
- 챕터당 약 1-2시간
- 전체 과정: 약 20-30시간

