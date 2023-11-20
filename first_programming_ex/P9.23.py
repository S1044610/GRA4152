import argparse
from operator import attrgetter
from operator import methodcaller

## A country has name, population, and area can be computed the population density.
#
class Country:
    ## Constructs a country with name, population, and area.
    # @param name the name of the country
    # @param population the population of the country
    # @param area the area of the country
    #
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    ## Gets the country with the largest population from a list of countries.
    # @param countries stores the name of the countries
    # @return the Country with the largest population
    #
    def largest_population(countries):
        return max(countries, key=attrgetter('population'))
    

    ## Gets the country with the largest area from a list of countries.
    # @param countries a list of Country
    # @return the Country with the largest area
    #
    def largest_area(countries):
        return max(countries, key=attrgetter('area'))


    ## Gets the density.
    # @return the density
    #
    def get_density(self):
        return self.population / self.area


    ## Gets the country with the largest population density from a list of countries.
    # @param countries a list of Country
    # @return the Country with the largest population density
    #
    def largest_density(countries):
        return max(countries, key=methodcaller('get_density'))

#Test class
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="countries.")
    
    parser.add_argument("--country", action="append", required=True, help="Name.")
    parser.add_argument("--population", action="append", type=int, required=True, help="Population.")
    parser.add_argument("--area", action="append", type=float, required=True, help="Area.")
    
    args = parser.parse_args()
    
    countries = [Country(name, pop, area) for name, pop, area in zip(args.country, args.population, args.area)]

    print(f"Largest Area: {Country.largest_area(countries).name}")
    print(f"Largest Population: {Country.largest_population(countries).name}")
    print(f"Largest Density: {Country.largest_density(countries).name}")