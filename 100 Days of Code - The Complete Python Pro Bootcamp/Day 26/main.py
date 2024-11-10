
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# with open("file1.txt") as file1:
#     file1_list = file1.readlines()
#     new_file1 = []
#     for item in file1_list:
#         strip_item = item.strip()
#         new_file1.append(int(strip_item))
# print(new_file1)
#
# with open("file2.txt") as file2:
#     file2_list = file2.readlines()
#     new_file2 = []
#     for item in file2_list:
#         strip_item = item.strip()
#         new_file2.append(int(strip_item))
# print(new_file2)
#
# result = [n for n in new_file1 if n in new_file2]
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {weekday: temp_c * 9/5 + 32 for (weekday, temp_c) in weather_c.items()}
print(weather_f)
