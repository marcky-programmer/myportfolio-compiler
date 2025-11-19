import os
import json

print("student information racord")
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

    choice = input("select from the option-->").lower()

    if choice == "a":
        os.system('cls')
        print("\n ADDING STUDENT RECORD")

        id_no = input("please input student ID number --> ")

        fisrt_name = input("please input student first name --> ").upper()
        second_name = input("please input student second name --> ").upper()
        age = input("input your age --> ")
        course = input("input your course --> ").upper()
        section = input("enter your section -->").upper()

        student_record[id_no] = [fisrt_name,second_name,age,course,section]
        print("DATA SAVED SUCCESFULLY")
        continue
    elif choice == "b":
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        
        for i, j in student_record.items(): #key - vlues
            print(f"STUDENT ID - {i}, INFORMATION - {j}")


        continue
    elif choice == "c":
        os.system('cls')
        print("SEARCH STUDENT RECORD")

        search_id = input("Input students ID for search").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("=================================")
                print(f"\n\n RECORD FOUND {search_id}")
                #to find the record for the search id
                for i in student_record[search_id]:
                    print("=================================")

            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == "d":
        os.system('cls')
        print("DELETE STUDENT RECORD")

        search_id = input("Input students ID for search").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("=================================")
                print("\n\n RECORD FOUND")
                #to find the record for the search id
                for i in student_record[search_id]:
                    print(f"--- {i}")
                print("=================================")

                student_record.pop(search_id)
                print("\n RECORD DELETED")

                

            else:
                print("NO RECORD FOUND")
            break
        
        continue
    elif choice == "e":
        os.system('cls')
        print("EDIT/MODIFY STUDENT RECORD")

        search_id = input("Input students ID for search").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
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
                        

            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == "f":
        os.system('cls')
        print("EXPORT STUDNET DATA")

        #json java script object notation

        with open('student_records.json', 'w') as new_file:
            json.dump(student_record,new_file, indent=4)
        continue
    elif choice == "g":
        pass
        continue
    else:
        print("INVALID INPUT, please try again")
        continue



