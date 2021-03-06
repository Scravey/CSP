"""

Directions: Create a Python module named csp1-4-1c.py.  Add the following code to the module.  Do not forget to test!!!
1.	Define a class named Animal. This class should have one attribute and one method:
    a.	gender
    b.	A getGender() method that returns the value of gender.

2.	Create a constructor for the Animal class that:
    a.	Accepts the value gender as a parameter and sets the gender attribute.
    b.	Prints the value of the gender attribute using the getGender() method.

3.	Create an instance of the Animal class passing gender value into it.

4.	Define a class named Mammal. This class must be a subclass of the Animal class.
    a.	Attributes:
        i.	isWarmBlooded
        ii.	weight
    b.	Methods:
        i.  getWarmBlooded()
        ii.	setWarmBlooded()
        iii.	getWeight()
        iv.	setWeight()
        v.	move()  -  Just print “Mammal Moves” in this method for the moment.
        vi.	makeNoise()  - Just print “Mammal Makes a Noise”

5.	Create a constructor for the Mammal class that:
    a.	Accepts the values gender, isWarmBlooded, and weight as parameters and
            sets the appropriate attributes.
    b.	Prints the values of gender, isWarmBlooded, and weight using the
            appropriate “get” methods.

6.	Define a class named Feline. This class must be a subclass of the Mammal class.
    a.	Attributes:
        i.	age
        ii.	type
        iii.	isDangerous
    b.	Methods:
        i.	Getters and setters for all three attributes above.
7.	Create a constructor for the Feline class that:
    a.	Accepts the values age, type, isDangerous as parameters and sets the
            appropriate attributes.
    b.	Prints the values of age, type, and isDangerous, using the appropriate
             “get” methods.

8.	Define a class named Canine. This class must be a subclass of the Mammal class.
    a.	Attributes:
        i.	age
        ii.	breed
        iii.	runSpeed
    b.	Methods:
        i.	Getters and setters for all three attributes above.

9.	Create a constructor for the Canine class that:
    a.	Accepts the values age, breed, runSpeed as parameters and sets the
            appropriate attributes.
    b.	Prints the values of age, breed, and runSpeed, using the appropriate
            getter methods.

10.	Create the makeNoise() method in both the Feline and Canine classes. The method
        should print “Feline says purr” and “Canine says Woof” respectively.

*** Test your Classes ***
*** Test your Classes ***

It is a good idea to test as you go, but now we want to test the entire set of
    classes.

1.	Create an instance of Animal class using “female” as the gender

2.	Create an instance of the Mammal class that is warm blooded and weighs 110
        pounds.
    a.	Set the value of the gender attribute using the setGender() method.
    b.	Print the gender of your mammal using the getGender() method.
    c.	Print the value of isWarmBlooded and the weight using the appropriate
        getter methods.

3.	Create an instance of the Feline class that is two years old, a Tiger, and
    is dangerous.
    a.	Set the value of the gender attribute using the setGender() method.
    b.	Print the gender of your mammal using the getGender() method.
    c.	Set the values of isWarmBlooded and the weight using the appropriate
        setter methods.
    d.	Print the value of isWarmBlooded and the weight using the appropriate
        getter methods.
    e.	Print the values of the age, type and isDangerous attributes using the
        appropriate getter methods.

4.	Create an instance of the Canine class that is two years old, a Labrador, and
    has a runSpeed of 18 MPH.
    a.	Set the value of the gender attribute using the setGender() method.
    b.	Print the gender of your mammal using the getGender() method.
    c.	Set the values of isWarmBlooded and the weight using the appropriate setter
        methods.
    d.	Print the value of isWarmBlooded and the weight using the appropriate getter
        methods.

5.	Print the values of the age, breed and runSpeed attributes using the appropriate
    getter methods.

6.	Call the makeNoise() and move() methods for the following object instances you
    created above:
    a.	Mammal
    b.	Feline
    c.	Canine

"""