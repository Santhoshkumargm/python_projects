import random
import art
import game_data

print(art.logo)
g_data = game_data.data
g_list = ["name", "follower_count", "description", "country"]
continue_game = True
win_counter = 0


def check_result(user_dict, choice_A_dict, choice_B_dict, user_choice):
    u_choice_name = user_dict[user_choice]
    choice_A_name = choice_A_dict[g_list[0]]
    choice_B_name = choice_B_dict[g_list[0]]
    if u_choice_name == choice_A_name and choice_A_dict[g_list[1]] > choice_B_dict[g_list[1]]:
        return True
    elif u_choice_name == choice_B_name and choice_A_dict[g_list[1]] < choice_B_dict[g_list[1]]:
        return True
    else:
        return False


while continue_game:
    if win_counter == 0:
        choice_A = random.choice(g_data)
    print(f"Compare A: {choice_A[g_list[0]]}, a {choice_A[g_list[2]]}, from {choice_A[g_list[3]]}")
    print(art.vs)
    choice_B = random.choice(g_data)
    if choice_A[g_list[0]] == choice_B[g_list[0]]:
        choice_B = random.choice(g_data)
    print(f"Against B: {choice_B[g_list[0]]}, a {choice_B[g_list[2]]}, from {choice_B[g_list[3]]}")
    user_choice_check = {"A": choice_A[g_list[0]], "B": choice_B[g_list[0]]}
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    result = check_result(user_choice_check, choice_A, choice_B, user_choice)
    if result:
        win_counter += 1
        print(art.logo)
        print(f"You're right! Current score: {win_counter}")
        if user_choice == "B":
            choice_A = choice_B
            continue_game = True
    else:
        print(art.logo)
        print(f"Sorry. that's wrong. Final score: {win_counter}")
        continue_game = False
