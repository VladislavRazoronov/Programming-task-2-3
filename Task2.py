import json
from twitter_api import twitter1

def read_dict(dict):
    """
    (dict)->element
    Shows dict keys and returns selected element
    """
    action = input('Would you like to select dictionary element or print dictionary?(keys-element,else-print)? ')
    if action.lower() == 'keys' or action.lower() == 'key':
        print(dict.keys())
        while True:
            user_key = input('Enter selected key: ')
            if user_key in dict.keys():
                break
            print('Invalid key')
        if type(dict[user_key]) == dict:
            return read_dict(dict[user_key])
        elif type(dict[user_key]) == list:
            return read_list(dict[user_key])
        else:
            return dict[user_key]
    else:
        return dict

def read_list(lst):
    """
    (list)->element
    shows list length and returns selected element
    """
    if len(lst) == 0:
        return lst
    action = input('Would you like to select list element or print list?(keys-element,else-print)? ')
    if action.lower() == 'keys' or action.lower() == 'key':
        print(len(lst) + 1)
        while True:
            number = int(input('Enter element index: '))
            if number <= len(lst) + 1:
                break
            print('Invalid index')
        number -= 1
        if type(lst[number]) == dict:
            read_dict(lst[number])
        elif type(lst[number]) == list:
            read_list(lst[number])
        else:
            return lst[number]
    else:
        return lst

if __name__ == '__main__':
    data = twitter1.get_data()
    info = json.loads(data)
    print('Here is the list of keys:')
    for el in info:
        for key in el.keys():
            print(key)
    user_key = input('Insert desired key: ')
    for el in info:
        if user_key in el.keys():
            if type(el[user_key]) != dict and type(el[user_key]) != list:
                print(el[user_key])
                break
            else:
                if type(el[user_key]) == dict:
                    print(read_dict(el[user_key]))
                    break
                else:
                    print(read_list(el[user_key]))
                    break
