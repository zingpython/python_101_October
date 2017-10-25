# print("Hello World!")
# print("How are you")

# name = "Art"
# print("My name is", name)

time = int(input("What time is it?"))
# print("line 5",type(time))
# time = int(time)
# print("line 7",type(time))

list_of_friends = ["Mark", "Emily", "John"]

for name in list_of_friends:
	if time < 7:
		print("Hello", name, "party starts at 7pm")
	elif time == 7:
		print("Hello", name, "you are right on time")
	else:
		print("Hello", name, "you are late")
