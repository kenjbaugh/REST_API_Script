import json
import requests
import re
from collections import Counter

#Webpages holding corresponding JSON data
JSONusers = 'http://jsonplaceholder.typicode.com/users'
JSONposts = 'http://jsonplaceholder.typicode.com/posts'

postsURL = requests.get(JSONposts).json()
usersURL = requests.get(JSONusers).json()

#Empty lists for later use
foundIds = []
countPosts = []
authors = []
#Now apply some regex logic to find the patterns you need
for post in postsURL:
    findMatch = re.search('cup', post['body'])
    findMatch2 = re.search('qu', post['body'])

# Goal is for regex to find the id matches and then append to the empty list created above
    if (findMatch):
        if(findMatch2):
            if (findMatch.start() < findMatch2.start()):
                foundIds.append(post['userId'])

#Printing out those ID's
print(foundIds)

#Grabs all of the occurances of userid, which will repeat
#This will be used later to count the occurances of each userid
for number in postsURL:
    if number['userId'] == 4:
        countPosts.append(number['userId'])
        #print(ele['userId'])
    if number['userId'] == 8:
        countPosts.append(number['userId'])
        #print(ele['userId'])
    if number['userId'] == 10:
        countPosts.append(number['userId'])
        #print(ele['userId'])

#Creating a text file called report.txt and outputing the results found in it
for found in usersURL:
    if found['id'] in foundIds:
        authors.append(found['name'])
        print(found['name'])
        fileReport = open("report.txt", "w")
        fileReport.write("\nThe authors who wrote blogs that contains the words 'cup' and 'qu' are"  + str(authors))
        fileReport.write("\nThese authors have the userId's of 4, 8, and 10. The amount of blog posts they have published are " + str(Counter(countPosts)))
        fileReport.close()
        print(found['name'])
print(authors)
