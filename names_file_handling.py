#obj1 - read data from name_data and use that data to print msg to user
#obj2 - get input from user and add that to the name_data

#to store "name:nick_name" pair in a dictionary
import csv
names_list = []

#give user options : read, write or Exit
def main():
    while True:
        user_choice = int(input("What do you want to do?\n1. Read   2. Write    3.Exit      --> Reply only 1, 2 or 3 -- "))
        match user_choice:
            case 1: 
                read_list()

            case 2:
                write_list()
        
            case 3:
                print("Exiting...")
                break
                


#read
#open/read file and save it in a var, 2 data in a row so split and store in 2 var and then use them to print msg
def read_list():
    with open("name_data.csv") as names:
            names_list = []
            reader = csv.reader(names)      #using reader func of csv to split values replacing old split method
            for name, nick_name in reader:
                name_row = {"name" : name, "nick_name" : nick_name}
                #names["name"] = name --> shortning the process of defining and then assigning value in names dictionary to line 32
                #names["nick_name"] = nick_name
                names_list.append(name_row)        #this appends to already existing list each time it runs, without deleting last data - SOLVED by assigning a blank list before the for loop (line 28)

    name_selected = str(input("Please enter the name to check for(Case Sensitive) -- "))
    trial = 0
    for name_line in names_list:
        trial +=1
        if name_selected == name_line["name"] :     
            print(f"Nick name of {name_selected} is {name_line["nick_name"]}")
            break
        elif trial <= len(names_list):
            continue
        else:       #this prints below msg each time until it finds the match - SOLVED by continuing the checking loop until trail numbers exceeds the length of the list (line 44)
            print("Name doesn't exist in the directory")
            break
             

#write
#get user input for 2 data, and then apppend it to the name_data
def write_list():
  while True:
    print("You're about to enter a new name")
    name = str(input("Enter the name -->"))
    nick_name = str(input("Enter the nick name -->"))
    YN = int(input(f"You entered {name} and {nick_name}\nIs this correct? 1.Yes  2.No -->"))
    if YN == 1 :
        with open("name_data.csv", "a") as file:
            file.write(f"{name},{nick_name}")
            print("Name entered succefully, going back to Main Menu")
        break
    else :
        YN_2 = int(input("Incorrect entry... 1.Try again  2.Main Menu -->"))
        if YN == 1:
            continue
        elif YN == 2:
            break
        else :
            print("only enter 1 or 2")
  

#Error Handling: 1> make sure user gives 2 data, it can be anything - NO NEED  2> Do i need to compare appended value to user input - PROB NOT


if __name__ == "__main__":
    main()