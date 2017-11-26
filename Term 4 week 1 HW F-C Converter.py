#Term 4 Week 1 Year 12
import time
ddd = 5
while ddd > 1:
    print('====================================================================================')
    print('                  Fahrenheit to Celsius Converter')
    # Asking user what temp system they want to use
    choice = input('What temp system do you want to use? F for fahrenheit and C for Celsius. ')
    print('...')
    time.sleep(1)
    print('====================================================================================')
    if choice == 'F':
        print('You have selected Fahrenheit')
        #Asking user what temp they want to use
        CALC = int(input('What temperature do you want converted? '))
        time.sleep(0.5)
        print('Calculating...')
        time.sleep(0.5)
        CALC = (CALC - 32) * 5 / 9
        print(str(CALC) + ' Degrees Celcius')
        time.sleep(0.5)
        close = input('Do you want to stop? y/n ');
        if close == 'y':
                print('Closing...')
                quit()
    elif choice == 'C':
         print('You have selected Celcius')
         #Asking user what temp they want to use
         CALC = int(input('What temperature do you want converted? '))
         time.sleep(0.5)
         print('...')
         print('Calculating...')
         time.sleep(0.5)
         CALC = (CALC /1.8) + 32
         print('Got it it is ', str(CALC) + ' Degrees Farenheit')
         time.sleep(0.5)
         close = input('Do you want to stop? y/n ')
         if close == 'y':
                print('Closing...')
                quit()
    else:
        print('I am sorry but I do not understand what you have said')
