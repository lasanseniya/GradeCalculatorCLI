# Author: Lasan Seniya Ranatunge

# Date: 4/16/2023 



import runpy

#Initializing variables
progress_list = []
progress_count = 0
retrieve_count = 0
trailer_count = 0
exclude_count = 0

#Calculate outcomes
def outcome( pass_credits, defer_credits, fail_credits, mode):
    global progress_count, trailer_count, exclude_count, retrieve_count
    if pass_credits == 120:
        print("Progress","\n")
        if mode == 't':
            progress_count += 1
            progress_list.append(f"{'Progress - '} {pass_credits},{defer_credits},{fail_credits}")
        
    elif pass_credits == 100:
        print("Progress (module trailer)","\n")
        if mode == 't':
            trailer_count += 1
            progress_list.append(f"{'Progress (module trailer) - '} {pass_credits},{defer_credits},{fail_credits}" )
        
    elif fail_credits >= 80:
        print("Exclude","\n")
        if mode == 't':
            exclude_count += 1
            progress_list.append(f"{'Exclude - '} {pass_credits},{defer_credits},{fail_credits}" )

    else:
        print("Do not progress - module retriever","\n")
        if mode == 't':
            retrieve_count += 1
            progress_list.append(f"{'Module retriever - '} {pass_credits},{defer_credits},{fail_credits}" )


#Get credit inputs and check total
def validate_user_credits():
    global credit_total,credit_fail,credit_defer,credit_pass
    while True:
        credit_total = 0
        credit_pass = is_credit_valid("Please enter your credits at pass: ")
        credit_defer = is_credit_valid("Please enter your credits at defer: ")
        credit_fail = is_credit_valid("Please enter your credits at fail: ")
        
        if credit_total == 120:
            break
        else:
            print("Total incorrect.")
            continue

#Menu choice validation
def validate_menu_option( prompt ):
    char = ['s','t','d','q']
    while True:
        menu_choice = input(prompt).lower()
        if menu_choice in char: 
            return menu_choice
        
        else:
            print("Invalid choice...")
            continue        

#Credit inputs validation
def is_credit_valid( prompt ):     
    global credit_total
    valid_range = list(range(0, 121, 20))
    while True:  #endless loop
        try:      
            credit_input = int(input(prompt))
            
        except ValueError:           
            print("Integer required", "\n")
            continue
        
        if credit_input in valid_range:
            credit_total += credit_input
            return credit_input  #returns if the credit input is valid..

        else:
            print("Out of range.", "\n")
            continue

#Validating user input for y/n and y/q
def is_valid( prompt, options ):    
    while True:
        choice = input(prompt).lower()
        valid_choice = list(options)
        if choice in valid_choice:
            return choice
        else:
            print(f"Please enter {options[0]} or {options[1]} as input")
            continue
        

if __name__ == "__main__":  #Entry point (main thread)
    menu_state = True
    while menu_state == True:                
        print("""
                  Student_Progression (Extended Version)
        """)

        print("""
                +---------------------------------------+                   
                |                Menu                   |           
                |                                       |        
                |       Student Version  - press  s     |         
                |       Staff Version    - press  t     |         
                |       Dictionary       - press  d     |     
                |       Quit program     - press  q     |        
                |                                       |
                +---------------------------------------+                                              
        """)


        choice = validate_menu_option("Enter your choice: ")

        if choice == 's':
            while True:
                validate_user_credits()
                outcome( credit_pass,credit_defer,credit_fail,'s' )
                back_to_menu = is_valid("Back to main menu?(y/n): ",'yn')
                if back_to_menu == 'y':
                    break
                else:
                    menu_state = False  #Avoids going back to main menu
                    break


        elif choice == 't':
            while True:
                validate_user_credits()
                outcome( credit_pass,credit_defer,credit_fail,'t')
                print("Would you like to enter another set of data?")
                new_inputs = is_valid("Enter 'y' for yes or 'q' to quit and view results: ",'yq')

                if new_inputs == 'y':
                    print(" ")
                    continue
                
                elif new_inputs == 'q':  #No further user inputs...
                    outcome_count = progress_count + trailer_count + retrieve_count + exclude_count
                    print("\n")
                    print("-------------------------------------------------------------------\n",)
                    print("Histogram","\n")
                    print("Progress", progress_count," :", progress_count * "*")
                    print("Trailer", trailer_count,"  :", trailer_count * "*")
                    print("Retriever", retrieve_count,":", retrieve_count * "*")
                    print("Excluded", exclude_count," :", exclude_count * "*","\n")
                    print(outcome_count, "outcomes in total.\n")
                    print("-------------------------------------------------------------------")
                    print(" ")
                    
                    print("Part 2:")
                    for credit_list in progress_list:
                        print(credit_list)
                    print("\n")
                        
                    file = open("progression_data.txt" , "w")
                    
                    for credit_list in progress_list:
                        file.write(f"{credit_list} \n")
                            
                    file.flush()
                    file.close()
                    file = open("progression_data.txt", "r")
                    output = file.read() 
                    file.close()
                    print("Part 3:")
                    print(output)
                    print("\n")
                    
                    back_to_menu = is_valid("Back to main menu?(y/n): ", 'yn')
                    if back_to_menu == 'y':
                        keep_data = is_valid("Do you want to keep the data entered in this staff session(y/n): ", 'yn')

                        if keep_data == 'n':    #Resets all the variables 
                            progress_list = []
                            progress_count = 0
                            retrieve_count = 0
                            trailer_count = 0
                            exclude_count = 0
                            
                        break
                    
                    else:
                        menu_state = False  #Avoids going back to main menu
                        break


        elif choice == 'd':
            runpy.run_path( path_name = 'dictionary.py') ####Runs dict.py

            back_to_menu = is_valid("\nBack to main menu?(y/n): ", 'yn')
            if back_to_menu == 'y':
                continue
            else:
                menu_state = False  #Avoids going back to main menu
                break

        else:        #If user input 'q' in the main menu
            break
        
    print("\nThank you for using Student_Progression(Extended version)... ")