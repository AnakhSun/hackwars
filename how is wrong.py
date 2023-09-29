import nums_from_string
people = {}    

messages = ["John:I'm in 1st position.",
      'Peter:There is 1 people in front of me.',
      'Tom:There are 2 people behind me.',
      'Peter:The man behind me is Tom.']

for message in messages:
    name = message.split(":")[0]
    phrase = message.split(":")[1]
    
    if name not in people:
        people[name] = {}
    if "position" in phrase:
        people[name]["pos"] = nums_from_string.get_nums(phrase)[0]

    if "man behind me" in phrase:
        
        people[name]["behind"] = phrase.split(" ")[-1].split(".")[0]
    if " man in front of me is" in phrase:
        people[name]["front"] = phrase.split(" ")[-1].split(".")[0]

    if "people in front of me" in phrase:
        people[name]["front_c"] = nums_from_string.get_nums(phrase)[0]

    if "people behind me" in phrase:        
        people[name]["behind_c"] = nums_from_string.get_nums(phrase)[0]
places = {i : [] for i in range(1, len(people)+1)}
print(people)
print(places)


for name, info in people.items():
    for key, val in info.items():
        if key == "pos":
            places[val].append(name)

        if key == "forward":
            places[info["pos"]-1].append(val)

        if key == "behind":
            try:
                places[info["pos"]+1].append(val)
            except:
                try:
                    places[people[val]["pos"]-1].append(name)
                except:
                    pass

        if key == "forward_c":
            places[val+1].append(name)

        if key == "behind_c":
            places[len(places)-val].append(name)



            

print(people)
print(places)