import random

class flashcard:
	def __init__(self):
		self.fruits={'apple':'red','orange':'orange','watermellon':'green','banana':'yellow'}
	def quiz(self):
		while True:
			fruit,color = random.choice(list(self.fruits.items()))
			print(f"What is the color of {fruit}")
			user_answer = input().lower()
			if user_answer == color:
				print("Your answer is correct")
			else:
				print("Your answer is incorrect")
				
print("Welcome to Fruit quiz")
obj = flashcard()
obj.quiz()