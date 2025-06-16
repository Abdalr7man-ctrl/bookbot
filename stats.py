
def get_num_words(text: str):
    return len(text.split())

def get_num_character(text: str) -> dict:
    my_dictionary: dict = {}
    for char in text.lower():
        if char in my_dictionary:
            my_dictionary[char] += 1
        else:
            my_dictionary[char] = 1
    return my_dictionary

def sort_on(mydict):
    return mydict["num"]

def sorted_list_dict(mydict: dict) -> list:
    lis = []
    for key, value in mydict.items():
        lis.append({"char": key, "num": value})
    lis.sort(reverse=True, key=sort_on)
    return lis
