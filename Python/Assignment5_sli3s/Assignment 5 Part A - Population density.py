#Programmer name: Susan Li
#Program creation date: August 13, 2022

#Calculate population density

#function to calculate population density
def population_density(population, area):
    return(float(population/area))
#population density of Maryland
population_density_maryland = population_density(6.062, 12407)
print("The population density of Maryland is {} million people per square mile.".format(population_density_maryland))
#population density of Virginia
population_density_virginia = population_density(8.4, 42775)
print("The population density of Virginia is {} million people per square mile.".format(population_density_virginia))
#population density of Pennsylvania
population_density_pennsylvania = population_density(12.81, 46055)
print("The population density of Pennsylvania is {} million people per square mile.".format(population_density_pennsylvania))
