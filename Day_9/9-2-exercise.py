travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country, visits, cities):
    flag = True
    for i in range(len(travel_log)):
        if travel_log[i]["country"] == country:
            flag = False
            travel_log[i]["visits"] += visits
            for city in cities:
                if city not in travel_log[i]["cities"]:
                    travel_log[i]["cities"].append(city)
    if flag:
        log = {"country":country,
               "visits":visits,
               "cities":cities}
        travel_log.append(log)
print(travel_log)
add_new_country("France", 4, ["Bordo", "Nangt"])
print(travel_log)
add_new_country("Korea", 3, ["Gwangju", "YoungGwang"])
print(travel_log)