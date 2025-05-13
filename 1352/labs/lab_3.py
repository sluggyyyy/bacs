if __name__ == '__main__':
    # Question 1. Use list comprehension to create a list containing the first 500 multiples of 5.
    # (The first element should be 5, the last element should be 2500)
    multiples_of_five = [i * 5 for i in range(501) if i >= 1] # finish this line of code

    
    # Questions 2. The list below gives the most popular baby names in 2021 that start with the letter 'E'
    # Create a new list that contains all the elements in the original list, but converted to lower-case.
    # Solve this in one line of code (use list comprehension to do this)
    popular_E_names = ['Emma', 'Evelyn', 'Elizabeth', 'Eleanor', 'Ella', 'Emily', 'Ellie', 'Emilia', 'Eliana', 'Everly', 'Elena', 'Emery', 'Eva', 'Everleigh', 'Eloise', 'Eliza', 'Eden', 'Elliana', 'Elijah', 'Ethan', 'Ezra', 'Elias', 'Ezekiel', 'Eli', 'Easton', 'Everett', 'Emmett', 'Evan', 'Enzo', 'Elliot', 'Elliott', 'Emiliano']
    popular_e_names = [i.lower() for i in popular_E_names] # finish this line of code
    
    #Part 3: Using the original list of (capitalized) popular E-names in part 2, use list comprehension
    # this time to create a new list of the names that start with "Em". Note that you will need to use 
    # a conditional list comprehension.
    popular_Em_names = [i for i in popular_E_names if i.startswith('Em')] # finish this line of code
    
    print(multiples_of_five)
    print(popular_e_names)
    print(popular_Em_names)
    
    oscars_best_picture_dictionary = {
    2024: "Oppenheimer",
    2023: "Everything Everywhere All at Once",
    2022: "CODA",
    2021: "Nomadland",
    2020: "Parasite",
    2019: "Green Book",
    2018: "The Shape of Water",
    2017: "Moonlight",
    2016: "Spotlight",
    2015: "Birdman or (The Unexpected Virtue of Ignorance)",
    2014: "12 Years a Slave",
    2013: "Argo",
    2012: "The Artist",
    2011: "The King’s Speech",
    2010: "The Hurt Locker",
    2009: "Slumdog Millionaire",
    2008: "No Country For Old Men",
    2007: "The Departed",
    2006: "Crash",
    2005: "Million Dollar Baby",
    2004: "Lord Of The Rings: Return Of The King",
    2003: "Chicago",
    2002: "A Beautiful Mind",
    2001: "Gladiator",
    2000: "American Beauty",
    1999: "Shakespeare In Love",
    1998: "Titanic",
    1997: "The English Patient",
    1996: "Braveheart",
    1995: "Forrest Gump",
    1994: "Schindler’s List",
    1993: "Unforgiven",
    1992: "The Silence of the Lambs",
    1991: "Dances With Wolves",
    1990: "Driving Miss Daisy",
    1989: "Rain Man",
    1988: "The Last Emperor",
    1987: "Platoon",
    1986: "Out of Africa",
    1985: "Amadeus",
    1984: "Terms of Endearment",
    1983: "Gandhi",
    1982: "Chariots of Fire",
    1981: "Ordinary People",
    1980: "Kramer Vs. Kramer",
    1979: "The Deer Hunter",
    1978: "Annie Hall",
    1977: "Rocky",
    1976: "One Flew Over The Cuckoo’s Nest",
    1975: "The Godfather: Part II",
    1974: "The Sting",
    1973: "The Godfather",
    1972: "The French Connection",
    1971: "Patton",
    1970: "Midnight Cowboy",
    1969: "Oliver!",
    1968: "In The Heat of the Night",
    1967: "A Man for All Seasons",
    1966: "The Sound of Music",
    1965: "My Fair Lady",
    1964: "Tom Jones",
    1963: "Lawrence of Arabia",
    1962: "West Side Story",
    1961: "The Apartment",
    1960: "Ben-Hur",
    1959: "Gigi",
    1958: "The Bridge on the River Kwai",
    1957: "Around the World in 80 Days",
    1956: "Marty",
    1955: "On the Waterfront",
    1954: "From Here to Eternity",
    1953: "The Greatest Show on Earth",
    1952: "An American in Paris",
    1951: "All About Eve",
    1950: "All the King’s Men",
    1949: "Hamlet",
    1948: "Gentleman’s Agreement",
    1947: "The Best Years of Our Lives",
    1946: "The Lost Weekend",
    1945: "Going My Way",
    1944: "Casablanca",
    1943: "Mrs. Miniver",
    1942: "How Green Was My Valley",
    1941: "Rebecca",
    1940: "Gone With The Wind",
    1939: "You Can’t Take It With You",
    1938: "The Life of Emile Zola",
    1937: "The Great Ziegfeld",
    1936: "Mutiny on the Bounty",
    1935: "It Happened One Night",
    1934: "Cavalcade",
    1933: "Grandhotel",
    1932: "Cimarron",
    1931: "All Quiet on the Western Front",
    1930: "The Broadway Melody",
    1929: "Wings"
}

# Question 4: Complete the next line of code, using list comprehension to create 
# a list of the one-word movie titles from the above dictionary values
best_pictures_list = {value for value in oscars_best_picture_dictionary.values() if ' ' not in value}
print(best_pictures_list)
print(len(best_pictures_list))