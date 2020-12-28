def solution(phone_book):#전화번호 목록
    phone_book_dict = {}
    for phone in phone_book :
        phone_book_dict[phone] = len(phone) # -> 폰번호:폰번호길이
    # print(phone_book_dict)
    phone_book_item = phone_book_dict.items()
    sorted_phone_book_item = sorted(phone_book_item,key = lambda item : item[1]) #폰 번호 길이 기준으로 정렬
    # print(sorted_phone_book_item)
    for idx in range(len(sorted_phone_book_item)) :
        find_phone_number = sorted_phone_book_item[idx][0]
        for idx_compare in range(idx+1,len(sorted_phone_book_item)):
            if sorted_phone_book_item[idx_compare][0].find(find_phone_number) == 0:
                #sorted_phone_book_item[idx_compare][0]에서 find_phone_number가 맨 앞에 있는지 확인

                return False
    return True
p  =['12','123','1235','567','125']
print(solution(p))