#Braden Leach
#December 9 2024
#


import time 
# #----Temp Try----#


for num in range(0,6):

    farenheit = num * (9/5) + 32

    print(f'{num}°C in farenheit is {farenheit}°F')
    print('...')
    time.sleep(1)



#----Input version----#
running = True
while running: 
    user_inp = int(input('What number do you want to convert to farenheit?: (input -9999 to stop code)\n'))
    if user_inp == -9999:
        print(f'\nThanks for trying my code!')
        time.sleep(1)
        print('Exiting code...')
        time.sleep(1)
        break 
    else:
        
        farenheit = user_inp * (9/5) + 32
    print(f'\n{user_inp}°C in farenheit is {farenheit:.2f}°F\n')
    time.sleep(1)



    



