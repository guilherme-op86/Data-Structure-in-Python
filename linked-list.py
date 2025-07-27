class Node:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.next = None

    def __repr__(self):
        return f'[{self.color}, {self.number}]'
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertWithoutPriority(self, color, number):
        new_node = Node(color, number)
        if(self.head is None):
            self.head = new_node
            return
        actual_node = self.head
        while(actual_node.next != None):
            actual_node = actual_node.next
        actual_node.next = new_node
    
    def insertWithPriority(self, color, number):
        new_node = Node(color, number)
        if (self.head is None):
            self.head = new_node
            return
        if (self.head.color == 'G'):
            new_node.next = self.head
            self.head = new_node
            return
        actual_node = self.head
        while (actual_node.next != None and actual_node.next.color == 'Y'):
            actual_node = actual_node.next
        new_node.next = actual_node.next
        actual_node.next = new_node

    def getPatientForConsultation(self):
        if(self.head is None):
            print('No patients for consultation.')
        removed_patient = self.head
        self.head = self.head.next
        print(f'Patient {removed_patient} presents fo consultation')
        return
    
    def printWatingList(self):
        actual_node = self.head
        while (actual_node != None):
            print(f'[{actual_node.color} {actual_node.number}]', end= ' -> ')
            actual_node = actual_node.next
        print(None)

    def insertData(self):
        print('-----------Menu Options-----------')
        print('1 - Add patient to queue')
        print('2 - Show patients in queue')
        print('3 - Call patient')
        print('4 - Exit')
        countGreen = 0
        countYellow = 200

        while True:
            try:
                option = int(input('Select your preferred option: '))
            except ValueError:
                print('Invalid option. Try again')
                continue
            if (option == 1):
                card_color = str(input('Enter the color of your card G/Y: ')).upper()
                if (card_color == 'G'):
                    countGreen+=1
                    self.insertWithoutPriority(card_color, countGreen)
                elif (card_color == 'Y'):
                    countYellow+=1
                    self.insertWithPriority(card_color, countYellow)
                else:
                    print('Invalid option. Try again.')
                    continue
            if (option == 2):
                if(self.head is None):
                    print('No patients in queue')
                else:
                    self.printWatingList()
            if (option == 3):
                if(self.head is None):
                    print('No patients for consultation')
                else:
                    self.getPatientForConsultation()
            if (option == 4):
                print('All consultations are complete.')
                break
                


lista = LinkedList()
lista.insertData()
        