import tempfile
import os

def get_user_scores():
    while True:
        try:
            first_score = int(input("Player 1: Enter your score: "))
            second_score= int(input("Player 2: Enter your score: "))
            third_score= int(input("Player 3: Enter your score: "))
            return first_score, second_score, third_score
        except:
            print("Error: NaN")

def get_user_new_score():
    while True:
        try:
            new_first_score = int(input(" Player 1: Enter your new score: "))
            new_second_score = int(input("Player 2:Enter your new score: "))
            new_third_score = int(input("Player 3: Enter your new score: "))
            return new_first_score, new_second_score, new_third_score
        except:
            print("Error: NaN")

def get_add_score(first1, first2, first3, second1, second2, second3):
    player1_final = first1 + second1
    player2_final = first2 + second2
    player3_final = first3 + second3
    return player1_final, player2_final, player3_final

def get_download_score(final1, final2, final3):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, "Score.txt")
    with open(temp_path, "w") as f:
        f.write(f"The first players combined score was {final1}\nThe second players combined score was {final2}\n The third players combined score was {final3}")
    get_read_score()

def get_read_score():
    while True:
        read_score = input("Would you like to read your file (Y/n): ")
        if read_score.lower() == "y":
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, "Score.txt")
            with open(temp_path, "r") as f:
                value = f.read()
                print(value)    
            break
        elif read_score.lower() == "n":
            print("Ok goodbye!")
            exit()
        else:
            read_score = input("please select (y/n): ")
            
def get_save_score(final1, final2, final3):
    download_scores = input("Would you like to download you scores, (Y/N): ")
    while True:
            if download_scores.lower() == "y":
                get_download_score(final1, final2, final3)
                break

            elif download_scores.lower() == "n":
                print("Ok, Goodbye!")
                break
            else:
                download_scores = input("Please select (Y/N): ")
        

first1, first2, first3 = get_user_scores()
second1, second2, second3 = get_user_new_score()
final1, final2, final3 = get_add_score(first1, first2, first3, second1, second2, second3)
Save_score = get_save_score(final1, final2, final3)
