import re


def get_ampl_key():
    """Concardate next digits: date(MMYY), ampl_num(DDDDD), device_type(DD), set(D)
    date:str, ampl_num:str, device_type:str, d_set:int"""
    date=get_date()
    ampl_num=get_ampl_num()
    device_type=get_device_type()
    d_set=get_set(device_type)
    ampl_key=date+ampl_num+device_type+str(d_set)
    print(ampl_key)
    return ampl_key

def get_controlsumm(skey):
    controlsumm = 0
    for i in range(len(skey)):
        controlsumm += int(skey[i])
    if controlsumm < 10:
        controlsumm = '0' + str(controlsumm)
    else:
        controlsumm = str(controlsumm)
    #print(controlsumm)
    return controlsumm

def get_product_key(ampl_key):
    print(ampl_key)
    key1=str(hex(int(ampl_key)))
    #print(key1)
    splited=key1.split('x')
    while len(splited[1])<12:
        splited[1]='0'+splited[1]
    #print(splited[1])
    key1=splited[1].upper()

    controlsumm1 = get_controlsumm(str(ampl_key))


    key2=key1[6:13]+key1[0:6]
    #print(key2)
    ikey=int(key2,16)
    #print(ikey)
    skey=str(ikey)

    controlsumm2=get_controlsumm(skey)

    key3=str(controlsumm1)+str(key2)+str(controlsumm2)
    #print(key3)

    key4=key3[0:4]+'-'+key3[4:8]+'-'+key3[8:12]+'-'+key3[12:16]
    #print(key4)
    return key4

def main():
    ampl_key=get_ampl_key()
    product_key=get_product_key(ampl_key)
    print(product_key)




def test_get_ampl_key():
    print('Test ampl_key started')
    date = ["01/01", "01/2001","01.01","01.2001"]
    ampl_num = [1,0,99999,8787]
    device_type = [10,1,21,55]
    d_set = [1,3,5,6]
    for i in range(4):
        if get_ampl_key(date[i], ampl_num[i], device_type[i], d_set[i]) == "112109999011":
           print('Test ' + str(i+1) + ' passed')
        else: print('Test ' + str(i+1) + ' failed')

#042100000011 095B-050B-0009-CD54
#042100000551 185B-0727-0009-CD45
#042100666011 2765-2E9B-0009-CD54
#042100666211 2965-2F63-0009-CD56
def test_get_product_key():
    print('Test product_key started')
    ampl_key=['042100000011','042100000551','042100666011','042100666211']
    product_key=['095B-050B-0009-CD54','185B-0727-0009-CD45','2765-2E9B-0009-CD54','2965-2F63-0009-CD56']
    for i in range(len(ampl_key)):
        print(product_key[i])
        if get_product_key(ampl_key[i]) == product_key[i]:
           print('Test ' + str(i+1) + ' passed')
        else: print('Test ' + str(i+1) + ' failed')


#test_get_ampl_key()
#test_get_product_key()
def input_from_prompt():
    """Recives next digits: date(MMYY), ampl_num(DDDDD), device_type(DD), set_num(D)
            and returns ampl_key"""
    pass



def get_date():
    date:str
    month=0
    year=0
    while True:
        try:
            month = int(input('Enter Month number: '))
            assert 0 < month <= 12
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between 1 and 12")
        else:
            break
    if month<10:
        month='0'+str(month)
    else:
        month = str(month)


    while True:
        try:
            year = int(input('Enter Year number: '))
            assert 0 <= year <= 22
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between 00 and 22")
        else:
            break
    if year<10:
        year='0'+str(year)
    else:
        year = str(year)


    date=month+year
    print('Digits from Date: '+date)
    return date

    """month=input('Enter Month number (by template "MM": ')
    year=input('Enter Year number (by template "YY": ')
    date=month+year
    device_type=input('Enter Device type (DD): ')
    ampl_num=input('Enter Amplifier number (DDDDD): ')
    set=input('Enter Set number (D): ')"""
def get_device_type():
    device_type=0
    correct_types=('01','02', '11', '21','31','32','41','42','43','44','45','51','52','53','54','55')
    while True:
        try:
            device_type = int(input('Enter Device_type number: '))
            if device_type<10:
                device_type='0'+str(device_type)
            else:
                device_type=str(device_type)
            #01 EEG 16 OLD|02 EEG 24 OLD|11 EMG 4 OLD|21 RHEOGRAPH|31 ECG USB|32 ECG BT|
            #41 EEG  BIOFEEDBACK|42 EEG  BASIC|43 EEG  STANDARD|44 EEG  EXTENDED|
            #45 EEG POLYGRAPH|51 EMG 2 ONE|52 EMG 4 ONE|53 EMG 8 ONE|54 EMG 2 HRC|55 EMG 2 HRA
            assert device_type in correct_types
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer\n01 EEG 16 OLD|02 EEG 24 OLD|11 EMG 4 OLD|21 RHEOGRAPH|31 ECG USB|32 ECG BT|\
            \n41 EEG  BIOFEEDBACK|42 EEG  BASIC|43 EEG  STANDARD|44 EEG  EXTENDED|\
            \n45 EEG POLYGRAPH|51 EMG 2 ONE|52 EMG 4 ONE|53 EMG 8 ONE|54 EMG 2 HRC|55 EMG 2 HRA")
        else:
            break
    print('Device_type number: '+device_type)
    return device_type

def get_ampl_num():
    ampl_num=0
    while True:
        try:
            ampl_num = int(input('Enter Amplifier number: '))
            while len(str(ampl_num))<5:
                ampl_num='0'+str(ampl_num)
            assert 0 < int(ampl_num) < 99999
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between 0 and 99999")
        else:
            break
    print('Amplifier number: '+ampl_num)
    return ampl_num

def get_set(device_type=0):
    """Case 0 or 4
	    1 BASE|2 EP|3 EP+CP|4 VIDEO|5 EP+VIDEO|6 EP+CP+VIDEO
    Case 1 or 5
	    1 BASE|2 EP|3 EP+CP
	Case 2
		1 REG|2 REG\RVG|3 FULL
	Case 3
	    1 ST|2 ERGO"""
    str_device_type=str(device_type)
    first_digit=int(str_device_type[0])
    if first_digit in (0,4):
        correct_num=range(1,7)
    elif first_digit in (1,5):
        correct_num=range(1,4)
    elif first_digit==2:
        correct_num=range(1,4)
    else:
        correct_num = range(1,3)

    set_num = 0
    while True:
        try:
            set_num = int(input('Enter Setting number: '))
            assert set_num in correct_num
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between "+str(correct_num[0])+" and "+str(correct_num[-1]))
        else:
            break
    print('Setting number: ' + str(set_num))
    return set_num

#get_date()
#device_type=get_device_type()
#get_ampl_num()
#get_set(device_type)
#get_ampl_key()
#main()
