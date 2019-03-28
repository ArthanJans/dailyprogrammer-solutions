relationships = {}
with open("input375[hard].txt") as inFile:
    text = inFile.readlines()
    params = text[0].split(" ")
    N = int(params[0])
    M = int(params[1])
    data = text[1:]
    for line in data:
        line = line.strip("\n")
        if "++" in line:
            components = line.split(" ++ ")
            relationship = "++"
        elif "--" in line:
            components = line.split(" -- ")
            relationship = "--"
        first = components[0]
        second = components[1]

        if first not in relationships:
            relationships[first] = {}
        relationships[first][second] = relationship

        if second not in relationships:
            relationships[second] = {}
        relationships[second][first] = relationship

        for person in relationships[second]:
            if person != first and person in relationships[first]:
                if relationships[first][person] != relationships[second][person]:
                    if relationships[first][second] != "--":
                        print("not balanced")
                        print(first, relationships[first][second], second)
                        print(first, relationships[first][person], person)
                        print(second, relationships[second][person], person)
                        exit()

print("balanced")