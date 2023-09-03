#1

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(list(my_text)))

# 2
i = 5
achive_lenth = 0
while i > 0:
    line_without_a = input("Insert longest sentence withot'a':\n")
    check_lane = list(line_without_a)
    if "a" in check_lane:
        print("WITHOUT a!, try from start")
        break
    else:
        current_lenth = int(len(check_lane))
    if achive_lenth < current_lenth:
        achive_lenth = current_lenth
        print("Congratilation! You achived new score: " + str(achive_lenth))
    elif achive_lenth >= current_lenth :
        print(f"Try Again.\nYour current score: {current_lenth}.\nYour Best score: {achive_lenth}" )