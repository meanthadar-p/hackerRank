contacts_lists = list()


def contacts(queries):
    result = list()
    for querie in queries:
        name = querie[1]
        if querie[0] == "add":
            add_contact(name)
        elif querie[0] == "find":
            result.append(find_contacts(name))

    return answer_format(result)

def add_contact(name):
    contacts_lists.append(name)


def find_contacts(name):
    count = 0
    for contact in contacts_lists:
        if contact[0:len(name)] == name:
            count += 1

    return count


def answer_format(arr):
    result = arr[0]
    for a in arr[1:len(arr)]:
        result = "{0}{1}".format(result, a)

    return result


result = contacts([["add", "hack"], ["add", "hackerrank"], ["find", "hac"], ["find",  "hak"]])
print(result)

# using tree graph to count
#       {}
#     a    m
#   n       a
#  t       t  x

d = {
        'dependence': 2,
        'h': {
            'dependence': 2,
            'a':{
                'dependence': 2,
                'c':{
                    'dependence': 1,
                    'k': {
                        'dependence': 0
                    }
                },
                'k': {
                    'dependence': 0
                }
            }
        }
    }


def finding(dict_contacts, contact):
    try:
        cnt = dict_contacts[contact[0]]['dependence']
    except:
        if len(contact) == 0:
            print("found {0} contact".format(dict_contacts['dependence']))
            return dict_contacts['dependence']

        print("didn't found this contact")
        return 0

    if len(contact[1::]) == 0:
        print("found {0} contact".format(cnt))
        return cnt

    finding(dict_contacts[contact[0]], contact[1::])


d2 = dict()


def adding(contact):
    contact = list(contact)


contact = "hx"
finding(d, list(contact))
