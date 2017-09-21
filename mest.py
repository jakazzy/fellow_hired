class School:


	def __init__(self, eits="", fellows=""):
		self.eits = eits
		self.fellows = fellows

class Person:


	def __init__(self, name, nationality):
		self.name = name
		self.nationality = nationality


class Eits(Person):


	 def __init__(self, name, nationality):
	 	super().__init__(name, nationality)

		
	 def __repr__(self):
	 	return '{} <{}, {}>'.format(type(self).__name__, self.name, self.nationality)

	 def funfacts(self, facts):
	 	print("{r} loves {s}".format(r=self.name, s=facts))


class Fellow(Person):
	

	fellows_hired = 0
	def __init__(self, name, nationality, happiness_level):
		super().__init__(name, nationality)
		self.happiness_level = happiness_level
		Fellow.fellows_hired += 1

		
	def check_fellows(self):
		if Fellow.fellows_hired < 5:
			print('it ok')
		else:
			raise Exception("you cant hire more than 4 fellow")

	def eating_abilities(self):
		print("Ability of {a} to eat increases {c}".format(a=self.name, c=self.happiness_level))

	def teaching_abilities(self):
		print("Teaching by {d} decreases {e}".format(d=self.name, e=self.happiness_level))




if __name__ == "__main__":

	fellow = Fellow('Andrew', 'USA', 5)
	fellow = Fellow('faddai', 'GH', 5)
	fellow = Fellow('Edem', 'GH', 5)
	fellow = Fellow('Miishe', 'USA - GH', 5)
	fellow = Fellow('simpiwe', 'SA', 5)
	fellow.check_fellows()
	# mest_school = School()

	# merci = Fellow(Person).name(Kwesi)



	# jida = Eits("jida", "Ghanaian")
	# print("Eit {f}, {g}".format(f=jida.name, g=jida.nationality))

	
	# facts_fun = input("What do you love doing?: \n")
	# print(jida)
	# EIT <Jida, Ghanaian>
