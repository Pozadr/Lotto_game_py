from totomodule import settings, drawNumber, downloadShots, compareShots
from totomodule import loadJson, saveJson, loadTxt, saveTxt
import time

def main(args):
    # game settings
    nick, howManyNumbers, maxNumber, howManyDraws = settings()

    # draw numbers
    numbers = drawNumber(howManyNumbers, maxNumber)

    # download hits of user and check result of lottery
    for i in range(howManyDraws):
        print("\nChance no. %s from %s" % (i + 1, howManyDraws))
        shots = downloadShots(howManyNumbers, maxNumber)
        howManyHits, hits = compareShots(set(numbers), shots)
        
    fileNameJson = nick + '.json'  # file name with history of hits .json
    lottery = loadJson(fileNameJson)
    lottery.append({
        "time": time.time(),
        "data": (howManyDraws, maxNumber),
        "drawn": numbers,
        "Hits quantity": howManyHits,
        "Hits": hits
        })
    saveJson(fileNameJson, lottery)

    fileNameTxt = nick + '.txt'  # file name with history of hits .txt
    lotteryTxt = loadTxt(fileNameTxt)
    lotteryTxt.append({
    "time": time.time(),
    "data": (howManyDraws, maxNumber),
    "drawn": numbers,
    "Hits quantity": howManyHits,
    "Hits": hits
    })
    saveTxt(fileNameTxt, lotteryTxt)

    numbers = ", ".join(map(str, numbers))  # 1.3.11. | https://python101.readthedocs.io/pl/latest/podstawy/elotek/index.html
    print("Randomly drawn numbers: ", numbers)
    return 0

# Program begins in main function.
# If you run program as main file '__name__' will be written by '__main__'. Code will run after start.
# If you run program as module '__name__' will be written by '_file_name__'('__Lotto__').
# Code will not run after start. You need to call a function.
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
