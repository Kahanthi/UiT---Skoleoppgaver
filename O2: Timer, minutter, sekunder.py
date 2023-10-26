user_input = int(input("Enter total seconds:  "))

hours = user_input // 3600
minutes = (user_input % 3600) // 60
seconds = user_input % 60

formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
print("the total time is:", formatted_time) 