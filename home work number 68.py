# Define the sets
domestic_cats = {"cat", "lion cat", "persian cat"}
domestic_dogs = {"dog", "poodle", "bulldog"}
wild_dogs = {"wolf", "fox", "jackal"}

endangered_animals = {"wolf", "panda", "dog", "tiger"}

# Combine domestic cats and domestic dogs into one set of pets
pets = domestic_cats.union(domestic_dogs)

# Combine domestic dogs and wild dogs into one set of dogs
dogs = domestic_dogs.union(wild_dogs)

# Find the dogs that are endangered
endangered_dogs = dogs.intersection(endangered_animals)

# Display the results
print("Pets:", pets)
print("Dogs:", dogs)
print("Endangered dogs:", endangered_dogs)
