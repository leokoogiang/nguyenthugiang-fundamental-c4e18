# Tạo từ điển teencode
# teencode = {
#     "hc": "học",
#     "ng": "người",
#     "pt": "phát triển",
#     "any": "anh người yêu"

# }

# print(teencode)

# yc = input("Your code: ")

# if yc in teencode:
#     print(teencode[yc])
# else:
#     yw = input("Not found, do you want to contribute this word (Y/N? ")
#     if yw=="Y":
        
#     else:
#         print("Enter ")

# Tạo dictionary
teen_dict = {
    "hc": "học",
    "ng": "người",
    "pt": "phát triển",
    "any": "anh người yêu"

}
while True: 
    for key in teen_dict:
        print(key, end="\t") # In tất cả trên 1 hàng, cách nhau 1 tab
    print()

    code = input("Your code: ")
    if code in teen_dict:
        print("Translation: ", teen_dict[code])
    else:
        print("Not found")
        user_choice = input("Do you want to contribute? (Y/N) ").upper()
        if user_choice == "Y":
            translation = input("Your translation: ")
            teen_dict[code] = translation 
        else:
            print("Bye")
            break

    print(teen_dict)