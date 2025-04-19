def count_words(file_str):
    return len(file_str.split())

def print_return_ordered_dict(inpt_dict):
    for _ in range(len(inpt_dict)):
        print(f"{inpt_dict[_]["char"]}: {inpt_dict[_]["num"]}")

def check_max(inpt_dict):
    max_char = {"char": "", "num": 0}
    i = 0
    for _ in inpt_dict:
        if i == 0:
            i+=1
            max_char["num"] = inpt_dict[_]
            max_char["char"] = _
        else:
            if max_char["num"] < inpt_dict[_]:
                max_char["num"] = inpt_dict[_]
                max_char["char"] = _
    del inpt_dict[max_char["char"]]
    return [max_char, inpt_dict]


def return_ordered_dict(inpt_dict):
    list_ordered = []
    current_dict = inpt_dict
    for _ in range(len(inpt_dict)):
        ret_val = check_max(current_dict)
        list_ordered.append(ret_val[0])
        current_dict = ret_val[1]
    print_return_ordered_dict(list_ordered)

def count_chars(file_str):
    char_dict = dict()
    for _ in file_str:
        if _.isalpha():
            try:
                    char_dict[_.lower()] +=1
            except:
                char_dict[_.lower()] = 1
    return_ordered_dict(char_dict)        

