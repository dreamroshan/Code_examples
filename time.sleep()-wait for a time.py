import time

def sleeper():
    #Get user input
    num = raw_input('How long to wait: ')

    #Try to convert it to a float
    try:
        num = float(num)
    except ValueError:
        print('please enter in a number.\n')

   #Run our time.sleep() command,
   #and show the before and after time
    print('Before: %s'% time.ctime())
    time.sleep(num)
    print('After:%s\n'%time.ctime())

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received.Exiting.')
    exit()