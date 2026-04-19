import os
import tempfile
temp_dir = tempfile.gettempdir()
temp_path = os.path.join(temp_dir, f"a")


def file_storage(temp_dir, temp_path):
   print("Some file options we have today include:\nDogs(1)\nCats(2)\nprograming(3)\nSports(4)")
   filetype = int(input(""))
   while True:
        if filetype == 1:
            temp_path = os.path.join(temp_dir, f"Dogs.txt")
            with open(temp_path, "w") as f:
             f.write("Dogs are mans best friends!")
             print(f"The file has been downloaded at {temp_path}")
             again()
             break
        elif filetype == 2:
            temp_path = os.path.join(temp_dir, "Cats.txt")
            with open(temp_path, "w") as f:
             f.write("Cats are really mean!")
             print(f"The file has been downloaded at {temp_path}")
             again()
             break
        elif filetype == 3:
            temp_path = os.path.join(temp_dir, "Programing.txt")
            with open(temp_path, "w") as f:
             f.write("Programing is a pain in the ass to learn!")
             print(f"The file has been downloaded at {temp_path}")
             again()
             break
            
        elif filetype == 4:
            temp_path = os.path.join(temp_dir, "Sports.txt")
            with open(temp_path, "w") as f:
             f.write("The best sport is baseball!")
             print(f"The file has been downloaded at {temp_path}")
             again()
             break
        else:
           filetype = int(input("Please select a valid option, Dogs(1)\nCats(2)\nprograming(3)\nSports(4)"))

def again():
   while True:
      another = input("Would you like to download another file? (yes/no): ")
      if another == "yes":
         file_storage(temp_dir, temp_path)
         break
      elif another == "no":
         print("Thanks for taking a look goodbye!")
         exit()
      else:
         another = input("Please select (yes/no)")
         
file = input("Would you like to browse some files today? (yes/no): ")

while True:
    if file == "yes":
        file_storage(temp_dir, temp_path)
        break
    elif file == "no":
        print("Goodbye!")
        break
    else:
        file = input("Please type (yes/no)! ")
