import os

print('\t\t~|CODE PYTHON COMPILER|~')
print('_________________________________________________________________')
user_name = input('\nPlease input your name here: ').title()
os.system('cls')

while True:
    explore = input(f'Hello {user_name} would you like to explore this system (YES or NO): ').lower()
    os.system('cls')

    if explore == 'yes':
        answer = True

        while answer is True: #main menu
            print('\t\t=|WELCOME TO MY SYSTEM|=')
            print('________________________________________________________________')
            print(' In this system you wil learn the fundamental concept in python')
            print('________________________________________________________________')

            print('\nMAIN MENU')
            print('A. Print Statements ')
            print('B. Variables ')
            print('C. Operators ')
            print('D. Conditionals ')
            print('E. Loops ')
            print('F. List ')
            print('G. Function ')
            print('H. Try to code')
            print('I. Exit the system ')
            print('________________________________________________________________')


            choice = input('\nPlease select an option from the above: ').lower()
            os.system('cls')

            #print statement
            if choice == 'a':
                print('\t\t\t\t-|PRINT STATEMENT|-')
                print('______________________________________________________________________________________')
                print('   \nA print statement in a program is used to display variables, objects or text \nto the output device (screen). In Python, the print() statementis commonly used\nfor displaying messages on the screen. ')
                
                while True:
                    example = input('\nDo you want an example on how it is work? YES or NO--> ').lower()

                    if example == 'yes':
                        print('\nprint("Hello World")')
                        print('The output is:')
                        print('Hello World')
                        
                        gagawin = input('\nDo you want to try? YES or NO.\nNote: If you choose No, you will be automatically returned to the main menu.-->  ').lower()
                        if gagawin == 'yes':
                                user_input = input('Input a phrases or word here --> ')
                                print(f'The output is: \n\t\t{user_input}')
                                print('_________________________________________________________________________________________')

                                do_you = input('\nDo you want to continue exploring the print statement? YES or NO.\nNote: If you choose No, you will be automatically returned to the main menu. --> ').lower()
                                os.system('cls')
                            
                                if do_you == 'yes':
                                    while True:
                                        print('______________________________________')
                                        print('PRINT FUNCTION')
                                        print('1. Printing Text')
                                        print('2. Printing Numbers')
                                        print('3. Printing Multiple Items')
                                        print('4. Printing Variables')
                                        print('5. Printing with Formatting')
                                        print('6. Try to Code')
                                        print('7. Back to Main Menu')
                                        print('______________________________________')
                                        explore_pri_func = input('\nChoose the Print Funtion you want to explore/try--> ')
                                        os.system('cls')
                                        
                                        if explore_pri_func == '1':
                                            print('\t\t\tPRINTING TEXT')
                                            print('______________________________________________________________')
                                            print('  To print text, you need to put it in quotation marks: "" ,\'\'')
                                            print('\nexample:')
                                            print('\tprint(\'I want to learn Python\') or \n\tprint("I\'m happy")')
                                            print('\noutput:')
                                            print("\tI want to learn Python\n\tI\'m happy")
                                            print('______________________________________________________________')
                                            #need lagyan ng while latur nalang
                                            
                                            while True:
                                                exit = input('\n Type exit to return to the print function menu--> ').lower().strip()
                                                if exit == 'exit':
                                                    os.system('cls')
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
                                            
                                            while True:
                                                exit = input('\n Type exit to return to the print function menu--> ').lower().strip()
                                                if exit == 'exit':
                                                    os.system('cls')
                                                    break
                                                else:
                                                    print('INVALID INPUT, try again')
                                                    continue
                                        elif explore_pri_func == '3':
                                            print('\t\tPRINTING MULTIPLE ITEMS')
                                            print('___________________________________________________________')
                                            print('    You can print several items at oonce using comm "," \n \t\tThis process called CONCATENATION')
                                            print('\nexample:')
                                            print('\tprint("age":, 18)\n\tprint("sum:", 7+3)')
                                            print('\noutput:')
                                            print('\tage: 18 \n\tsum: 10 ')
                                            print('___________________________________________________________')
                                            while True:
                                                exit = input('\n Type exit to return to the print function menu--> ').lower().strip()
                                                if exit == 'exit':
                                                    os.system('cls')
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
                                            
                                            while True:
                                                exit = input('\n Type exit to return to the print function menu--> ').lower().strip()
                                                if exit == 'exit':
                                                    os.system('cls')
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
                                            
                                            while True:
                                                exit = input('\n Type exit to return to the print function menu--> ').lower().strip()
                                                if exit == 'exit':
                                                    os.system('cls')
                                                    break
                                                else:
                                                    print('INVALID INPUT, try again')
                                                    continue
                                        elif explore_pri_func == '6':
                                                print('\t\t-|TRY IT WITH YOURSELF|-')
                                                print('_______________________________________________________')
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

                                                print('_______________________________________________________')
                                                print('\n\t\t-|End code|-')
                                                print('_______________________________________________________')
                                            
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
                            os.sytem('cls')
                            break
                        else:
                            print('INVALID INPUT, try again')
                            continue
                    elif example == 'no':
                        break
                    else:
                            print('INVALID INPUTp, try again')   
                            continue        
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
                        print('\nname = "lean"' \
                        '\nage = eval(input("Type your age--> "))')
                        print('\n\tRelated Topics:')

                        print('DATA TYPES')
                        print('__________________________________________________')
                        do_you = input('Do you want to explore Data types? YES no NO--> ').lower()
                        os.system('cls')
                        if do_you == 'yes':
                            while True:
                                print('\t\t-|DATA TYPES|-')
                                print('__________________________________________________________')
                                print('classifications that specify what kind of value a' \
                                'variable\nholds and what operations can be performed on it.' \
                                'They\ntell Python how to interpret the data.')
                                print('1. String (str)')
                                print('2. Integer (int)')
                                print('3. Float ')
                                print('4. Boolean')
                                print('5. Dictionary')
                                print('6. Try to code')
                                print('7. Back to Main Menu')
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
                                        print('STRING METHODS')
                                        print('____________________________________________')

                                        method = input('\nDo you want to explore String Methods? YES or NO--> ').lower()
                                        os.system('cls')

                                        while True:
                                            if method == 'yes':
                                                while True:
                                                    print('\t\t-|STRING METHOD|-')
                                                    print('_________________________________________________')
                                                    print(' it is a built-in functions in Python that are' \
                                                    '\nused to modify,analyze and manipulate a STRING. ')
                                                
                                                    print('1. .upper()') 
                                                    print('2. .lower()') 
                                                    print('3. .capitalize()') 
                                                    print('4. .title()') 
                                                    print('5. .strip()') 
                                                    print('6. exit')
                                                    print('_________________________________________________')
                                                    string_method = input('\nSelect the option above--> ').lower()
                                                    os.system('cls')
                                                    if string_method == '1':
                                                    
                                                        print('\t\t-|.upper()|-')
                                                        print('____________________________________________')
                                                        print('\tConverts string to uppercase' \
                                                        '\nExample:' \
                                                        '\n\t"Marc".upper()' \
                                                        '\nOuput:' \
                                                        '\n\tMARC')
                                                        print('____________________________________________')
                                                    
                                                        while True:
                                                            exit = input('\n Type exit to return to the String Methods Menu--> ').lower().strip()
                                                            if exit == 'exit':
                                                                os.system('cls')
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
                                                                os.system('cls')
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
                                                        '\n\t\"marc".capitalize()' \
                                                        '\nOuput:' \
                                                        '\n\tMarc')
                                                        print('___________________________________________________')
                                                        while True:
                                                            exit = input('\n Type exit to return to the  String Methods Menu. ').lower()
                                                            if exit == 'exit':
                                                                os.system('cls')
                                                                break
                                                            else:
                                                                print('INVALID INPUT, try again')
                                                                continue
                                                    elif string_method == '4':
                                                        print('\t\t-|.title()|-')
                                                        print('________________________________________________')
                                                        print('  Capitalizes the first letter of each word' \
                                                        '\n\nExample:' \
                                                        '\n\t"lean marc g alcala".title()' \
                                                        '\nOuput:' \
                                                        '\n\tLean Marc G Alcala')
                                                        print('________________________________________________')
                                                        while True:
                                                            exit = input('\n Type exit to return to the String Method Menu. ').lower()
                                                            if exit == 'exit':
                                                                os.system('cls')
                                                                break
                                                            else:
                                                                print('INVALIsD INPUT, try again')
                                                                continue
                                                    elif string_method == '5':
                                                        print('\t\t-|.strip()|-')
                                                        print('____________________________________________')
                                                        print('   Removes spaces from the start and end' \
                                                        '\n\nExample:' \
                                                        '\n\t" hi ".strip()' \
                                                        '\nOuput:' \
                                                        '\n\thi')
                                                        print('____________________________________________')
                                                        while True:
                                                            exit = input('\n Type exit to return to the Strinf Method Menu. ').lower()
                                                            if exit == 'exit':
                                                                os.system('cls')
                                                                break
                                                            else:
                                                                print('INVALID INPUT, try again')
                                                                continue
                                                    elif string_method == '6':#need na babalik sa data types menu d sa main menu
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
                                        print('\tprint(123)\n\tname = -456\n\t789')
                                        print('________________________________________________')
                                        
                                        exit = input('\nType exit to return to the print Data Types menu. ').lower()
                                        os.system('cls')
                                        while True:
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
                                    print('a data type in used to represent numbers with\n decimal points (fractional numbers) 3.14,\n-0.11, or 2.0.')

                                    example = input('Do you want an example (YES or NO)--> ').lower()

                                    if example == 'yes':
                                        print('\nExample:')
                                        print('\tprint(1.23)\n\tnumber = -0.0456\n\t10.0')
                                        print('______________________________________________')

                                        exit = input('\nType exit to return to the print Data Types menu. ').lower()
                                        os.system('cls')
                                        while True:
                                            if exit == 'exit':
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue

                                    elif example == 'no':
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue
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

                
                                        exit = input('\nType exit to return to the print Data Types menu. ').lower()
                                        os.system('cls')
                                        while True:
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
                                    print('\t\t-|DICTIONARY|-')
                                    print('___________________________________________________________________')
                                    print('a data structure that stores information in key–value \npairs.Each key has a corresponding value, and you \nuse the key to access the value.')

                                    example = input('Do you want an example (YES or NO)--> ').lower()

                                    if example == 'yes':
                                        print('\nExample:')
                                        print('\tstudent = {"name":"Lean","age": 18,"course":"BSIT"}')
                                        print('\nAccessing Dictionary Values')
                                        print('\n\tprint(student["name"])\n\tprint(student["age"])')
                                        print('Output:\n\tLean\n\t18')
                                        print('\nAdding New Key-Value Pair')
                                        print('\n\tstudent["section"]="B"\n\tprint(student)')
                                        print('Output:\n\t{"name": "Lean", "age": 18, "section": "B"}')
                                        print('\nChangin an Existing Value')
                                        print('\n\tstudent["section"]="A"')
                                        print('Output:\n\t{"name": "Lean", "age": 18, "section": "A"}')
                                        print('_________________________________________________________')
                                        exit = input('\nType exit to return to the print Data Types menu. ').lower()
                                        os.system('cls')
                                        while True:
                                            if exit == 'exit':
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue

                                    elif example == 'no':
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                elif _data_types == '6':
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
                                elif _data_types == '7':
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
                while True:
                    print('\t\t\t-|OPERATORS|-')
                    print('________________________________________________________________')
                    print('Operators are symbols or keywords used to perform operations on\nvalues or variables.')
                    print('\n Types of Operators')
                    print('1. Arithmetic Operators')
                    print('2. Assigment Operators')
                    print('3. Relational Operators')
                    print('4. Logical Operators')
                    print('5. Back to Main Menu')
                    print('________________________________________________________________')

                    opera = input('Select an option from the above--> ').strip()
                    os.system('cls')
                
                    if opera == '1':
                        while True:
                            print('\t-|ARITHMETIC OPERATORS|-')
                            print('_____________________________________') 
                            print(' Used for mathematical operations.')
                            print('\nA. Addition (+)')
                            print('B. Subtraction (-)')
                            print('C. Multiplicaltion (*)')
                            print('D. Division (/)')
                            print('E. Floor Division (//)')
                            print('F. Modulus (%)')
                            print('G. Exponent (**)')
                            print('H. Exit')
                            print('_____________________________________') 
                            a_opera = input('Selet an option from the above--> ').lower().strip()
                            os.system('cls')
                            
                            if a_opera == 'a':
                                while True:
                                    print('\t\t-ADDITION-')
                                    print('______________________________________________')
                                    print('+ operator to add numbers, combine strings, or\njoin lists.')
                                    example = input('\nDo you want an example(YES  or NO)-->').lower().strip()
                                    
                                    
                                    if example == 'yes':
                                        print('Example:')
                                        print('\ta = 6\n\tb = 3\n\tc = 5')
                                        print('\n\tsum = a + b\n\ttotal = a + b + c\n\tprint(sum)\n\tprint(total)\n\tprint("Hello" + "World")')
                                        print('Output:\n\t9\n\t14\n\tHello World')
                                        print('_____________________________________') 
                                        while True:
                                            exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                            if exit == 'exit':
                                                os.system('cls')
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue
                                        break
                                    elif example == 'no':
                                        os.system('cls')
                                        break
                                    else:
                                        print('INVALID INPUT,try again')
                                        continue
                            elif a_opera == 'b':
                                while True:
                                    print('\t-|SUBTRACTION|-')
                                    print('_____________________________________') 
                                    print(' - operator to subtract numbers.')
                                    example = input('\nDo you want an example(YES  or NO)-->').lower().strip()
                                    
                                        
                                    if example == 'yes':
                                        print('Example:')
                                        print('\ta = 6\n\tb = 3\n\tc = 2')
                                        print('\n\ttotal = a - b\n\ttotals = a - b - c\n\n\tprint(total)\n\tprint(totals)')
                                        print('Output:\n\t3\n\t1')
                                        print('_____________________________________') 
                                        while True:
                                            exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                            if exit == 'exit':
                                                os.system('cls')
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue
                                        break
                                    elif example == 'no':
                                        os.system('cls')
                                        break
                                    else:
                                        print('INVALID INPUT,try again')
                                        continue
                            elif a_opera == 'c':
                                while True:
                                    print('\t-|MULTIPLICATION|-')
                                    print('_____________________________________') 
                                    print('  * operator to multiply numbers.')
                                    example = input('\nDo you want an example(YES  or NO)-->').lower().strip()
                                    
                                        
                                    if example == 'yes':
                                        print('Example:')
                                        print('\ta = 6\n\tb = 3\n\tc = 2')
                                        print('\n\ttotal = a * b\n\ttotals = a * b * c\n\n\tprint(total)\n\tprint(totals)')
                                        print('Output:\n\t18\n\t36')
                                        print('_____________________________________') 
                                        while True:
                                            exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                            if exit == 'exit':
                                                os.system('cls')
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue
                                        break
                                    elif example == 'no':
                                        os.system('cls')
                                        break
                                    else:
                                        print('INVALID INPUT,try again')
                                        continue
                            elif a_opera == 'd':
                                while True:
                                    print('\t-|DIVISION|-')
                                    print('_____________________________________') 
                                    print(' / operators use to divide numbers and\nalways returns a float (may have decimal).')
                                    example = input('\nDo you want an example(YES  or NO)-->').lower().strip()
                                    
                                        
                                    if example == 'yes':
                                        print('Example:')
                                        print('\ta = 12\n\tb = 3\n\tc = 2')
                                        print('\n\ttotal = a / b\n\ttotals = a / b / c\n\n\tprint(total)\n\tprint(totals)')
                                        print('Output:\n\t4.0\n\t1.3')
                                        print('_____________________________________') 
                                        while True:
                                            exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                            if exit == 'exit':
                                                os.system('cls')
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue
                                        break
                                    elif example == 'no':
                                        os.system('cls')
                                        break
                                    else:
                                        print('INVALID INPUT,try again')
                                        continue
                            elif a_opera == 'e':
                                while True:
                                    print('\t-|FLOOR DIVISION|-')
                                    print('_____________________________________') 
                                    print('// operator use to divide numbers and\ngives the whole number only (cuts off the decimal). ')
                                    example = input('\nDo you want an example(YES  or NO)-->').lower().strip()
                                    
                                        
                                    if example == 'yes':
                                        print('Example:')
                                        print('\ta = 12\n\tb = 3\n\tc = 2')
                                        print('\n\ttotal = a // b\n\ttotals = a // b // c\n\n\tprint(total)\n\tprint(totals)')
                                        print('Output:\n\t4\n\t1')
                                        print('_____________________________________') 
                                        while True:
                                            exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                            if exit == 'exit':
                                                os.system('cls')
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue
                                        break
                            elif a_opera == 'f':
                                while True:
                                    print('  \t-|MODULUS|-')
                                    print('_____________________________________') 
                                    print(' "%" returns the remainder when you \n divide one number by another.')
                                    example = input('\nDo you want an example(YES  or NO)-->').lower().strip()
                                    
                                        
                                    if example == 'yes':
                                        print('Example:')
                                        print('\ta = 12\n\tb = 3\n\tc = 5')
                                        print('\n\ttotal = a "%" b\n\ttotals = a "%" c\n\n\tprint(total)\n\tprint(totals)')
                                        print('Output:\n\t0\n\t4')
                                        print('_____________________________________') 
                                        while True:
                                            exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                            if exit == 'exit':
                                                os.system('cls')
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue
                                        break
                            elif a_opera == 'g':
                                while True:
                                    print('  \t-|EXPONENT|-')
                                    print('_____________________________________') 
                                    print(' ** operator to raise a number to a \npower.')
                                    example = input('\nDo you want an example(YES  or NO)-->').lower().strip()
                                    
                                        
                                    if example == 'yes':
                                        print('Example:')
                                        print('\ta = 12\n\tb = 3\n\tc = 5')
                                        print('\n\ttotal = a ** b\n\ttotals = a ** c\n\n\tprint(total)\n\tprint(totals)')
                                        print('Output:\n\t1728\n\t248832')
                                        print('_____________________________________') 
                                        while True:
                                            exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                            if exit == 'exit':
                                                os.system('cls')
                                                break
                                            else:
                                                print('INVALID INPUT, try again')
                                                continue
                                        break
                            elif a_opera == 'h':
                                break
                            else:
                                print('INVALID INPUT,try again')
                                continue
                            continue
                    elif opera == '2':
                        while True:
                            print('\t\t-|ASSIGNMENT OPERATORS|-')
                            print('___________________________________________________________')
                            print('Assignment operators are used to store values in variables.\nSome also update the value (add, subtract, multiply, etc.) \nand then assign it.')
                            print('\nA. Simple Assignment ')
                            print('B. Add and Assign')
                            print('C. Subtract and Assign')
                            print('D. Multiply and Assign')
                            print('E. Divide and Assign')
                            print('F. Floor Divide and Assign')
                            print('G. Modulus and Assign')
                            print('H. Exponent and Assign')
                            print('I. Exit')
                            print('___________________________________________________________')

                            ass_opera = input('Select an option from the above--> ').lower().strip()
                            os.system('cls')  

                            if ass_opera == 'a':
                                while True:
                                    print('\t-|SIMPLE ASSIGN|-')
                                    print('_________________________________')
                                    print(' Assigns a value to a variable.')

                                    print('Example:\n\tx = 5')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'b':
                                while True:
                                    print('\t-|ADD AND ASSIGN|-')
                                    print('__________________________________')
                                    print('Adds a value and stores the result \nin the same variable.')

                                    print('Example:\n\tx = 5\n\tx += 6')
                                    print('Output:\n\t11')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'c':
                                while True:
                                    print('\t-|SUBTRACT AND ASSIGN|-')
                                    print('__________________________________')
                                    print('Subtract a value and stores the result \nin the same variable.')

                                    print('Example:\n\tx = 5\n\tx -= 6')
                                    print('Output:\n\t1')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'd':
                                while True:
                                    print('\t-|MULTIPLY AND ASSIGN|-')
                                    print('__________________________________')
                                    print('Multiply a value and stores the result \nin the same variable.')

                                    print('Example:\n\tx = 5\n\tx *= 6')
                                    print('Output:\n\t30')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'e':
                                while True:
                                    print('\t-|DIVIDE AND ASSIGN|-')
                                    print('__________________________________')
                                    print('Divide a value and stores the result \nin the same variable.')

                                    print('Example:\n\tx = 5\n\tx /= 3')
                                    print('Output:\n\t1.6')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'f':
                                while True:
                                    print('\t-|FLOOR DIVIDE AND ASSIGN|-')
                                    print('__________________________________')
                                    print('Floor divide a value and stores the result \nin the same variable.')

                                    print('Example:\n\tx = 5\n\tx //= 3')
                                    print('Output:\n\t1')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'g':
                                while True:
                                    print('\t-|MODULUS AND ASSIGN|-')
                                    print('__________________________________')
                                    print('Modulus a value and stores the result \nin the same variable.')

                                    print('Example:\n\tx = 5\n\tx %= 6')
                                    print('Output:\n\t83')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'h':
                                while True:
                                    print('\t-|EXPONENT AND ASSIGN|-')
                                    print('__________________________________')
                                    print('Exponent a value and stores the result \nin the same variable.')

                                    print('Example:\n\tx = 5\n\tx **= 6')
                                    print('Output:\n\t15625')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif ass_opera == 'i':
                                break
                        else:
                            print('INVALID INPUT,try again')
                            continue
                        continue
                    elif opera == '3':
                        while True:
                            print('\t\t-|RELATIONAL OPERATOR|-')
                            print('____________________________________________________________')
                            print('Relational operators are also called comparison operators.\nThey conpare two values and always return True or False.')
                            print('A. == (Equal To)')
                            print('B. != (Not Equal To)')
                            print('C. > (Greater Than)')
                            print('D. < (Less Than)')
                            print('E. >= (Greater Than or Equal)')
                            print('F. <= (Less Than or Equal)')
                            print('G. exit')
                            print('____________________________________________________________')

                            re_opera = input('Select an option from the above--> ').lower().strip()
                            os.system('cls')

                            if re_opera == 'a':
                                while True:
                                    print('\t\t-|EQUAL TO|-')
                                    print('__________________________________________')
                                    print('Checks if two values are exactly the same.\nReturns True if equal, otherwise False.')
                                    print('Example:\n\tprint(4 == 4)\n\tprint(4 == 5)\nOutput:\n\tTrue\n\tFalse')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif re_opera == 'b':
                                while True:
                                    print('\t\t-|NOT EQUAL TO|-')
                                    print('__________________________________________')
                                    print('Checks if two values are different.Returns\nTrue if NOT equal, otherwise False.')
                                    print('Example:\n\tprint(4 != 4)\n\tprint(4 != 5)\nOutput:\n\tFalse\n\tTrue')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif re_opera == 'c':
                                while True:
                                    print('\t\t-|GREATER THAN|-')
                                    print('__________________________________________')
                                    print('Checks if the value on the left is greater\nthan the value on the right.')
                                    print('Example:\n\tprint(4 > 4)\n\tprint(2 > 6)\n\tprint(5 > 4)\nOutput:\n\tFalse\n\tFalse\n\tTrue')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif re_opera == 'd':
                                while True:
                                    print('\t\t-|LESS THAN|-')
                                    print('__________________________________________')
                                    print('Checks if the value on the left is less \nthan the value on the right.')
                                    print('Example:\n\tprint(4 < 4)\n\tprint(6 < 2)\n\tprint(4 < 5)\nOutput:\n\tFalse\n\tFalse\n\tTrue')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif re_opera == 'e':
                                while True:
                                    print('\t-|GREATER THAN OR EQUAL TO|-')
                                    print('__________________________________________')
                                    print('Checks if the value on the left is greater\nthan or equal to the value on the right.')
                                    print('Example:\n\tprint(4 >= 4)\n\tprint(6 >= 2)\n\tprint(4 >= 5)\nOutput:\n\tTrue\n\tTrue\n\tFalse')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif re_opera == 'f':
                                while True:
                                    print('\t-|LESS THAN OR EQUAL TO|-')
                                    print('_____________________________________________')
                                    print('Checks if the value on the left is less than \nor equal to the value on the right.')
                                    print('Example:\n\tprint(4 <= 4)\n\tprint(6 <= 2)\n\tprint(4 <= 5)\nOutput:\n\tTrue\n\tFalse\n\tTrue')
                                    print('_____________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif re_opera == 'g':
                                break
                            else:
                                print('INVALID INPUT,try again')
                                continue
                            continue
                    elif opera == '4':
                        while True:
                            print('\t\t-|LOGICAL OPERATOR|-')
                            print('___________________________________________________________')
                            print('Logical operators are used to combine multiple conditions \nor reverse them.They always return True or False.')
                            print('\nA. and')
                            print('B. or')
                            print('C. not')
                            print('D. Exit')
                            print('___________________________________________________________')
                            lo_opera = input('Select an option from the above--> ').lower().strip()
                            os.system('cls')

                            if lo_opera == 'a':
                                while True:
                                    print('\t\t-|and|-')
                                    print('___________________________________________')
                                    print(' Returns True if both conditions are True.')
                                    print('\nExample:\n\tprint((5 >3)and(10 > 7))\n\tprint((5 > 3)and(2 > 7))')
                                    print('Output:\n\tTrue\n\tFalse')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif lo_opera =='b':
                                while True:
                                    print('\t\t-|or|-')
                                    print('___________________________________________')
                                    print(' Returns True if at least one condition is \nTrue.')
                                    print('\nExample:\n\tprint((5 >3)or(2 > 7))\n\tprint((1 > 3)or(2 > 7))\n\tprint((5 > 6)or(9 > 6))')
                                    print('Output:\n\tTrue\n\tFalse\n\tTrue')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif lo_opera =='c':
                                while True:
                                    print('\t\t-|not|-')
                                    print('___________________________________________')
                                    print(' Reverses the truth value of a condition.')
                                    print('\nExample:\n\tprint(not (5 > 3))\n\tprint(not (1 > 3)or(2 > 7))\n\tprint(not (5 > 6)and(9 > 6))')
                                    print('Output:\n\tFalse\n\tTrue\n\tTrue')
                                    print('_________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Arithmetic Operators--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif lo_opera =='d':
                                break
                            else:
                                print('INVALID INPUT, try again')


                        continue
                    elif opera == '5':
                        break
                    else:
                        print('INVALID INPU,try again')
                        continue
                    continue
            elif choice == 'd':
                while True:
                    print('\t\t\t-|CONDITIONALS|-')
                    print('________________________________________________________________')
                    print('Conditional statements allow a program to make decisions based \non conditions.They let Python choose what code to\nrun depending on whether a condition is True or False.')
                    print('\nTypes of Conditional Statements')
                    print('A. if Statement')
                    print('B. if...else Statement')
                    print('C. if...elif...else Statement')
                    print('D. Nested if Statements')
                    print('E. Exit')
                    print('________________________________________________________________')

                    condi = input('Select an option from the above--> ').lower().strip()
                    os.system('cls')

                    if condi == 'a':
                        while True:
                            print('\t\t-|if Statement|-')
                            print('__________________________________________________')
                            print('Executes a block of code only if the condition is \nTrue.')
                            print('\nExample:\
                                \n\tx = 10\n\tif x > 5:\n\t\tprint("x is greater than 5")')
                            print('Output:\n\tx is greater than 5')
                            while True:
                                exit = input('\n Type exit to return to the Conditionals Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif condi == 'b':
                        while True:
                            print('\t\t-|if...else Statement|-')
                            print('__________________________________________________')
                            print('  Provides an alternative block of code if the \n  condition is False.')
                            print('\nExample:\
                                \n\tx = 3\n\tif x > 5:\n\t\tprint("x is greater than 5")\n\telse:\n\t\tprint("x is less than 5")')
                            print('Output:\n\tx is less than 5')
                            while True:
                                exit = input('\n Type exit to return to the Conditionals Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif condi == 'c':
                        while True:
                            print('\t\t-|if...elif...else Statement|-')
                            print('_______________________________________________________')
                            print(' Checks multiple conditions in sequence.The first True\ncondition\'s block is executed, and the rest are skipped.')
                            print('Example:\
                                \n\tx = 5\n\tif x > 5:\n\t\tprint("x is greater than 5")\n\telif x == 5:\n\t\tprint("x is exactly 5")\n\telse:\n\t\tprint("x is less than 5")')
                            print('Output:\n\tx is exactly 5')
                            while True:
                                exit = input('\n Type exit to return to the Conditionals Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif condi == 'd':
                        while True:
                            print('\t\t-|Nested if Statements|-')
                            print('_______________________________________________________')
                            print(' An if statement inside another if statement, used for \nmore complex decision-making.')
                            print('Example:\
                                \n\tu_name = "marc"\n\tp_word = "1234"\n\tif u_name == "marc":\n\t\tif p_word == "1234"\n\t\t   print("Login succesfull")\n\t\telse:\n\t\t   print(Wrong password)\n\telse:\n\t   print("Username not found")')
                            print('Output:\n\tLogin succesfully')
                            while True:
                                exit = input('\n Type exit to return to the Conditionals Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif condi == 'e':
                        break
                    else:
                        print('INVALID INPUT, try again')

                continue
            elif choice == 'e':
                while True:
                    print('\t\t\t-|LOOPS|-')
                    print('_________________________________________________________________')
                    print('A loop is a programming structure that allows a block of code to\nbe repeated multiple times as long as a certain condition is true \nor while there are items to process.')
                    print('\nTypes of loop')
                    print('A. for loop')
                    print('B. while loop')
                    print('C. Exit')
                    print('_________________________________________________________________')

                    lo = input('Select an option from the above--> ').lower().strip()
                    os.system('cls')

                    if lo == 'a':
                        
                        print('\t\t-|for loop|-') 
                        print('__________________________________________________')
                        print('for loop is a control structure in Python used to\nrepeat a block of code for each item in a sequence,\nsuch as a range of numbers, a list, a string, or \nany iterable object.')
                        example = input('\nDo you want an example (YES or NO)--> ').lower().strip()
                        while True:
                            if example == 'yes':
                                print('\nExample:\n\tfor ikot in range(1,11,1):\n\t   print( ikot,"hello world") ')
                                print('Output:\n\thello world\n\thello world\n\thello world\n\thello world\n\thello world\n\thello world\n\thello world\n\thello world\n\thello world\n\thello world')
                                print('\nExample:\n\ttotal = 0\n\tfor i in range(1,6):\n\t   total += i\n\tprint("Total",total)')
                                print('Output:\n\t15')
                                print('\nExample:\n\tfor i in range(1,11,1):\n\tprint(i, end=" ")')
                                print('Output:\n\t12345678910')
                                while True:
                                    exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                    if exit == 'exit':
                                        os.system('cls')
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue
                                break
                            elif example == 'no':
                                os.system('cls')
                                break
                            else:
                                print('INVALID INPUT, try again ')
                    elif lo == 'b':
                    
                        print('\t\t-|while loop|-') 
                        print('__________________________________________________')
                        print('A while loop repeatedly executes a block of code \nas long as a specified condition is true.')
                        example = input('Do you want an example (YES or NO)--> ').lower().strip()
                        while True:
                            if example == 'yes':
                                print('\nExample:\n\tcount = 5\n\twhile count > 0:\n\t   print("Countdown:", count)\n\t   count -= 1')
                                print('Output:\n\tCountdown: 5\n\tCountdown: 4\n\tCountdown: 3\n\tCountdown: 2\n\tCountdown: 1')
                                while True:
                                    exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                    if exit == 'exit':
                                        os.system('cls')
                                        break
                                    else:
                                        print('INVALID INPUT, try again')
                                        continue
                                break
                            elif example == 'no':
                                os.system('cls')
                                break
                            else:
                                print('INVALID INPUT,try again')
                                continue
                    elif lo == 'c':
                        break
                    else:
                        print('INVALID INPUT, try again')
                        continue     
            elif choice == 'f':
                while True:
                    print('\t\t\t-|LIST|-')
                    print('_________________________________________________________________')
                    print('list is a data structure in Python used to store multiple items \nin a single variable.You can store numbers, strings, booleans,\nor mixed data types inside a list.\n\nA list is written using square brackets:')
                    print('\n\tmy_list = [1,2,3,4,5]')
                    print('\nCharacteristic:\n\tOrdered → Items have index positions\n\tMutable → You can change or update items\n\tAllows duplicates\n\tCan store different data types\n\tUse index')
                    print('\nExample with mixed data:\n\n\tmixed_list = ["Lean", 18 , True , 1.25]')
                    print('_________________________________________________________________')
                    print('\nCommon List Operations')               
                    print('A. Append')
                    print('B. Insert')
                    print('C. Remove')
                    print('D. Pop')
                    print('E. Length')
                    print('F. Sort')
                    print('G. Reverse')
                    print('H. More')
                    print('I. Back to main menu')
                    print('____________________________________________')

                    li = input('Select an option from the above--> ').lower().strip()
                    os.system('cls')

                    if li == 'a':
                        while True:
                            print('\t\t\t-|Append|-')
                            print('_________________________________________________________________')
                            print(' \t\t    Adds an item to the end')
                            print('syntax:\n\tlist.append(item)')
                            print('\nExample:\n\tsub_1st_sem = ["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\tprint(sub_1st_sem)\n\tsub_1st_sem.append("MMW")\n\tprint(sub_1st_sem)\nOutput:\n\t["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\t["STS","EU1","ITCS101","ITCS102","ITPS101","MMW"]')
                            print('_________________________________________________________________')
                            while True:
                                exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif li == 'b':
                        while True:
                            print('\t\t\t-|Insert|-')
                            print('_________________________________________________________________')
                            print(' \t\t Inserts item at specified index')
                            print('syntax:\n\tlist.insert(index,item)')
                            print('\nExample:\n\tsub_1st_sem = ["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\tprint(sub_1st_sem)\n\tsub_1st_sem.insert(0,"MMW")\n\tprint(sub_1st_sem)\nOutput:\n\t["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\t["MMW","STS","EU1","ITCS101","ITCS102","ITPS101"]')
                            print('_________________________________________________________________')
                            while True:
                                exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif li == 'c':
                        while True:
                            print('\t\t\t-|Remove|-')
                            print('_________________________________________________________________')
                            print(' \t\t Removes first occurrence of item')
                            print('syntax:\n\tlist.remove(item)')
                            print('\nExample:\n\tsub_1st_sem = ["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\tprint(sub_1st_sem)\n\tsub_1st_sem.remove("ITCS101")\n\tprint(sub_1st_sem)\nOutput:\n\t["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\t["STS","EU1","ITCS102","ITPS101"]')
                            print('_________________________________________________________________')
                            while True:
                                exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif li == 'd':
                        while True:
                            print('\t\t\t-|Pop|-')
                            print('_________________________________________________________________')
                            print(' \t\t Removes and returns item at index')
                            print('syntax:\n\tlist.pop(index)')
                            print('\nExample:\n\tsub_1st_sem = ["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\tprint(sub_1st_sem)\n\tsub_1st_sem.append("MMW")\n\tprint(sub_1st_sem)\n\tsub_1st_sem.pop()print(sub_1st_sem)\nOutput:\n\t["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\t["STS","EU1","ITCS101","ITCS102","ITPS101","MMW"]\n\t["STS","EU1","ITCS101","ITCS102","ITPS101"]')
                            print('_________________________________________________________________')
                            while True:
                                exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif li == 'e':
                        while True:
                            print('\t\t\t-|Length|-')
                            print('_________________________________________________________________')
                            print(' \t\t   Returns number of elements')
                            print('syntax:\n\tlen(list)')
                            print('\nExample:\n\tsub_1st_sem = ["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\tprint(len(sub_1st_sem))\nOutput:\n\t5')
                            print('_________________________________________________________________')
                            while True:
                                exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif li == 'f':
                        while True:
                            print('\t\t\t-|Sort|-')
                            print('_________________________________________________________________')
                            print(' \t\t Sorts the list (ascending by default)')
                            print('syntax:\n\tlen(list)')
                            print('\nExample:\n\tsub_1st_sem = ["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\tprint(sub_1st_sem)\n\tsub_1st_sem.sort()\n\tprint(sub_1st_sem)\nOutput:\n\t["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\t["EU1","ITCS101","ITCS102","ITPS101","STS"]')
                            print('_________________________________________________________________')
                            while True:
                                exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif li == 'g':
                        while True:
                            print('\t\t\t-|Reverse|-')
                            print('_________________________________________________________________')
                            print(' \t\t    Reverses the list order')
                            print('syntax:\n\tlist.reverse()')
                            print('\nExample:\n\tsub_1st_sem = ["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\tprint(sub_1st_sem)\n\tsub_1st_sem.reverse()\n\tprint(sub_1st_sem)\nOutput:\n\t["STS","EU1","ITCS101","ITCS102","ITPS101"]\n\t["ITPS101","ITCS102","ITCS101","EU1","STS"]')
                            print('_________________________________________________________________')
                            while True:
                                exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                if exit == 'exit':
                                    os.system('cls')
                                    break
                                else:
                                    print('INVALID INPUT, try again')
                                    continue
                            break
                    elif li == 'h':
                        while True:
                            print('__________________________________')
                            print('1. Iterating Through a List')
                            print('2. List Slicing')
                            print('3. Indexing')
                            print('4. Exit')
                            print('__________________________________')

                            more = input('Select an option from the above--> ').strip()
                            os.system('cls')

                            if more == '1':
                                while True:
                                    print('\t-|Iterating Through a List|-')
                                    print('__________________________________________')
                                    print('Iterating means looping through each item \nin a list, one by one.')
                                    print('\nExample:\n\tanimals = ["cat","dog","rabbit"]\n\tfor animal in animals:\n\t   print(animal)\nOutput:\n\tcat\n\tdog\n\trabbit')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif more == '2':
                                while True:
                                    print('\t-|List Slicing|-')
                                    print('__________________________________________')
                                    print('List slicing allows you to get a portion \n(slice) of a list')
                                    print('\nExample:\n\tpets = ["cat","dog","rabbit","bird","fish","hamster","duck"]\n\tprint(pets[1:4])\nOutput:\n\t["dog","rabbit","bird","fish"]')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break

                            elif more == '3':
                                while True:
                                    print('\t-|Indexing|-')
                                    print('__________________________________________')
                                    print('Indexing means accessing a specific item \nin a list using its index number.')
                                    print('\nExample:\n\tpets = ["cat","dog","rabbit","bird","fish","hamster","duck"]\n\tprint(pets[5])\n\tprint(-3)\nOutput:\n\thamster\n\tfish')
                                    print('__________________________________________')
                                    while True:
                                        exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                                        if exit == 'exit':
                                            os.system('cls')
                                            break
                                        else:
                                            print('INVALID INPUT, try again')
                                            continue
                                    break
                            elif more == '4':
                                break
                            else:
                                print('INVALID INPUT,try again')
                    elif li == 'i':
                        break
                    else:
                        print('INVALID INPUT,try again')
                        continue



                continue
            elif choice == 'g':
                while True:
                    print('\t\t\t-|FUNCTION|-')
                    print('__________________________________________________________________________________________')
                    print('A function is a block of reusable code that performs a specific task.You can call (run) \nthe function whenever you want, which helps avoid repeating the same code.')
                    print('\nDefine a Function\nUse the keyword def, then the function name followed by parentheses () and a colon :')
                    print('\n\tdef greet():\n\t   print("Hello, boi")')
                    print('\nTo call a funtion\nAfter defining, run the function by writing its name with parentheses:')
                    print('\n\tgreet()\nOutput:\n\tHello, boi')
                    print('\nFunction with Parameters(inputs)\nYou can pass data to a function using parameters:')
                    print('\n\tdef greet(name):\n\t   print("Hello," + name)\n\n\tgreet(Lean)')
                    print('Output:\n\tHello, Lean')
                    print('\nFunction with Return Value\nFunctions can return a value using the return statement:')
                    print('\n\tdef add(a,b):\n\t   return a + b\n\n\tresult = add(4,7)\n\tprint(result)')
                    print('Output:\n\t11')
                    print('\nFunction with Default Parameters\nYou can set default values for parameters:')
                    print('\n\tdef greet(name="Guest"):\n\t   print("Hello," + name)\n\n\tgreet()\n\tgreet("Lean")')
                    print('Output:\n\tHello, Guest\n\tHello, Lean')
                    print('__________________________________________________________________________________________')
                    while True:
                        exit = input('\n Type exit to return to the Loops Menu--> ').lower().strip()
                        if exit == 'exit':
                            os.system('cls')
                            break
                        else:
                            print('INVALID INPUT, try again')
                            continue
                    break
            elif choice == 'h':
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
                    exit = input('\n Type exit to return to the Main  menu. ').lower()
                    os.system('cls')
                    if exit == 'exit':
                        break
                    else:
                        print('INVALID INPUT, try again')
                        continue
            elif choice == 'i':
                break
            else:
                print('Invalid input, please try again')
        break
    elif explore == 'no':
        break
    else:
        print('INVALID INPUTt,try again')
        continue                          
