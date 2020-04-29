import random
# create 100 names and descriptions

endpoint = [{id: "", "roomName": "", "description": ""}, {
    id: "", "roomName": "", "description": ""}, {id: "", "roomName": "", "description": ""}]

# generates whatever number of rooms we need


def name_Generator(numOfRooms):
    # read entire names in file
    array1 = []
    array2 = []
    with open("util/roomnames.csv") as f:
        for line in f:
            d = line.split(",")
            array1.append(d[0])
            if d[1]:
                array2.append(d[1])

    namesArray = []
    for i in range(numOfRooms):
        namesArray.append(array1[random.randint(0, len(array1) - 1)] +
                          array2[random.randint(0, len(array2) - 1)])
    return namesArray

# generate descriptions


def description_generator(numOfDescriptions):
    description1 = []
    description2 = []
    description3 = []
    with open("util/descriptions.csv") as f:
        for line in f:
            d = line.split('$')
            description1.append(d[0])
            if d[1]:
                description2.append(d[1])
            if d[2]:
                description3.append(d[2])

    descriptionsArray = []
    for i in range(numOfDescriptions):
        descriptionsArray.append(description1[random.randint(0, len(description1) - 1)] +
                                 (description2[random.randint(0, len(description2) - 1)] +
                                  (description3[random.randint(
                                      0, len(description3) - 1)])))
    return descriptionsArray


def contentGeneration(numOfRooms):
    rooms = []
    names = name_Generator(numOfRooms)
    descriptions = description_generator(numOfRooms)

    for i in range(numOfRooms):
        rooms.append({
            "title": names[i],
            "description": descriptions[i]
        })
    return rooms


print(contentGeneration(100))
