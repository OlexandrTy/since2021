# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

def coloroMontages(montages='\\16\\Standard'):
    # Use a breakpoint in the code line below to debug your script.
    dirname = os.getcwd()
    entry=os.listdir(dirname + montages)
    for file in entry:
        if file.find('xmcfg')>0:
            print(dirname + montages + '\\'+ file)
            with open(dirname + montages + '\\' + file, 'r') as f:
                filedata = f.readlines()
                tempList = []
            for line in filedata:
                if line.find(' channel=')>0:
                    splitedLine = line.split(' ')
                    doublesplited=splitedLine[11].split('"')
                    if doublesplited[1] in ['2','5','6','10','11','15','16','20']:
                        line=line.replace(splitedLine[15],'color="12582912"')
                    if doublesplited[1] in ['4', '8', '9', '13', '14', '18', '19', '22']:
                        line = line.replace(splitedLine[15], 'color="192"')
                    if doublesplited[1] in ['0', '1']:
                        line = line.replace(splitedLine[15], 'color="16744448"')
                    if doublesplited[1] == '23':
                        line = line.replace(splitedLine[15], 'color="255"')
                        #print(line)
                    print(line)
                tempList.append(line)

            f.close()
            with open(dirname + montages + '\\' + file, 'w') as f:
                f.writelines(tempList)
            f.close()

    montageDir=dirname.split('\\')
    # Read in the file
    #with open('file.txt', 'r') as file:
    #    filedata = file.read()

    # Replace the target string
    #filedata = filedata.replace('ram', 'abcd')

    # Write the file out again
    #with open('file.txt', 'w') as file:
    #    file.write(filedata)


    #print(dirname)  # Press Ctrl+F8 to toggle the breakpoint.
    #print()
# montageDir[len(montageDir)-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    coloroMontages('\\16\\Standard')
    coloroMontages('\\16\\User')
    coloroMontages('\\24\\Standard')
    coloroMontages('\\24\\User')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
