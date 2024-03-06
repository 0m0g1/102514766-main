#include <cs50.h>
#include <stdio.h>

// This is the main function that calculates the number of years the population will grow
int main()
{
    // This initializes the variables
    int population, endpopulation, years = 0;

    //This repeats if the starting population is less than 9
    do
    {
        population = get_int("Starting size: ");
    }
    while (population < 9);

    //This repeats if the ending population is less than the starting population
    do
    {
        endpopulation = get_int("Ending size: ");
    }
    while (endpopulation < population);

    //This calculates the number of years
    while (population < endpopulation)
    {
        population += (population / 3) - (population / 4);
        years++;
    }

    //This outputs the number of years
    printf("Years: %d \n", years);
}