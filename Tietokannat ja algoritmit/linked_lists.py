memory = {
    'lists': 0,
    'last_list': None
}


class Node:
    def __init__(self, name=None, address=None, number=None):
        self.name = name
        self.address = address
        self.number = number
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addend(self, newdata):
        NewNode = Node(newdata[0], newdata[1], newdata[2])
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode


def menu():
    while(True):
        print('Next operation?', '1 = Add person information', '2 = Print person information', '3 = Remove all person information', '0 = Quit', sep='\n')
        select = input('Select: ')
        if select in selections:
            if select == "2" or select == "3":
                try:
                    print('List has the following persons:')
                    selections[select](memory['last_list'].head)
                except AttributeError:
                    print("List is empty!")
            else:
                selections[select]()
        else:
            print('Invalid selection.') 


def enter():
    name = input("Enter person name: ")
    address = input("Enter person address: ")
    number = input("Enter person number: ")
    if memory["lists"] == 0:
        memory['last_list'] = LinkedList()
        memory['last_list'].head = Node(name, address, number)
        memory['lists'] += 1
    else:
        memory['last_list'].addend((name, address, number))
        memory['lists'] += 1


def print_lists(lista):
    print(lista.name, ":", lista.address, ":", lista.number, end=" -> ")
    if lista.nextval:
        print_lists(lista.nextval)
    else:
        print("NULL")


def delete_lists(lista):
    memory["last_list"] = None
    memory["lists"]  = 0


selections = {
    '1': enter,
    '2': print_lists,
    '3': delete_lists,
    '0': quit,
}

menu()