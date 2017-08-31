name = 'Zed A. Shaw'
age = 35 
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

pound2kg = weight * 2.2
inch2cm = height * 2.54
print "In kg %f" % pound2kg
print "In cm %f" % inch2cm
print "Testing %r" % name