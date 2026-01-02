from models import Book
from models import Member
from models import Library
import utils

"""
Library 구현 시스템 구현을 위한 csv파일 목록 초기화
"""

print("[System] 도서관의 목록을 구성합니다.")
my_library = Library()
print("[system] 도서관의 목록이 갱신되었습니다..")
file_path = "books.csv"
my_library.set_book(file_path)

"""
프로그램의 동작 while문 사용하여 매뉴 선택
"""
while True:
  print('=======================================================')
  print('1. 도서 등록')
  print('2. 도서 목록')
  print('3. 회원 등록')
  print('4. 도서 대출')
  print('5. 도서 반납')
  print('6. 도서 검색')
  print('7. 프로그램 종료')

  userInput = int(input("메뉴를 선택하세요 : "))

  if userInput== 1:
      print("도서등록 매뉴입니다. 도서를 등록하기 위해서는 도서의 이름, 저자, ISBN이 필요합니다.")
      book_name = input("도서의 이름을 입력해 주세요 : ")
      book_author = input("도서의 저자를 입력해 주세요 : ")
      book_isbn = input("도서의 ISBN을 입력해 주세요 : ")

      my_book = Book(book_name,book_author,book_isbn)
      print(f"{my_book.title}: 도서의 이름 입니다. {my_book.author}: 도서의 저자입니다. {my_book.isbn} 도서의 isbn 입니다")
      my_library.add_book(my_book)
      my_library.show_library()
      print("[system] 도서관의 목록이 갱신되었습니다..")

      # # 입력한 책의 정보를 저장할지 말지 한번 더 물어보는 항목을 만들지 말지 고민중
      # check = input("해당 책의 정보를 도서관에 저장하시겠습니까? (yes/no) 로 입력하세요")
      # if check.lower() == "yes":
      #
      break


  elif int(userInput)== 2:
      print("도서 출력 메뉴 입니다. 도서관에 소장하고 있는 모든 목록을 불러옵니다.")
      my_library.show_library()

  elif userInput== 3:
      print("회원 등록 매뉴입니다. 회원 이름과, 전화 번호를 입력하세요")
      name = input("회원 이름을 입력하세요 : ")
      phone = input("회원 전화번호를 입력하세요 : ")

      my_member = Member(name, phone)
      my_library.add_member(my_member)

      print(f"{my_library.show_member()}")

      # my_member =Member("김동균","111-1111-1111")
      # my_member.add_book(my_book)
      # my_member.add_book(my_book2)
      # my_member.add_book(my_book3)
      # my_member.show_book()

      # my_member["borrowed_book"].append(my_book)
      #
      # print(f"{my_member.get("name")} : {my_member['borrowed_book'].get('title')} ")
      #

  elif userInput== 4:
      print("도서 대출 매뉴입니다, 책을 대출하려면 회원이름과, 대출할 책의 isbn을 입력해 주세요")
      member_name = input("회원의 이름을 입력하세요 : ")
      book_isbn = input("대출할 책의 isbn을 입력하세요 :")

      #
      # if not my_book.get("is_borrowed"):
      #     print(f"{my_book} : 책은 대출 상태가 아닙니다")
      # else:
      #     print(f"{my_book} : 책이 대출중입니다.")


  elif userInput== 5:
      print("도서 반납 매뉴입니다, 책을 반납하려면 회원이름과, 반납할 책의 isbn을 입력해 주세요")
      member_name = input("회원의 이름을 입력하세요 : ")
      book_isbn = input("반납할 책의 isbn을 입력하세요 :")

  elif userInput== 6:
      print("도서 검색의 매뉴입니다")
      book_name = input("도서관의 책을 검색하려면 책 이름을 입력하십시오")
      my_library.search_book(book_name)

  elif userInput== 7:
      break

  else: print("1~7까지의 숫자만 입력하세요\n")
