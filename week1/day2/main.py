# type conversion 

a = 100;
b = bool(a);
c = float(a);
d = str(a);

print(a," ",b," "," ",c," ",d);


# f-string
# name = input("Enter your name:");
# age = int(input("Enter your age:"));

# print(f"Your name is {name} and your age is {age}");

# Basic Arithmetic in Python

a = 15;
b = 5;

print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) # Floor Division
print(a%b) # Modulus
print(a**b) # power

# String Methods in Python

# .upper() and .lower()
text = "Hello";
print(text.upper());
print(text.lower());

#.strip() (remove spaces)

text = "   Hello   ";
print(text.strip());

#.replace()

text = "I like java";
print(text.replace("java","python"));

# .split() (convert string to list)

text = "apple banana mango";
print(text.splgit push origin main
it());

#.find()"index of first a" and .count() "how many a's"

text = "Banana"
print(text.find("a"),text.count("a"));

# .startswith() and .endswith()

text = "python.py";
print(text.startswith("py"));
print(text.endswith("py"));

# capitalize()
text = "hello world";
print(text.capitalize());

# isdigit(), isalpha(), isalnum()

text = "123";
print(text.isdigit());
text = "abc";
print(text.isalpha());
text = "abc123";
print(text.isalnum());

# join()

words = ["I", "love", "Python"]
print(" ".join(words));

# format()
name = "Ali";
print("Hello {}".format(name));