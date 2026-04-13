seconds = int(input("Enter the duration in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")