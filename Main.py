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
    },{"title":"School",
    "words":[{"title":"Homework","clues":["School at home","Due tomorrow","At your own pace"] 
             },{"title":"Fortnite","clues":["Boogie","Ninja","Tfue"]}]}
              
]

#print(data)

guessing=True
while guessing:
  hidden = data[0]["words"][0]["title"]
  guess = input("what is your guess ")
  if guess == hidden:
    print("cool")
    guessing=False
    