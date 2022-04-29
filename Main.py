data=[
    {"title":"Geography",
    "words":[{"title":"Europe","clues":["Paris","Euro","Polish Leader I think"] 
             }
            ]},
    {"title":"School",
    "words":[{"title":"Homework","clues":["School at home","Due tomorrow","At your own pace"] 
             },{"title":"Fortnite","clues":["Boogie","Ninja","Tfue"] 
             }
            ]
    },{"title":"History",
    "words":[{"title":"Italy","clues":["Roman Empire","Romanum Empirum","All roads lead to Rome"] 
             },{"title":"The United States","clues":["July 4th 1776","North American Powerhouse","Dollar"] 
             }
            ]
      }
]


#print(data)

guessing=True
#rannum1
while guessing:
  hidden = data[0]["words"][0]["title"]
  print ("You're category is",data[0]["title"])
  for i in data[0]["words"][0]["clues"]:
    print ("You're first clue is",i)
    guess = input ("Geography what is your guess")
    if guess == hidden: 
      print("cool")
      guessing=False

import random

print(random.randrange(3, 9))