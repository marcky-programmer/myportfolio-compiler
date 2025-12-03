import os

print('\t\tCODE PYTHON COMPILER')
user_name = input('\nPlease input your name here: ').title()
os.system('cls')

explore = input(f'Hello {user_name} would you like to explore this system (yes or no): ').lower()
os.system('cls')

if explore == 'yes':
    answer = True

    while answer is True: #main menu
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

        choice = input('Please select an option from the above: ').lower()
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
                            do_you = input('\nDo you want to continue exploring the print statement? YES or NO.\nNote: If you choose No, you will be automatically returned to the main menu. --> ').lower()
                            os.system('cls')
                        
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
                                        print('\tprint(\'I want to learn Python\') or \n\tprint("I\'m happy")')
                                        print('\noutput:')
                                        print("\tI want to learn Python\n\tI\'m happy")
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
                                break
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
            print('\t\t\t-|VARIABLES|-')
            print('_______________________________________________________________')
            print('A variable in Python is simply a name that you give to a value\nso you can store is and use it when needed ')
            print('\nCHARACTERISTICS:\nDynamic\nUser define\nThe value is depend on user/s(users can input\nStart with a letter or underscore\nCan contain letters, numbers, underscore\nCannot start with a number\nCannot use special symbol\nCannot use python keywords like if, for, and while')
            print('_______________________________________________________________')
            while True:
                do_you = input('\nDo you want an example of a variables (YES or NO)--> ').lower()
                if do_you == 'yes':
                    print('__________________________________________________')
                    print('Examples:')
                    print('\nname = lean ' \
                    '_activity1\ncode_challenge\nage = input("Type your age--> ")')
                    print('\n\tRelated Topics:')

                    print('DATA TYPES')
                    print('__________________________________________________')
                    do_you = input('Do you want to explore Data types? YES no NO--> ').lower()
                    if do_you == 'yes':
                        while True:
                            print('\t\t-|DATA TYPES|-')
                            print('______________________________________________________')
                            print('classifications that specify what kind of value a' \
                            '\nvariable holds and what operations can be performed on it.' \
                            '\nThey tell Python how to interpret the data.')
                            print('1. String (str)')
                            print('2. Integer (int)')
                            print('3. Float ')
                            print('4. Boolean')
                            print('5. Try to code')
                            print('6. Back to Main Menu')
                            print('______________________________________________________')

                            _data_types = input('\nSelect from the option above-->  ')
                            os.system('cls')
                            
                            if _data_types == '1':
                                print('\t\t-|STRING|-')
                                print('_____________________________________________')
                                print('a data type used to represent text and always\nuse quatation \'\' or " ".')
                                print('_____________________________________________')

                                example = input('\nDo you want an example (YES or NO)--> ').lower()

                                if example == 'yes':
                                    print('Example:')
                                    print('\tprint("Hello world")\n\tname = "lean"\n\t"123"')
                                    print('\n\tRelated Topics')
                                    print('String Methods')
                                    print('____________________________________________')

                                    method = input('\nDo you want to explore String Methods? YES or NO--> ').lower()

                                
                                    if method == 'yes':
                                        while True:
                                            print('\t\t-|STRING METHOD|-')
                                            print('____________________________________________')
                                            print(' it is a built-in functions in Python that are' \
                                            '\nused to modify,analyze and manipulate a STRING. ')
                                        
                                            print('1. .upper()') 
                                            print('2. .lower()') 
                                            print('3. .capitalize()') 
                                            print('4. .title()') 
                                            print('5. .strip()') 
                                            print('6. exit')
                                            print('____________________________________________')
                                            string_method = input('\nSelect the option above--> ').lower()
                                            os.system('cls')
                                            if string_method == '1':
                                                while True:
                                                    print('\t\t-|.upper()|-')
                                                    print('____________________________________________')
                                                    print('\tConverts string to uppercase' \
                                                    '\nExample:' \
                                                    '\n\t"Marc".upper()' \
                                                    '\nOuput:' \
                                                    '\n\tMARC')
                                                    print('____________________________________________')
                                                
                                                    exit = input('\n Type exit to return to the String Methods Menu. ').lower()
                                                    if exit == 'exit':
                                                        break
                                                    else:
                                                        print('INVALID INPUT, try again')
                                                        continue
                                            elif string_method == '2':
                                                print('\t\t-|.lower()|-')
                                                print('________________________________________________')
                                                print('Converts string to lowercase' \
                                                '\nExample:' \
                                                '\n\t"MARC or MaRc".lower()' \
                                                '\nOuput:' \
                                                '\n\tmarc or marc')
                                                print('________________________________________________')
                                                while True:
                                                    exit = input('\n Type exit to return to the String Methods Menu. ').lower()
                                                    if exit == 'exit':
                                                        break
                                                    else:
                                                        print('INVALID INPUT, try again')
                                                        continue
                                            elif string_method == '3':
                                                print('\t\t-|.capitalize()|-')
                                                print('___________________________________________________')
                                                print('')
                                                print('\tCapitalizes the first letter' \
                                                '\nExample:' \
                                                '\t\n\"marc".capitalize()' \
                                                '\nOuput:' \
                                                '\n\tMarc')
                                                print('___________________________________________________')
                                                while True:
                                                    exit = input('\n Type exit to return to the  String Methods Menu. ').lower()
                                                    if exit == 'exit':
                                                        break
                                                    else:
                                                        print('INVALID INPUT, try again')
                                                        continue
                                            elif string_method == '4':
                                                print('\t\t-|.title()|-')
                                                print('________________________________________________')
                                                print('  Capitalizes the first letter of each word' \
                                                '\nExample:' \
                                                '\n\t"lean marc g alcala".title()' \
                                                '\nOuput:' \
                                                '\n\tLean Mard G Alcala')
                                                print('________________________________________________')
                                                while True:
                                                    exit = input('\n Type exit to return to the String Method Menu. ').lower()
                                                    if exit == 'exit':
                                                        break
                                                    else:
                                                        print('INVALIsD INPUT, try again')
                                                        continue
                                            elif string_method == '5':
                                                print('\t\t-|.strip()|-')
                                                print('____________________________________________')
                                                print('Removes spaces from the start and end' \
                                                '\nExample:' \
                                                '\n\t" hi ".strip()' \
                                                '\nOuput:' \
                                                '\n\thi')
                                                print('____________________________________________')
                                                while True:
                                                    exit = input('\n Type exit to return to the Strinf Method Menu. ').lower()
                                                    if exit == 'exit':
                                                        break
                                                    else:
                                                        print('INVALID INPUT, try again')
                                                        continue
                                            elif string_method == '6':
                                                break
                                            else:
                                                print('IVALID INPUT, try again')
                                        break
                                    elif method == 'no':
                                        break
                                    else:
                                        print('INVALID INPUT,try again')

                                    # exit = input('Type exit to return in DATA TYPES menu --> ').lower()
                                elif example == 'no':
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                            elif _data_types == '2':
                                print('\t\t-|INTEGER|-')
                                print('________________________________________________')
                                print('a data type in used to represent whole numbers\nwithout any decimal part. Examples are -3, 0,\n7, 100.')

                                example = input('Do you want an example (YES or NO)--> ').lower()

                                if example == 'yes':
                                    print('\nExample:')
                                    print('\tprint(123)\n\tname = -456\t\n789')
                                    print('________________________________________________')
                                    
                                    exit = input('\nType exit to return to the print Data Types menu. ').lower()
                                    if exit == 'exit':
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue

                                elif example == 'no':
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                            elif _data_types == '3':
                                print('\t\t-|FLOAT|-')
                                print('______________________________________________')
                                print('a data type in used to represent numbers with\n decimal points (fractional numbers) 3.14,\t-.011, or 2.0.')

                                example = input('Do you want an example (YES or NO)--> ').lower()

                                if example == 'yes':
                                    print('\nExample:')
                                    print('\tprint(1.23)\n\tnumber = -0.0456\t\n10.0')
                                    print('______________________________________________')

                                    exit = input('\n Type exit to return to the print Data Types menu. ').lower()
                                    if exit == 'exit':
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue

                                elif example == 'no':
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                            elif _data_types == '4':
                                print('\t\t-|BOOLEAN|-')
                                print('______________________________________________')
                                print('a data type that represents truth values. It\ncan only have one of two possible values:')
                                print('\tTrue (meaning yes, or truth)')
                                print('\tFalse (meaning no, or false)')

                                example = input('Do you want an example (YES or NO)--> ').lower()

                                if example == 'yes':
                                    print('\tExample:')
                                    print('\t_prog_isEasy = False\n\t_final_isBusy = True')
                                    print('______________________________________________')

            
                                    exit = input('\n Type exit to return to the print Data Types menu. ').lower()
                                    if exit == 'exit':
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue

                                elif example == 'no':
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                            elif _data_types == '5':
                                print('\t\t-|TRY IT WITH YOURSELF|-')
                                print('______________________________________________')
                                print('Type your Python Code. After that,\nType RUN to the nextline to execute the code.')
                                print('______________________________________________')
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

                                print('\n--|End code|--')
                            
                                while True:
                                    exit = input('\n Type exit to return to the print function menu. ').lower()
                                    if exit == 'exit':
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue
                            elif _data_types == '6':
                                os.system('cls')
                                break
                            else:
                                print('INVALID INPUT, try again')
                        break
                    elif do_you == 'no':
                        break
                    else:
                        print('INVALID INPUT,try again')
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