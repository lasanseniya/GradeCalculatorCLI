# Author: Lasan Seniya Ranatunge

# Date: 4/16/2023 



#Initializing variables
credit_total = 0
progress_list = []

#Calculate outcomes
def outcome( pass_credits, defer_credits, fail_credits ):
    if pass_credits == 120:
        print("Progress","\n")
        progress_list.append(f"{'Progress - '} {pass_credits},{defer_credits},{fail_credits}")
                
    elif pass_credits == 100:
        print("Progress (module trailer)","\n")
        progress_list.append(f"{'Progress (module trailer) - '} {pass_credits},{defer_credits},{fail_credits}" )
    
    elif fail_credits >= 80:
        print("Exclude","\n")
        progress_list.append(f"{'Exclude - '} {pass_credits},{defer_credits},{fail_credits}" )

    else:
        print("Do not progress - module retriever","\n")
        progress_list.append(f"{'module retriever - '} {pass_credits},{defer_credits},{fail_credits}" )


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


#Validating student id
def is_id_valid( prompt ): 
    while True:
        student_id = input(prompt).lower()
        if len(student_id) == 8 and student_id[0] == "w" and student_id[1:].isdigit():
            return student_id  #if not returned it won't be accessible within outcomes function
            
        else:
            print('Invalid student id')
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



            
print("""
          =-----------------------------------------= 
          |  Part 4 - Dictionary (separate program) |  
          =-----------------------------------------= 


""")


student_data = {}
active = True 
while active:
    student_id = is_id_valid("Enter student id: ")
    
    while True:
        validate_user_credits()
        outcome( credit_pass,credit_defer,credit_fail )
        student_data[student_id] = progress_list[-1]
        
        print("\nWould you like to enter another set of data?")
        new_inputs = is_valid("Enter 'y' for yes or 'q' to view dictionary: ",'yq')

        if new_inputs == 'y':
            print(" ")
            break

        else:
            print("\n\n")
            for key, value in student_data.items():
                print(f"{key} : {value}")
            active = False
            break