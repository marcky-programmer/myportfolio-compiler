import os
print('\t\tCODE PYTHON COMPILER')
user_name = input('\nPlease input your name here: ').title()
os.system('cls')

explore = input(f'Hello {user_name} would you like to explore this system (yes or no): ').lower()
os.system('cls')

if explore == 'yes':
    answer = True

    while answer is True:
        print('\t\t|WELCOME TO MY SYSTEM|')
        print('________________________________________________________________')
        print(' In this system you wil learn the fundamental concept in python')
        print('________________________________________________________________')

        print('\nMAIN MENU')
        print('A. Print Statements ')
        print('B. Variables ')
        print('C. Operators ')
        print('D. Conditionals ')
        print('E. Loops ')
        print('F. Lists ')
        print('G. Function ')
        print('H. Exit the system ')

        choice = input('Select from the option above: ').lower()
        os.system('cls')

        #print statement
        if choice == 'a':
            print('\t\t\t-|PRINT STATEMENT|-')
            print('\nA print statement in a program is used to display variables, objects, \nor text to the output device (screen). In Python, the print() statement is \ncommonly used for displaying messages on the screen. ')
            
            while True:
                example = input('\nDo you want an example on how it is work? YES or NO--> ').lower()

                if example == 'yes':
                    print('\nprint("Hello World")')
                    print('The output is:')
                    print('Hello World')
                    
                    gagawin = input('\nDo you want to try? YES or NO.\nNote: If you choose No, you will be automatically returned to the main menu.-->  ').lower()
                    if gagawin == 'yes':
                            user_input = input('Input a phrases or word here --> ')
                            print(f'The output is: \n{user_input}')
                        #
                            # do_you = input('\nDo you want to continue exploring the print statement? YES or NO.\nNote: If you choose No, you will be automatically returned to the main menu. --> ').lower()
                            # os.system('cls')
                        
                            if do_you == 'yes':
                                while True:
                                    print('PRINT FUNCTION')
                                    print('1. Printing Text')
                                    print('2. Printing Numbers')
                                    print('3. Printing Multiple Items')
                                    print('4. Printing Variables')
                                    print('5. Printing with Formatting')
                                    print('6. Try to Code')
                                    print('7. Back to Main Menu')

                                    explore_pri_func = input('Choose the Print Funtion you want to explore/try--> ')
                                    
                                    if explore_pri_func == '1':
                                        print('\t\tPRINTING TEXT')
                                        print('______________________________________________________________')
                                        print('To print text, you need to put it in quotation marks: "" \'\'')
                                        print('\nexample:')
                                        print('\tprint(\'I want to learn Python\') or \nprint("I\'m happy")')
                                        print('\noutput:')
                                        print("\tI want to learn Python\nI\'m happy")
                                        print('______________________________________________________________')
                                        #need lagyan ng while latur nalang
                                        exit = input('\nType exit to return to the print function menu.').lower()
                                        if exit == ' exit':
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    elif explore_pri_func == '2':
                                        print('\t\t\tPRINTING NUMBERS')
                                        print('____________________________________________________________')
                                        print(' You can print integers or decimal directly without qoute')
                                        print('\nexample:')
                                        print('\tprint(23) \n\tprint(2.5)')
                                        print('\noutput:')
                                        print('\t23 \n\t2.5')
                                        print('____________________________________________________________')
                                        exit = input('\n Type exit to return to the print function menu.').lower()
                                        if exit == ' exit':
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    elif explore_pri_func == '3':
                                        print('\t\tPRINTING MULTIPLE ITEMS')
                                        print('___________________________________________________________')
                                        print('    You can print several items at oonce using comm "," \n \t\tThis process called CONCATENATION')
                                        print('\nexample:')
                                        print('\tprint("Age":, 18)\n\tprint("Sum:", 7+3)')
                                        print('\noutput:')
                                        print('\tAge: 18 \n\tSum: 10 ')
                                        exit = input('\nType exit to return to the print function menu. ').lower()
                                        print('___________________________________________________________')
                                        if exit == ' exit':
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    elif explore_pri_func == '4':
                                        print('\t\tPRINTING VARIABLES')
                                        print('______________________________________________________________')
                                        print('\tYou can print values stored in variables')
                                        print('\nexample:')
                                        print('\tname = "Marc"\n\tage = 18')
                                        print('\tprint(name)\n\tprint(age)')
                                        print('\noutput:')
                                        print('\tMarc\n\t18')
                                        print('______________________________________________________________')
                                        exit = input('\n Type exit to return to the print function menu. ').lower()
                                        if exit == ' exit':
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    elif explore_pri_func == '5':
                                        print('\t\tPRINTING WITH FORMATTING')
                                        print('______________________________________________________________')
                                        print('  You can use formatting format to make the output cleaner')
                                        print('\nexample:')
                                        print('\tname = "Marc" \n\tage = 18')
                                        print("\tprint(f'My name is {name } and I am {age} years old.')")
                                        print('output:')
                                        print('\tMy name is Marc and I am 18 years old.')
                                        print('______________________________________________________________')
                                        exit = input('\n Type exit to return to the print function menu. ').lower()
                                        if exit == ' exit':
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    elif explore_pri_func == '6':
                                            print('-|TRY IT WITH YOURSELF|-')
                                            print('Type your Python Code. After that,\nType RUN to the nextline to execute the code.')

                                            collection_code = []

                                            while True:
                                                lines = input('>>> ') or input( )
                                                if lines.strip().upper() == 'RUN':
                                                    break
                                                collection_code.append(lines)
                                            code = '\n'.join(collection_code)

                                            print('\nOutput:')
                                            try:
                                                exec(code)
                                            except Exception as e:
                                                print("error:", e)

                                            print('\nEnd code')
                                        
                                            while True:
                                                exit = input('\n Type exit to return to the print function menu. ').lower()
                                                if exit == 'exit':
                                                    break
                                                else:
                                                    print('INVALID INPUT, try again')
                                                    continue

                                    elif explore_pri_func == '7': 
                                        os.system('cls')
                                        break
                                        
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue
                            elif do_you == 'no':
                                break
                            else:
                                print('INVALID INPUT, try again')
                                continue  
                    elif gagawin == 'no':
                        break
                    else:
                        print('INVALID INPUT, try again')
                        continue
                elif example == 'no':
                    break
                else:
                        print('INVALID INPUTp, try again')   
                        continue    
        # elif example == 'no':
        #     print('Related Topics')
        #     print('VARIABLES')
        #     print('DATA TYPES')
        # else:
            
        # continue
        elif choice == 'b':
            print('-|VARIABLES|-')
            print('A variable in Python is simply a name that you give to a value\nso you can store is and use it when needed ')
            print('CHARACTERISTICS:\nStart with a letter or underscore\nCan contain letters, numbers, underscore\nCannot start with a number use special symbol and python keywords like if, for, and while')
            while True:
                do_you = input('Do you want an examle YES or NO--> ')
                if do_you == 'yes':
                    print('Example:')
                    print('\nname = lean\nprint(name)')
                    print('Output:')
                    print('\nlean')

                elif do_you == 'no':
                    break
                else:
                    ('INVALID INPUT, try again')

            continue
        elif choice == 'c':
            pass
            continue
        elif choice == 'd':
            pass
            continue
        elif choice == 'e':
            pass
            continue
        elif choice == 'f':
            pass
            continue
        elif choice == 'g':
            pass
            continue
        elif choice == 'h':
            pass
            continue
        else:
            print('Invalid input, please try again')
                            
# age = eval(input("enter age: " ))

# if age >= 18:
#     def status():
#         print("Adult")
# else:
#     def status():
#         print("Minor")

# status()   # prints: Minor