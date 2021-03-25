import string, random



class Password:

	def __init__(self,default=None, \
		Length= None, print_info=None):
		

		self.info = print_info
		if Length != None:

			while 4 > Length or Length > 30:
				Length = int(input("[*]Enter The Length of the Password: "))

				if Length < 4:
					print("[*]Length should be greater than or Equal to 4!") 
				elif Length > 30:
					print("[*]Length should be lesser than or Equal to 30!") 
			
			self.length = int(Length)
		elif Length == None:
			default = True
		
		if default:
			self.length = random.randint(4, 23)

		self.default = default
		self.simple_algo()
		if self.info == True:
			if self.default:
				print(f"[*]Your Default Password is: {self.password}")
				print(f"""
	Uppercase   :{self.uppercase} 
	Lowercase   :{self.lowercase}
	Digits      :{self.digits}
	Punctuation :{self.punctuation}
	""")
			else:
				print(f"[*]Your Password is: {self.password}")
				print(f"""
	Uppercase   :{self.uppercase} 
	Lowercase   :{self.lowercase}
	Digits      :{self.digits}
	Punctuation :{self.punctuation}
	""")





	def simple_algo(self):
		letters = string.ascii_uppercase 
		letters_lower = string.ascii_lowercase 
		st_digits = string.digits 
		st_punct = string.punctuation


		letters = list(letters)
		letters_lower = list(letters_lower)
		st_digits = list(st_digits)
		st_punct = list(st_punct)


		random.shuffle(letters)
		random.shuffle(letters_lower)
		random.shuffle(st_digits)
		random.shuffle(st_punct)

		uppercase = self.length //3
		lowercase = self.length // 4
		digits = self.length // 4
		punctuation =self.length - (lowercase + digits + uppercase)


		shuffle_lis = [uppercase, lowercase, digits,punctuation]
		random.shuffle(shuffle_lis)
		random.shuffle(shuffle_lis)

		uppercase, lowercase, digits, punctuation = shuffle_lis
		self.uppercase, self.lowercase, self.digits, self. punctuation = shuffle_lis


		password = ''.join(random.choice(letters) for i in range(uppercase)) \
		+ ''.join(random.choice(letters_lower) for i in range(lowercase))\
		+ ''.join(random.choice(st_digits) for i in range(digits))\
		+ ''.join(random.choice(st_punct) for i in range(punctuation))

		password = list(password)
		random.shuffle(password)
		password = ''.join(password)
		self.password = password



	def __str__(self):
		return self.password


if __name__ == "__main__":
	passw = Password(Length=44, print_info=False) # if print_info=True It will print the information of of the given password
	# Password(default=True) will give default password length from 4 to 23
	# Password(Length=12) Length stands for length of the password you want
	print(passw)
	

