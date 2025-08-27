def get_middle_character(text):

    length = len(text)
    mid = length // 2

    if length % 2 == 0:
        return text[mid-1:mid+1]
    else:
        return text [mid]
    

    print(get_middle_character("lean"))
    