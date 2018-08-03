
#
# DICE ROLLING SIMULATOR
# version 1
#

import random

while True:
    start = str(input("Roll? [Input Y/N]\n> "))
    if start.lower() == "y":
        number = random.randint(0,6);
        print(number)
    else:
        exit()

        
        
