#!/bin/python
# From 30 days of Code:
# https://www.hackerrank.com/contests/30-days-of-code/challenges/
# By: Hugo D. Lopes

import sys
from abc import ABCMeta, abstractmethod

# ---------------------------------------------------------------------


def day1():
    print " : " + type(5.35).__name__
    print " : " + type('a').__name__
    print " : " + type(False).__name__
    print " : " + type(100).__name__
    print " : " + type("I am a code monkey").__name__
    print " : " + type(True).__name__
    print " : " + type(17.3).__name__
    print " : " + type('c').__name__
    print " : " + type("derp").__name__
# ---------------------------------------------------------------------

def day2():
    # Meal price
    m = float(input())
    # Tip percentage
    t = float(input())
    # Tax percentage
    x = float(input())
    # Compute final meal price
    finalvalue = m + t*m/100 + x*m/100
    print "The final price of the meal is $" + str(int(round(finalvalue))) + "."
# ---------------------------------------------------------------------


def day3():
    N = float(raw_input().strip())
    print N
    if N % 2 != 0:
        print "Weird"
    elif N>=2 and N<=5:
        print "Not Weird"
    elif N>=6 and N<=20:
        print "Weird"
    else:
        print "Not Weird"
# ---------------------------------------------------------------------


class Person:
    def __init__(self,initial_Age):
        # Add some more code to run some checks on initial_Age
        if initial_Age < 0:
            print "This person is not valid, setting age to 0."
            self.age = 0
        else:
            self.age = initial_Age

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print "You are young."
        elif self.age >= 13 and self.age < 18:
            print "You are a teenager."
        else:
            print "You are old."

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


def day4():
    T=int(raw_input())
    for i in range(0, T):
        age=int(raw_input())
        p=Person(age)
        p.amIOld()
        for j in range(0,3):
            p.yearPasses()
        p.amIOld()
# ---------------------------------------------------------------------


def day5():
    T = int(raw_input())
    for k in range(0, T+1):
        T = raw_input().split()
        a = int(T[0])
        b = int(T[1])
        N = int(T[2])
        saveValue = a
        for n in range(0, N):
            value = saveValue + (2**n)*b
            print str(value) + " ",
            saveValue = value
        print " "
# ---------------------------------------------------------------------


def day6():
    n = int(raw_input().strip())
    for k in range(0, n):
        print " "*(n-k-1) + "#"*(k+1)
# ---------------------------------------------------------------------


def day7():
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    arr.reverse()
    for k in range(n):
        print arr[k],
# ---------------------------------------------------------------------


def day8():
    n = int(raw_input())
    phoneBook = dict()
    # Create phone book
    for k in range(n):
        name = raw_input()
        phone = str(raw_input())
        phoneBook[name] = phone
    # Return user requests
    while True:
        nameRequest = str(raw_input())
        if nameRequest in phoneBook:
            phoneAnswer = phoneBook.get(nameRequest)
            print nameRequest + '=' + phoneAnswer
        else:
            print 'Not found'
# ---------------------------------------------------------------------

def find_gcd(a,b):
   # write base condition
    return find_gcd(b, a%b) if b > 0 else a

def day9():
    # Take input
    a, b = map(int, raw_input().strip().split())

    gcd = find_gcd(a, b)
    print gcd
# ---------------------------------------------------------------------


def day10():
    n = int(raw_input())
    # Create binary
    for k in range(n):
        decimal = int(raw_input())
        binary = ''
        while decimal != 0:
            binary = str(decimal % 2) + binary
            decimal /= 2
        print binary
    # Return user requests
# ---------------------------------------------------------------------


def day11():
    # Read from input
    arr = []
    for arr_i in xrange(6):
        arr_temp = map(int,raw_input().strip().split(' '))
        arr.append(arr_temp)
    # Computations
    # First move column, then move row
    sumVector = []
    for r in range(4):
        for c in range(4):
            sumVector.append(sum(arr[r][c:c+3]) + arr[r+1][c+1] + sum(arr[r+2][c:c+3]))
    print max(sumVector)
