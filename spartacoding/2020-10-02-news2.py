from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles" #시트제목
ws1.append(["제목", "링크", "신문사"])
ws1.append(["제목1", "링크2", "신문사3"])

wb.save(filename='articles.xlsx')