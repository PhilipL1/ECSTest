from collections import defaultdict




def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    points = { "1" : 3, "2" : 2, "3": 1 }
    res = defaultdict(int)
    
    for dictionary in results:
        for key, value in dictionary.items():
            if key == "podium":
                for places in value:
                    parts = places.split(".")
                    position = parts[0]
                    country = parts[1]
                    res[country] += points[position]
    return res




