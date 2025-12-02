import os
import json


print("STUDENT RECORD INFPRMATION")
print("===========================")

student_record = {}

while True:
    print("A - add student record")
    print("B - print all student record")
    print("C - search student record")
    print("D - delete student record")
    print("E - edit student record")
    print("F -  export student record")
    print("G - exit system")

    choice = input('Select from the optin above: ').lower()



    if choice == 'a':
        os.system('cls')
        print('ADDING STUDENT RECORD')
        print('______________________________')

        id_no = input('Please input your student number: ')

        f_name = input('Plese input your first name here: ').upper()
        l_name = input('Please input your last name here: ').upper()
        age = input('Please input your age here: ')
        section = input('Please input your section here: ').upper()
        course = input('Please input your course here: ').upper()

        student_record[id_no] = [f_name,l_name,age,section,course]
        print('DATE SAVED SUCCESSFULLY')
        continue
    elif choice == 'b':
        os.system('cls')
        print('PRINTING STUDENT RECORD')
        print('______________________________')

        for i, j in student_record.items():
            print(f'STUDENT NUMBER: \n\t{i} \nINFORMATION \n\t{j}')
        continue
    elif choice == 'c':
        os.system('cls')
        print('SEARCH STUDENT RECORD')
        print('______________________________')

        search_stu_no = input('Enter a student number for search: ')

        for each_no in student_record.keys():
            if search_stu_no in student_record.keys():
                print('RECORD FOUND')
                checking = input('Would you like to check (yes or no ): ').lower()
                if checking == 'yes':
                    print(f'STUDENT NUBER: \n\t{search_stu_no}')
                    print('IFORMATION')
                    for i in student_record[search_stu_no]:
                        print(f'\t{i}')
                    break
                
            else:
                print('RECORD NOT FOUND')
        continue
    elif choice == 'd':
        os.system('cls')
        print('DELETE STUDENT RECORD')
        print('______________________________')

        search_stu_no = input('Enter a student number for DELETING: ')

        if search_stu_no  in student_record.keys():
                print(f'STUDENT NUMBER \n\t{search_stu_no}')
                print('INFORMATION')
                for i in student_record[search_stu_no]:
                    print(f'\t{i}')
                
                student_record.pop(search_stu_no)
                print('STUDENT RECORD DELETED')
        else:
            print('Student Number not FOUND')
        continue

    elif choice == "e":
        os.system('cls')
        print("EDIT/MODIFY STUDENT RECORD")

        search_id = input("Input students ID for search").lower()
        
        if search_id in student_record:
            print("=================================")
            print(f"\n\n RECORD FOUND {search_id}")
            #to find the record for the search id
            for i in student_record[search_id]:
                print(f"--- {i}")
            print("=================================")
            fisrt_name = input("please input student first name --> ").upper()
            second_name = input("please input student second name --> ").upper()
            age = input("input your age --> ")
            course = input("input your course --> ").upper()
            section = input("enter your section -->").upper()

            student_record[search_id][0] = fisrt_name
            student_record[search_id][1] = second_name
            student_record[search_id][2] = age
            student_record[search_id][3] = course
            student_record[search_id][4] = section

            print("DATA UPDATED")
            continue
        else:
            print("NO RECORD FOUND")
        break
        continue
    elif choice == "f":
        os.system('cls')
        print("EXPORT STUDENT DATA")
        print('______________________________')

        #json java script object notation

        with open('student_records.json', 'w') as new_file:
            json.dump(student_record,new_file, indent=4)
        continue
    elif choice == "g":
        os.system('cls')
        continue
    else:
        print("INVALID INPUT, please try again")
        continue


