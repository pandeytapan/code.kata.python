MINUTES_IN_A_DAY = 1440

first_time = int(input("Enter the first time (HHMM): "))
second_time = int(input("Enter the second time (HHMM): "))

# Should convert the times to the minutes

first_time_in_minutes = first_time // 100 * 60 + first_time % 100
second_time_in_minutes = second_time // 100 * 60 + second_time % 100

total_duration  = (second_time_in_minutes - first_time_in_minutes + MINUTES_IN_A_DAY ) % MINUTES_IN_A_DAY
print("%02d:%02d" % (total_duration / 60, total_duration % 60))
