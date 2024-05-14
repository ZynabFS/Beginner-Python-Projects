
class info:
    pass # we are writing 'pass' for the time being.
    # writing the 'pass' here is not neccessary the code will work without it too.

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def names(self):
        return "{} {}".format(self.fname, self.lname)
    
    def emails(self):
        return "{}.{}".format(self.fname, self.lname)+ "@email.com"

    def passwords(self):
        return "_" + "{}.{}".format(self.fname, self.lname) + "1234"

#ignore the names, i just copy-pasted them
user1 = info("Jake", "Logan")
user2 = info("Peter", "Oliver")
user3 = info("James", "Allan")

#for user1:
print(info.names(user1))
print(info.emails(user1))
print(info.passwords(user1))

#for user2:

print(info.names(user2))
print(info.emails(user2))
print(info.passwords(user2))

# for user3:

print(info.names(user3))
print(info.emails(user3))
print(info.passwords(user3))

# and so on....
