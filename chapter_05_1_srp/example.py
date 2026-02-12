"""
Chapter 5-1: SRP (단일 책임 원칙)
하나의 클래스는 하나의 책임만 가진다.
"""


# ========================================
# Before: SRP 위반
# ========================================

class UserServiceBad:
    """여러 책임을 가진 클래스 (나쁜 예)"""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def save_to_db(self) -> None:
        """DB 저장 (책임 1)"""
        print(f"DB에 저장: {self.name}")
    
    def send_email(self) -> None:
        """이메일 발송 (책임 2)"""
        print(f"이메일 발송: {self.email}")


# ========================================
# After: SRP 준수
# ========================================

class User:
    """사용자 데이터만 관리"""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class UserRepository:
    """DB 저장 책임"""
    
    def save(self, user: User) -> None:
        print(f"DB에 저장: {user.name}")


class EmailSender:
    """이메일 발송 책임"""
    
    def send(self, email: str, message: str) -> None:
        print(f"이메일 발송: {email}")


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("SRP (단일 책임 원칙)")
    print("=" * 60)
    
    print("\n[Before: SRP 위반]")
    user_bad = UserServiceBad("김철수", "kim@example.com")
    user_bad.save_to_db()
    user_bad.send_email()
    
    print("\n[After: SRP 준수]")
    user = User("이영희", "lee@example.com")
    repo = UserRepository()
    sender = EmailSender()
    
    repo.save(user)
    sender.send(user.email, "환영합니다")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)