# ---------------------------------------------------------------------


class Student:
    def __init__(self,firstName,lastName,phone):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone

    def display(self):
        print "First Name:",self.firstName
        print "Last Name:",self.lastName
        print "Phone:",self.phone


class Grade(Student):
    def __init__(self, firstName, lastName, phone, score):
        self.score = score
        super(Grade, self).__init__(firstName,lastName,phone)
        #Student.__init__(self,firstName,lastName,phone)

    def calculate(self):
        if self.score < 40:
            return 'D'
        elif 40 >= self.score < 60:
            return 'B'
        elif 60 >= self.score < 75:
            return 'A'
        elif 75 >= self.score < 90:
            return 'E'
        elif 90 <= self.score <= 100:
            return 'O'

def day12():
    firstName='Heraldo' #raw_input().strip()
    lastName='Memelli' #raw_input().strip()
    phone=8135627 #int(raw_input())
    score=90 #int(raw_input())
    stu=Grade(firstName,lastName,phone,score)
    stu.display()
    print "Grade:",stu.calculate()
# ---------------------------------------------------------------------


class Book:
    __metaclass__ = ABCMeta
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass

# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        #self.title = title
        #self.author = author
        self.price = price

    def display(self):
        print 'Title: ' + self.title
        print 'Author: ' + self.author
        print 'Price: ' + str(self.price)

def day13():
    title = raw_input()
    author = raw_input()
    price = int(raw_input())
    new_novel = MyBook(title, author, price)
    new_novel.display()
# ---------------------------------------------------------------------


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        absValues = []
        for k in range(len(self.__elements)):
            for n in range(k+1, len(self.__elements)):
                absValues.append(abs(self.__elements[k]-self.__elements[n]))
        self.maximumDifference = max(absValues)
# End of Difference class

def day14():
    _ = raw_input()
    a = [int(e) for e in raw_input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print d.maximumDifference
# ---------------------------------------------------------------------


class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current != None:
            print current.data,
            current = current.next

    def insert(self, head, data):
        if head != None:
            current = head
            # Find tail (last node)
            while current.next != None:
                current = current.next
            # Create new node
            x = Node()
            x.data = data
            # new node at the tail
            current.next = x
            if head.next is None:
                head.next = x
        else:
            head = Node()
            head.data = data
            head.next = None
        return head
        #Complete this method

def day15():
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)
    mylist.display(head)
# ---------------------------------------------------------------------


def minAbsVal(n, a):
    MinValue = 0
    for k in range(n-1):
        currentPair = [a[k], a[k+1]]
        diff = abs(currentPair[0] - currentPair[1])
        # Assign pair and save minimum value
        if diff < MinValue or MinValue == 0:
            MinValue = diff
            listMinAbsVal = currentPair
        elif diff == MinValue:
            listMinAbsVal.append(currentPair[0])
            listMinAbsVal.append(currentPair[1])
    return listMinAbsVal

def day16():
    n = int(raw_input())
    a = [int(e) for e in raw_input().split(' ')]
    # Sort values in list
    a.sort()
    # Compute minimum absolute difference
    listValues = minAbsVal(n, a)
    listValues = ' '.join(str(e) for e in listValues)
    print listValues
# ---------------------------------------------------------------------


#def day17():



# ---------------------------------------------------------------------
def testing():
    a = 12
    b = 2
    x = 'IF!' if 5 > 0 else 'ELSE!'

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Call the corresponding test
# ---------------------------------------------------------------------
#testing()
#day1()
#day2()
#day3()
#day4()
#day5()
#day6()
#day7()
#day8()
#day9() - NOT COMPLETED - ERRORS
#day10()
#day11()
#day12()
#day13()
#day14()
#day15()
day16()
#day17()


print "!!END of FILE!!"