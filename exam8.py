from sys import argv

script, filename = argv

txt = open(filename)

print "Your filename is %r:" % filename
print txt.read()


print "Type the filename again here:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

