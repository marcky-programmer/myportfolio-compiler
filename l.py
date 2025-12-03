import os

print('\t\tCODE PYTHON COMPILER')
user_name = input('\nPlease input your name here: ').title()
os.system('cls')

explore = input(f'Hello {user_name} would you like to explore this system (yes or no): ').lower()
os.system('cls')

if explore == 'yes':
    answer = True

    while answer:     # MAIN MENU LOOP
        print('\t\t|WELCOME TO MY SYSTEM|')
        print('________________________________________________________________')
        print(' In this system you will learn the fundamental concepts in Python')
        print('________________________________________________________________')

        print('\nMAIN MENU')
        print('A. Print Statements')
        print('B. Variables')
        print('C. Operators')
        print('D. Conditionals')
        print('E. Loops')
        print('F. Lists')
        print('G. Function')
        print('H. Exit the system')

        choice = input('Select from the option above: ').lower()
        os.system('cls')

        # =========================================================
        # ==================== PRINT STATEMENT =====================
        # =========================================================
        if choice == 'a':
            print('\t\t\t-|PRINT STATEMENT|-')
            print('\nA print statement in Python is used to display variables, objects, '
                  '\nor text to the output device (screen). The print() function is '
                  '\ncommonly used for displaying messages on the screen.')

            while True:  # EXAMPLE LOOP
                example = input('\nDo you want an example? YES or NO --> ').lower()

                if example == 'yes':
                    print('\nprint("Hello World")')
                    print('The output is:')
                    print('Hello World')

                    gagawin = input('\nDo you want to try? YES or NO --> ').lower()
                    if gagawin == 'yes':
                        user_input = input('Input a phrase or word here --> ')
                        print(f'\nThe output is:\n{user_input}')

                        # ================================
                        # PRINT FUNCTION MENU STARTS HERE
                        # ================================
                        while True:
                            print('\nPRINT FUNCTION MENU')
                            print('1. Printing Text')
                            print('2. Printing Numbers')
                            print('3. Printing Multiple Items')
                            print('4. Printing Variables')
                            print('5. Printing with Formatting')
                            print('6. Try Coding')
                            print('7. Back to MAIN MENU')

                            explore_pri_func = input('Choose an option --> ')

                            # ------------------------------
                            # PRINTING TEXT
                            # ------------------------------
                            if explore_pri_func == '1':
                                print('\n\t\tPRINTING TEXT')
                                print('______________________________________________________________')
                                print('To print text, put it inside quotation marks.')
                                print('\nExample:')
                                print('  print("I want to learn Python")')
                                print('Output:')
                                print('  I want to learn Python')
                                print('______________________________________________________________')

                                input('\nPress ENTER to return...')

                            # ------------------------------
                            # PRINTING NUMBERS
                            # ------------------------------
                            elif explore_pri_func == '2':
                                print('\n\t\tPRINTING NUMBERS')
                                print('____________________________________________________________')
                                print('You can print numbers directly without quotes.')
                                print('\nExample:')
                                print('  print(23)')
                                print('  print(2.5)')
                                print('Output:')
                                print('  23')
                                print('  2.5')
                                print('____________________________________________________________')

                                input('\nPress ENTER to return...')

                            # ------------------------------
                            # PRINTING MULTIPLE ITEMS
                            # ------------------------------
                            elif explore_pri_func == '3':
                                print('\n\t\tPRINTING MULTIPLE ITEMS')
                                print('___________________________________________________________')
                                print('You can print several items at once using commas.')
                                print('\nExample:')
                                print('  print("Age:", 18)')
                                print('  print("Sum:", 7+3)')
                                print('Output:')
                                print('  Age: 18')
                                print('  Sum: 10')
                                print('___________________________________________________________')

                                input('\nPress ENTER to return...')

                            # ------------------------------
                            # PRINTING VARIABLES
                            # ------------------------------
                            elif explore_pri_func == '4':
                                print('\n\t\tPRINTING VARIABLES')
                                print('______________________________________________________________')
                                print('You can print values stored in variables.')
                                print('\nExample:')
                                print('  name = "Marc"')
                                print('  age = 18')
                                print('  print(name)')
                                print('  print(age)')
                                print('______________________________________________________________')

                                input('\nPress ENTER to return...')

                            # ------------------------------
                            # PRINTING WITH FORMATTING
                            # ------------------------------
                            elif explore_pri_func == '5':
                                print('\n\t\tPRINTING WITH FORMATTING')
                                print('______________________________________________________________')
                                print('Format strings make output cleaner.')
                                print('\nExample:')
                                print('  name = "Marc"')
                                print('  age = 18')
                                print("  print(f'My name is {name} and I am {age} years old.')")
                                print('Output:')
                                print('  My name is Marc and I am 18 years old.')
                                print('______________________________________________________________')

                                input('\nPress ENTER to return...')

                            # ------------------------------
                            # TRY TO CODE (EXEC)
                            # ------------------------------
                            elif explore_pri_func == '6':
                                print('\n-|TRY IT YOURSELF|-')
                                print('Type your Python code. Type RUN on a new line to execute.')

                                collection_code = []

                                while True:
                                    line = input('>>> ')
                                    if line.strip().upper() == 'RUN':
                                        break
                                    collection_code.append(line)

                                code = '\n'.join(collection_code)
                                print('\nOUTPUT:')

                                try:
                                    exec(code)
                                except Exception as e:
                                    print('Error:', e)

                                print('\nEnd of code.')
                                input('\nPress ENTER to return...')

                            # ------------------------------
                            # GO BACK TO MAIN MENU
                            # ------------------------------
                            elif explore_pri_func == '7':
                                os.system('cls')
                                break  # break out of PRINT FUNCTION MENU

                            else:
                                print('INVALID INPUT, try again.')

                        break  # break example-trying loop

                    elif gagawin == 'no':
                        break

                    else:
                        print('INVALID INPUT, try again.')

                elif example == 'no':
                    break

                else:
                    print('INVALID INPUT, try again.')

        # =========================================================

        elif choice == 'h':
            print("Thank you for using the system!")
            break

        else:
            print("Invalid input, try again.")
