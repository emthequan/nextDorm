from pymongo import Connection
 
databaseName = "users"
connection = Connection()
 
db = connection[databaseName]
usersDB = db['usersDB']
 
user1 = { "name" : "Valerie Nayak",
		"username": "valerienayak", "password": "janebanks" }
user2 = { "name" : "Anyesha Majumdar",
		"username": "titli", "password": "turtle"}
user3 = { "name" : "Kanvi Shah",
		"username": "moo", "password": "rawr"}
user4 = { "name" : "Emily Quan",
		"username": "hopbunny", "password": "bunno"}
 
#print "clearing"
employees.remove()
 
print "saving"
users.save(user1)
users.save(user2)
users.save(user3)
users.save(user4)
 
#print "searching"
#for e in employees.find():
	#print e["name"] + " " + unicode(e["languages"])
