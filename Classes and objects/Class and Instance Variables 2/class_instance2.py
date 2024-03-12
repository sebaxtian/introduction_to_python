class City:
    # TODO: add a mutable class variable (all_cities list) to store all added city names
    all_cities = []
    value = 100
    dict_value = {"key": "value"}

    def __init__(self, name, population, country):
        self.name = name
        self.population = population
        self.country = country
        # TODO: call add_city method to add the city name to the list upon object initialization
        City.all_cities.append(self.name)

    def add_city(self):
        # TODO: implement a method that will append a city name to the all_cities list. Delete the pass statement!
        self.all_cities.append(self.name)


if __name__ == '__main__':
    malaga = City('Malaga', 569005, 'Spain')
    malaga.value = 1
    boston = City('Boston', 689326, 'USA')
    boston.value = 2
    beijing = City('Beijing', 21540000, 'China')
    beijing.value = 3

    print(malaga.all_cities)  # This should print "['Malaga', 'Boston', 'Beijing']".

    print(malaga.value, boston.value, beijing.value)
    print(malaga.dict_value, boston.dict_value, beijing.dict_value)

    City.value = 200
    City.dict_value = {"key": 123}

    print(malaga.value, boston.value, beijing.value)
    print(malaga.dict_value, boston.dict_value, beijing.dict_value)

