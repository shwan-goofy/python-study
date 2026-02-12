"""
Chapter 5-2: OCP (개방-폐쇄 원칙)
확장에는 열려 있고, 수정에는 닫혀 있어야 한다.
"""

from abc import ABC, abstractmethod


# ========================================
# Before: OCP 위반
# ========================================

class ReportGeneratorBad:
    """리포트 생성 (나쁜 예)"""
    
    def generate(self, report_type: str) -> None:
        if report_type == "PDF":
            print("PDF 리포트 생성")
        elif report_type == "Excel":
            print("Excel 리포트 생성")
        # 새로운 형식 추가 시 이 클래스를 수정해야 함


# ========================================
# After: OCP 준수
# ========================================

class ReportGenerator(ABC):
    """리포트 생성 추상 클래스"""
    
    @abstractmethod
    def generate(self) -> None:
        pass


class PDFReport(ReportGenerator):
    """PDF 리포트"""
    
    def generate(self) -> None:
        print("PDF 리포트 생성")


class ExcelReport(ReportGenerator):
    """Excel 리포트"""
    
    def generate(self) -> None:
        print("Excel 리포트 생성")


class HTMLReport(ReportGenerator):
    """HTML 리포트 (새로 추가)"""
    
    def generate(self) -> None:
        print("HTML 리포트 생성")


# ========================================
# 메인 실행
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("OCP (개방-폐쇄 원칙)")
    print("=" * 60)
    
    print("\n[After: OCP 준수]")
    reports: list[ReportGenerator] = [
        PDFReport(),
        ExcelReport(),
        HTMLReport()
    ]
    
    for report in reports:
        report.generate()
    
    print("\n" + "=" * 60)
    print("학습 완료!")
    print("=" * 60)

