Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> if 8>7
SyntaxError: invalid syntax
>>> if 8>7:
	print("what U want ")

	
what U want 
>>> 
>>> if 6 > 7 :
	print ("yep")
else:
	print (" nope :D )
	       
SyntaxError: EOL while scanning string literal
>>> if 6 > 7 :
	print ("yep")
else:
	print (" nope :D")

	
 nope :D
>>> var = "panda"
>>> var = 'panda'
>>> if var == "panda":
	print("cute")
elif var == "panda" :
	print ("regal")
else:
	print ("ugly betty")

	
cute
>>> if var == "pand":
	print("cute")
elif var == "panda" :
	print ("regal")
else:
	print ("ugly betty")

	
regal
>>> if var == "pand":
	print("cute")
elif var == "pandaa" :
	print ("regal")
else:
	print ("ugly betty")

	
ugly betty
>>> temp = 120
>>> if temp > 85:
	print("HOT")
elif temp > 100
SyntaxError: invalid syntax
>>> if temp > 85:
	print("hot")
elif temp > 100:
	print ("really hot")
elif temp > 60 ("normal ")
SyntaxError: invalid syntax
>>> if temp > 85:
	print("hot")
elif temp > 100:
	print ("really hot")
elif temp > 60 ("normal "):
else :
	
SyntaxError: expected an indented block
>>> if temp > 85:
	print("hot")
elif temp > 100:
	print ("really hot")
elif temp > 60:
	print ("cold a bit ")
else :
	print ("where are U ?? ")

	
hot
>>> temp = 40
>>> 
>>> 
>>> if temp > 85:
	print("hot")
elif temp > 100:
	print ("really hot")
elif temp > 60:
	print ("cold a bit ")
else :
	print ("where are U ?? ")

	
where are U ?? 
>>> money = 2000
>>> if money > 50:
	print(" I m Hilmi :D )
	      
SyntaxError: EOL while scanning string literal
>>> if money > 50:
	print(" I m Hilmi :D ")
else :
	print(" I m not Hilmi )
	      
SyntaxError: EOL while scanning string literal
>>> if money > 50:
	print(" I m Hilmi :D ")
else :
	print(" I m not Hilmi ")
		print ("but i will be in the future :D :D ")
		
SyntaxError: unexpected indent
>>> if money > 50:
	print(" I m Hilmi :D ")
else :
	print(" I m not Hilmi ")
	print ("but i will be in the future :D :D ")

	
 I m Hilmi :D 
>>> money = 43
>>> if money > 50:
	print(" I m Hilmi :D ")
else :
	print(" I m not Hilmi ")
	print ("but i will be in the future :D :D ")

	
 I m not Hilmi 
but i will be in the future :D :D 
>>> if money > 50:
	print(" I m Hilmi :D ")
else :
	print("	I m not Hilmi ")
	print ("    but i will be in the future :D :D ")

	
	I m not Hilmi 
    but i will be in the future :D :D 
>>> # I mean i hope :D
>>> 
