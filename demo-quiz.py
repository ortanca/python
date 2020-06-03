#question

class Question():
	def __init__(self, text, choice, answer):
		self.text = text
		self.choice = choice
		self.answer = answer
	def kontrol(self, answer):
		return self.answer == answer


#quiz

class Quiz:
	def __init__(self, questions):
		self.questions = questions
		self.score = 0
		self.questionIndex = 0
	

	def getquestion(self):
		return self.questions[self.questionIndex]
	def displayquestion(self):
		question = self.getquestion()
		print(f'soru{self.questionIndex + 1 }: {question.text}')
		
		for q in question.choice:
			print('-'+ q)

		answer = input('cevap: ')
		print(question.kontrol(answer))
		self.guess(answer)
		self.loadquestion()
	def guess(self, answer):
		question = self.getquestion()

		if question.kontrol(answer):
			self.score += 1
		self.questionIndex += 1

		self.displayquestion()
	def loadquestion(self):

		if len(self.questions) == self.questionIndex:
			self.showsore()
		else:
			self.displayprogress()
			self.displayquestion()
	def showscore(self):
		print(f"score {self.score}")
	def displayprogress(self):
		totalquestion = len(self.questions)
		questionnumber = self.questionIndex + 1

		if questionnumber > totalquestion:
			print('quiz bitti')
		else:
			print(f" question {questionnumber} of {totalquestion}".center(100, '*'))






q1 = Question('ben kimim', ['ahmet', 'yasin', 'burak','abdullah', 'zehra'], 'ahmet')
q2 = Question('sen kimsin', ['ahmet', 'yasin', 'burak','abdullah', 'zehra'], 'ahmet')	
q3 = Question('o kim', ['ahmet', 'yasin', 'burak','abdullah', 'zehra'], 'ahmet')			
questions = [q1,q2,q3]

quiz = Quiz(questions)
question = quiz.getquestion()
quiz.loadquestion()

