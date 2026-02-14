"""
Chapter 5-5: DIP (의존 역전 원칙)
고수준 모듈은 저수준 모듈에 의존하지 않고, 둘 다 추상화에 의존한다.
"""

from abc import ABC, abstractmethod


# ========================================
# Before: DIP 위반
# ========================================

class EmailSenderBad:
    """이메일 발송 (구체적 클래스)"""
    
    def send(self, message: str) -> None:
        print(f"이메일 발송: {message}")


class NotificationServiceBad:
    """알림 서비스 (나쁜 예 - 구체적 클래스에 의존)"""
    
    def __init__(self):
        self.sender = EmailSenderBad()  # 구체적 클래스에 의존
    
    def notify(self, message: str) -> None:
        self.sender.send(message)


# ========================================
# After: DIP 준수
# ========================================

class MessageSender(ABC):
    """메시지 발송 추상 인터페이스"""
    
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailSender(MessageSender):
    """이메일 발송"""
    
    def send(self, message: str) -> None:
        print(f"이메일 발송: {message}")


class SMSSender(MessageSender):
    """SMS 발송"""
    
    def send(self, message: str) -> None:
        print(f"SMS 발송: {message}")


class NotificationService:
    """알림 서비스 (좋은 예 - 추상화에 의존)"""
    
    def __init__(self, sender: MessageSender):
        self.sender = sender  # 추상화에 의존
    
    def notify(self, message: str) -> None:
        self.sender.send(message)


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("DIP (의존 역전 원칙)")
    print("=" * 60)
    
    print("\n[After: DIP 준수]")
    
    email_service = NotificationService(EmailSender())
    email_service.notify("이메일로 알림")
    
    sms_service = NotificationService(SMSSender())
    sms_service.notify("SMS로 알림")
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)
    print("\n모든 SOLID 원칙을 학습했다!")

