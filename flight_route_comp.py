#---Destinations that both airlines fly to.
#---Destinations unique to your airline.
#---Whether there are any destinations that neither airline shares.

import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def route_comp(our_routes, competitor_routes):
    while True:
        print()
        print(Style.BRIGHT + '              RouteComparison App')
        print('             ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        print('''                   Menu
              
    1. Destinations provided by BOTH airlines
    2. Destinations that only WE provide
    3. Destinations that NEITHER airlines share
    4. Quit''')    
        print()
        choice = input('What destinations would you like to explore?: ')
        print()
        if choice == '1':
            both = our_routes.intersection(competitor_routes)
            print('Here are the destinations that ' + Style.BRIGHT + Fore.LIGHTGREEN_EX + 'BOTH' +Style.RESET_ALL + ' airlines offer:')
            print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
            for b in both:
                print(b)
        elif choice == '2':
            we = our_routes.difference(competitor_routes)
            print('Here are the destinations that only ' + Style.BRIGHT + Fore.LIGHTCYAN_EX + 'WE' +Style.RESET_ALL + ' offer:')
            print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
            for w in we:
                print(w)
        elif choice == '3':
            sym = our_routes.symmetric_difference(competitor_routes)
            print('Here are the destinations that ' + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'NEITHER' +Style.RESET_ALL + ' airline shares:')
            print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
            for s in sym:
                print(s)
        elif choice == '4':
            print('         Thanks for using RouteComparison')
            print()
            break
        else:
            print(Style.BRIGHT + Fore.RED +'        Plese enter valid menu option')



route_comp(our_routes, competitor_routes)