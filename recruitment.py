def main():
	#write your code here
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}
	cv['name'] = input("Please enter your name: ")
	cv['age'] = input("Please enter your age: ")
	cv['experience'] = input("Please enter your years of experience: ")
	cv['skills'] = []

	print("The skills are:")

	for skill in skills:
		print ((skills.index(skill)+1),' ',skill)

	print()
	user_skill = input("Please choose a skill from the list: ")

	if 0 < user_skill <= len(skills):
		cv['skills'].append(skills[user_skill-1])
	else:
		print("Invalid skill input, please try again")

	second_skill = input("Please choose a second skill: ")

	if 0 < second_skill <= len(skills) and second_skill != user_skill :
		cv['skills'].append(skills[second_skill-1])
	else:
		print("Invalid skill input, please try again")

	if 25 <= cv['age'] <=40 and cv['experience'] > 5 and skills[5] in cv['skills'] :
		print("accepted")
	else:
		print("rejected")


if __name__ == '__main__':
	main()
