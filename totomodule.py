import random
import os
import json
import ast

def settings():
    ''' Function download from user: nick, how many numbers to draw,
        maximum drawn number, quantity of chances.
        It allow to pick difficulty of the game - quantity of chances'''
    
    nick = input("Type your nick: ")
    fileName = nick + '.ini'
    player = readSettingsFromFile(fileName)
    answer = None

    if player:
        print("Your settings:\nQuantuty of numbers: %s \nMaximum number of lottery: %s Chances: %s" %
              (player[1], player[2], player[3]))
        answer = input("Do you want to change settings (y/n)? ")

    if not player or answer.lower() == 'y':    
        while True:
            try:
                howManyNumbers = int(input("Type quantity of numbers to draw: "))
                maxNumber = int(input("Type maximum number of lottery: "))
                if howManyNumbers > maxNumber:
                   print("Wrong data!")
                   continue
                howManyDraws = int(input("How many draws? "))
                break
            except ValueError:
                print("Wrong data!")
                continue
        player = [nick, str(howManyNumbers),str(maxNumber), str(howManyDraws)]
        print(player)
        saveSettingsToFile(fileName, player)
    return player[0:1] + [int(x) for x in player[1:4]]

def drawNumber(howManyNumbers, maxNumber):
    ''' Function draw random numbers from 1 to maxNumber '''
                                     
    numbers = []
    i = 0
    while i < howManyNumbers:
        number = random.randint(1, maxNumber)
        if numbers.count(number) == 0:
            numbers.append(number)
            i = i + 1
    return numbers

def readSettingsFromFile(fileName):
    ''' Read player setting from file. '''
    
    if os.path.isfile(fileName):
        file = open(fileName, 'r')
        line = file.readline()
        file.close()
        if line:
            return line.split(";")
    return False

def saveSettingsToFile(fileName, player):
    ''' Save player settings to file. '''

    file = open(fileName, 'w')
    file.write(';'.join(player))
    file.close()
    
def loadTxt(fileName):
    ''' Function load the data from .txt file. '''

    data = []
    d = {}
    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                lineList = line.split(';')
                for x in lineList:
                    (key, val) = x.split(':')
                    val = eval(val) #  !!! Used eval method. Be careful !!!
                    d[key] = val
                data.append(d)
    return data
    
    
def loadJson(fileName):
    ''' Function load the data in .json format from file. '''

    data = []
    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            data = json.load(file)
    return data

def saveTxt(fileName, data):
    ''' Function save the data from .txt file '''
    
    with open(fileName, 'w') as file:
        for dictionary in data:
            line = [k + ':' + str(w) for k, w in dictionary.items()]
            line = ";".join(line)
            file.write(line+'\n') 

    
def saveJson(fileName, data):
    ''' Function save the data in .json format to file '''

    with open(fileName, 'w') as file:
        json.dump(data, file)

def downloadShots(howManyNumbers, maxNumber):
    ''' Function download hits from user. '''

    print("Pick %s from %s numbers: " % (howManyNumbers, maxNumber))
    shots = set()
    i = 0
    while i < howManyNumbers:
        try:
            shot = int(input("Pick the number %s: " % (i + 1)))
        except ValueError:
            print("Wrong data!")
            continue
        
        if 0 < shot <= maxNumber and shot not in shots:
            shots.add(shot)
            i = i + 1
    return shots

def compareShots(numbers, shots):
    ''' Function compare shots with lottery numbers. Return quantity of hits. '''
    
    hits = set(numbers) & shots
        
    if hits:
        print("Quantity of hits: %s" % len(hits))
        hitsPrint = ", ".join(map(str, hits))
        print("Hited numbers: %s" % hitsPrint)
        hitsRet = [int(x) for x in hitsPrint.split(',')]
        return len(hits), hitsRet
    else:
        print("No hits. Please, try again.")

    print("\n" + "x" * 40 + "\n")  # print 40 times 'x'
