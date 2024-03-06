#include <cs50.h>
#include <stdio.h>

//This is the main function
//It takes a string input of the users name and concatenates the name and hello, then outputs it
int main(void)
{
    string name = get_string("What is your name? ");
    printf("hello, %s\n", name);
}