from app import App
from file_manager import FileManager
import json



class UI:
    def __init__(self):
        self.app = App()

    def _print_menu(self):
        print("\t\tPeople List Application")
        print("\n")
        print("\t1. Add New Person")
        print("\t2. List People")
        print("\t3. Delete Person")
        print("\t4. Exit")
        print("\n")

    def _process_menu_choice(self):
        user_input = input("Enter Menu Choice: ")

        match(user_input[0]):
            case "1": self.add_person()
            case "2": self.list_people()
            case "3": self.delete_person()
            case "4": quit()
            case _: print("Invalid menu choice!")

    def start_ui(self):
        while True:
            self._print_menu()
            self._process_menu_choice()


    def add_person(self):
        first_name = input("First Name: ")
        middle_name = input("Middle Name: ")
        last_name = input("Last Name: ")
        self.app.add_person(first_name=first_name, middle_name=middle_name, \
                            last_name=last_name)


    def list_people(self):
      with open("people_list.json", "r") as f:
        json_file = json.load(f)
        i=1
        for entry in json_file:
          print(f"Customer number {i}")
          print("First name: ", json_file[entry].get("firstName"))
          print("Last name: ", json_file[entry].get("lastName"))
          print("\n\n")
          i=i+1 

    def delete_person(self):  
      delete_person= input("Please input last name of customer to delete?: ")
      with open("people_list.json", "r") as f:
          json_file = json.load(f)

          if delete_person in json_file:
             json_file.pop(delete_person)

             with open("people_list.json", "w") as delete:
                data1 = json.dump(json_file, delete)
                print("Sucessfully deleted")



      #  new_data =[]
       # with open("people_list.json", "r") as f:
        #  json_file = json.load(f)
        
  #      i = (f"customer number {i}")
   #     for entry in json_file:
    #       if i ==int(delete_person):
     #         del json_file[i]
      #  with open ("people_list.json", "w") as f:
       ##  print(new_data)
            

    
    
    

           
      

         
     
         


         
      
      
  


