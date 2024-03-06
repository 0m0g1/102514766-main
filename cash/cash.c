#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int cents;
    //Gets the number of cents and reprompts if the number is less than 0
    do
    {
        cents = get_int("Change: ");
    }
    while (cents < 0);
    return cents;
}

int calculate_quarters(int cents)
{
    int quaters = 0;
    //This calculates the number of quaters to be given while the number of cents is greater than 24
    if (cents > 24)
    {
        do
        {
            cents -= 25;
            quaters += 1;
        }
        while (cents > 24);
    }
    return quaters;
}

int calculate_dimes(int cents)
{
    int dimes = 0;
    //This calculates the number of dimes to be given while the number of cents is greater than 9
    if (cents > 9)
    {
        do
        {
            cents -= 10;
            dimes += 1;
        }
        while (cents > 9);
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels = 0;
    //This calculates the number of nickels to be given while the number of cents is greater than 4
    if (cents > 4)
    {
        do
        {
            cents -= 5;
            nickels += 1;
        }
        while (cents > 4);
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies = 0;
    //This calculates the number of pennies to be given while the number of cents is greater than 0
    if (cents > 0)
    {
        do
        {
            cents -= 1;
            pennies += 1;
        }
        while (cents > 0);
    }
    return pennies;
}
