import csv

user = open("user.csv",'r')
cc = user.readline()

def row(x):
    a = 0
    for i in x:
        a = a+1
    return(a)

def user_read():
    user = open("user.csv",'r')
    cc = user.read()
    d = [[('') for j in range (3)] for i in range (103)]
    e = 0
    f = 0
    for i in cc:
        if i != ";" and i != "\n":
            d[f][e] = d[f][e] + i
        elif i == ";":
            e = e+1
        elif i == "\n":
            e = 0
            f = f+1
    return d


def UsernameValid(x):
    user = open("user.csv",'r')
    user.readline()
    user_array = user_read()
    isValid = False
    for i in range (row(user)):
        if x == user_array[i][0]:
            isValid = True
            y = user_array[i][2]
            getrole(y)
    return isValid

def getrole(y):
    return y


#def ubahjin():
    #jin = input("Masukkan username jin: ")
    #if UsernameValid(jin):


print(user_read())