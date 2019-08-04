def city(city,country,population=""):
    if population:
        total=city+","+country+"-"+"population "+str(population)
    else:
        total=city+","+country
    return total
"""total=city("shanghai","China",500000)
print(total)"""