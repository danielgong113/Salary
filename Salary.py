def hourinput():#input function for hours
    global hour #update the value for hour globally
    hour=input('Please Enter Hours: ')
    return hour
def hourcheck():# check if user input is valide (int float good, str is bad)
    global hour
    try:
        hour=float(hour)          
        return hour
    except:
        hour= -3
        print('Please enter a number like "0123"')
        return hour
def rateinput():
    global rate 
    rate=input('Please Enter Rate: ')
    return rate
def ratecheck():
    global rate
    try:
        rate=float(rate)          
        return rate
    except:
        rate= -3
        print('Please enter a number like "0123"')
        return rate
def compute():
    global pay
    # pay=hour*rate
    pay=format(hour*rate, '.2f')   # give 2 digits after the point
    print("Pay: $",pay)
    return pay
def main():
        global hour,rate
        while(hour<0):
            hourinput()
            hourcheck()
        while(rate<0):
            rateinput()
            ratecheck()
        compute()
        hour=-1 #reset hour value so that the while loop can run when user wants to run the program again
        rate=-1 #same here
    #quit()

hour=-1#inital value for hour while loop in ln36
rate=-1#initial value for rate while loop
status='n'#initial value for while loop that detect Y/N
wrongin='s'

if __name__=='__main__':
    # while (status=='y') or (status=='Y'):
    #     main()
    #     status=input('Do you want to quit the program? (Y/N)')
    #     if status == 'n' or status =='N'
    while True:
        main()
        # print(1)
        status=input('\nDo you want to quit the program? (Y/N)')
        if (status == 'y' or status =='Y'):
            # print(2)
            quit()
        elif (status == 'n'or status == 'N'):
            # print(3)
            pass
        elif(not any([status=='y',status=='n',status=='Y',status=='N'])): 
            # print(4)
            while(not any([wrongin=='y',wrongin=='n',wrongin=='Y',wrongin=='N'])):
                # print(5)
                wrongin=input('You have to enter Y or N')
                if(wrongin=='y'):
                    # print(6)
                    quit()
                elif(wrongin=='n'):
                    wrongin='s'
                    # print(7)
                    break
                else:
                    # print(8)
                    wrongin='s'
