"""
Chapter 1-2: Type Hinting (Annotation) 기초
파이썬에서 타입을 명시하는 방법을 학습한다.
"""

from typing import List, Dict, Tuple, Optional, Union


# ========================================
# 1. 기본 타입 명시
# ========================================

# 변수 타입 명시
name: str = "홍길동"
age: int = 25
height: float = 175.5
is_student: bool = True


def greet_user(name: str) -> str:
    """
    사용자에게 인사하는 함수
    
    Args:
        name: 사용자 이름
    
    Returns:
        인사 메시지
    """
    return f"안녕하세요, {name}님!"


def add_numbers(x: int, y: int) -> int:
    """
    두 정수를 더하는 함수
    
    Args:
        x: 첫 번째 정수
        y: 두 번째 정수
    
    Returns:
        두 정수의 합
    """
    return x + y


def print_message(msg: str) -> None:
    """
    메시지를 출력하는 함수 (반환값 없음)
    
    Args:
        msg: 출력할 메시지
    """
    print(f"메시지: {msg}")


# ========================================
# 2. typing 모듈 활용
# ========================================

def sum_list(numbers: List[int]) -> int:
    """
    정수 리스트의 합을 계산한다
    
    Args:
        numbers: 정수 리스트
    
    Returns:
        리스트의 총합
    """
    total: int = 0
    for num in numbers:
        total += num
    return total


def get_scores(students: Dict[str, int]) -> List[int]:
    """
    학생 점수 딕셔너리에서 점수 리스트를 추출한다
    
    Args:
        students: {학생명: 점수} 딕셔너리
    
    Returns:
        점수 리스트
    """
    return list(students.values())


def get_coordinate() -> Tuple[float, float]:
    """
    좌표를 반환한다
    
    Returns:
        (위도, 경도) 튜플
    """
    latitude: float = 37.5665
    longitude: float = 126.9780
    return (latitude, longitude)


def find_student(student_id: int, students: Dict[int, str]) -> Optional[str]:
    """
    학생 ID로 학생 이름을 찾는다
    
    Args:
        student_id: 학생 ID
        students: {학생ID: 학생명} 딕셔너리
    
    Returns:
        학생 이름 또는 None (찾지 못한 경우)
    """
    return students.get(student_id)


def process_id(id_value: Union[int, str]) -> str:
    """
    ID를 문자열로 변환한다
    여러 타입을 받을 수 있다
    
    Args:
        id_value: 정수 또는 문자열 ID
    
    Returns:
        문자열 ID
    """
    return str(id_value)


# ========================================
# 3. 실전 예제: 학생 성적 관리 시스템
# ========================================

# 학생 정보 타입: (이름, 수학, 영어, 과학)
StudentInfo = Tuple[str, int, int, int]


def create_student(name: str, math: int, english: int, science: int) -> StudentInfo:
    """
    학생 정보를 생성한다
    
    Args:
        name: 학생 이름
        math: 수학 점수
        english: 영어 점수
        science: 과학 점수
    
    Returns:
        학생 정보 튜플
    """
    return (name, math, english, science)


def calculate_average(student: StudentInfo) -> float:
    """
    학생의 평균 점수를 계산한다
    
    Args:
        student: 학생 정보 (이름, 수학, 영어, 과학)
    
    Returns:
        평균 점수
    """
    name, math, english, science = student
    return (math + english + science) / 3


def calculate_all_averages(students: List[StudentInfo]) -> Dict[str, float]:
    """
    모든 학생의 평균 점수를 계산한다
    
    Args:
        students: 학생 정보 리스트
    
    Returns:
        {학생명: 평균점수} 딕셔너리
    """
    result: Dict[str, float] = {}
    for student in students:
        name = student[0]
        avg = calculate_average(student)
        result[name] = avg
    return result


def find_top_student(students: List[StudentInfo]) -> Optional[StudentInfo]:
    """
    최고 평균 점수를 가진 학생을 찾는다
    
    Args:
        students: 학생 정보 리스트
    
    Returns:
        최고 점수 학생 정보 또는 None (학생이 없는 경우)
    """
    if not students:
        return None
    
    top_student: StudentInfo = students[0]
    top_average: float = calculate_average(top_student)
    
    for student in students[1:]:
        avg = calculate_average(student)
        if avg > top_average:
            top_student = student
            top_average = avg
    
    return top_student


