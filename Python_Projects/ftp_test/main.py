# This is a sample Python script.
# Local $sServer = '176.241.138.180';
# '176.241.138.180' - MyCloud
# Local $sUsername = 'alexandr';
# 'updateuser' / 'alexandr'
# Local $sPass = '0937633284';
# '357951' / '0937633284'
# Local $hOpen = _FTP_Open('WD My-Cloud')
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ftplib import FTP
import os
import tempfile
import mybot
from telebot import TeleBot




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def connectDX():
    global ftp
    ftp = FTP(host='176.241.138.180', user='alexandr', passwd='0937633284')
    # Connecting
    # ftp.cwd(instal_path)
    # Changing path
    # listFiles=ftp.nlst()


def get_updateinfo_file(product, condition="release"):
    tmp_file_path = tempfile.gettempdir() + '\\' + product + 'updateinfo.xml'
    if condition == "release":
        ftp.cwd('//update_ftp//' + product + '//Program')
    else:
        ftp.cwd('//PublicDX//QA//Programs//' + product + '//Program')
    xml_for_download = 'updateinfo.xml'
    #print(xml_for_download)
    #print(tmp_file_path)
    with open(tmp_file_path, 'wb') as f:
        ftp.retrbinary('RETR ' + xml_for_download, f.write)
    with open(tmp_file_path, "r") as file:
        for line in file:
            str = file.readline()
            print(product)
            print(str)
            if str.find('<VERSION>') != -1:
                return str.replace('<VERSION>', '').replace('</VERSION>', '').lstrip()
        return 'error'


def download_test():
    print('Avaliagble for downloading:')
    # setup_files[], num_setup_files=0
    for i in range(len(listFiles) - 1):
        # if listFiles[i].find('ini') > 0:
        if listFiles[i].find('exe') > 0 and listFiles[i].find('Test') > -1:
            # setup_files[num_setup_files]=listFiles[i]
            #print('    ' + listFiles[i])
            out = 'd:\\' + listFiles[i]
            with open(out, 'wb') as f:
                ftp.retrbinary('RETR ' + listFiles[i], f.write)


def new_versions(condition="release"):
    products = ['BrainTest', 'M-Test', 'RheoTest']#, 'CardioTest') #
    if condition == "release":
        products.append('CardioTest')
    msg = ''
    for product1 in products:
        msg += product1 + ' ' + get_updateinfo_file(product1)# + '\n'
    print(msg)
    return msg

def disconnect():
    ftp.close()

if __name__ == '__main__':
    print_hi('PyCharm')
    #instal_path = 'PublicDX//QA'
    #connectDX()
    #msg=new_versions('QA')
    #msg = new_versions('release')
    #ftp.close()
#new_versions()
#'888716873:AAE_cr1wQt5IeeZbReR00S2hGvDq4cQpsxc'
#bot.poll(none_stop = True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
