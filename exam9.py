from sys import argv

script, user_name = argv
prompt ='- '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I Have some questions for you."
print "Do you drink beer %s?" % user_name
likes = raw_input(prompt)

print "What food are you going to eat tonight %s?" % user_name
food = raw_input(prompt)

print "What filipino food you don't like to eat again?"
fili = raw_input(prompt)

print """
Alright, so you said %r so let's drink again next time.
Wow I love %r too. Enjoy your dinner.
I see, so top eating %r. HAHAHHAHAH.

""" % (likes, food, fili)