def get_students_above_threshold(
    students: List[StudentInfo],
    threshold: float
) -> List[str]:
    """
    기준 점수 이상인 학생들의 이름을 반환한다
    
    Args:
        students: 학생 정보 리스트
        threshold: 기준 점수
    
    Returns:
        기준 점수 이상인 학생 이름 리스트
    """
    result: List[str] = []
    for student in students:
        name = student[0]
        avg = calculate_average(student)
        if avg >= threshold:
            result.append(name)
    return result


def format_student_info(student: StudentInfo) -> str:
    """
    학생 정보를 포맷팅한다
    
    Args:
        student: 학생 정보
    
    Returns:
        포맷팅된 문자열
    """
    name, math, english, science = student
    avg = calculate_average(student)
    return f"{name}: 수학={math}, 영어={english}, 과학={science}, 평균={avg:.1f}"


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 50)
    print("1. 기본 타입 명시")
    print("=" * 50)
    
    print(f"\n변수들:")
    print(f"name: {name} (타입: {type(name).__name__})")
    print(f"age: {age} (타입: {type(age).__name__})")
    print(f"height: {height} (타입: {type(height).__name__})")
    print(f"is_student: {is_student} (타입: {type(is_student).__name__})")
    
    greeting: str = greet_user("김철수")
    print(f"\n{greeting}")
    
    result: int = add_numbers(10, 20)
    print(f"10 + 20 = {result}")
    
    print_message("타입 힌팅 테스트")
    
    print("\n" + "=" * 50)
    print("2. typing 모듈 활용")
    print("=" * 50)
    
    # List
    number_list: List[int] = [1, 2, 3, 4, 5]
    total: int = sum_list(number_list)
    print(f"\n리스트 {number_list}의 합: {total}")
    
    # Dict
    student_scores: Dict[str, int] = {
        "Alice": 90,
        "Bob": 85,
        "Charlie": 95
    }
    scores: List[int] = get_scores(student_scores)
    print(f"학생 점수: {student_scores}")
    print(f"점수 리스트: {scores}")
    
    # Tuple
    coord: Tuple[float, float] = get_coordinate()
    print(f"좌표: 위도={coord[0]}, 경도={coord[1]}")
    
    # Optional
    student_db: Dict[int, str] = {
        1: "김철수",
        2: "이영희",
        3: "박민수"
    }
    found: Optional[str] = find_student(2, student_db)
    print(f"\n학생 ID 2: {found}")
    
    not_found: Optional[str] = find_student(99, student_db)
    print(f"학생 ID 99: {not_found}")
    
    # Union
    id1: str = process_id(12345)
    id2: str = process_id("USER-999")
    print(f"\nID 처리: {id1}, {id2}")
    
    print("\n" + "=" * 50)
    print("3. 실전 예제: 학생 성적 관리 시스템")
    print("=" * 50)
    
    # 학생 정보 생성
    students: List[StudentInfo] = [
        create_student("김철수", 85, 90, 88),
        create_student("이영희", 92, 88, 95),
        create_student("박민수", 78, 82, 80),
        create_student("최지은", 95, 93, 97),
        create_student("정대현", 88, 85, 90)
    ]
    
    print("\n전체 학생 정보:")
    for student in students:
        print(f"  {format_student_info(student)}")
    
    # 평균 점수 계산
    averages: Dict[str, float] = calculate_all_averages(students)
    print("\n평균 점수:")
    for name, avg in averages.items():
        print(f"  {name}: {avg:.1f}점")
    
    # 최고 점수 학생
    top: Optional[StudentInfo] = find_top_student(students)
    if top:
        print(f"\n최고 점수 학생:")
        print(f"  {format_student_info(top)}")
    
    # 기준 점수 이상 학생
    threshold: float = 90.0
    excellent_students: List[str] = get_students_above_threshold(students, threshold)
    print(f"\n평균 {threshold}점 이상 학생:")
    for name in excellent_students:
        print(f"  - {name}")
    
    print("\n" + "=" * 50)
    print("학습 완료!")
    print("타입 체크: mypy chapter_01_2_type_hinting/example.py")
    print("=" * 50)

