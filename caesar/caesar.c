#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

//prototype functions
string encode(int key, string text);
bool onlydigits(string text);

//main function
int main(int argc, string argv[])
{
    //handles the lack of an argument
    //handles too many arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //Checks if the key has only digits
    if (!onlydigits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //convert the key into an integer
    int key = atoi(argv[1]);
    string plain_text = get_string("plaintext:  ");
    string encoded_text = encode(key, plain_text);

    //output encrypted text
    printf("ciphertext: %s\n", encoded_text);
}

//check if the input has only strings
bool onlydigits(string text)
{
    int text_length = strlen(text);
    bool only_digits = true;
    for (int i = 0; i < text_length; i++)
    {
        int char_index = text[i];
        if (char_index < 48 || char_index > 57)
        {
            only_digits = false;
        }
    }
    return only_digits;
}

//encodes the inputed text
string encode(int key, string text)
{
    //Handles keys that are greater than 26
    if (key > 26)
    {
        int times = round(key / 26);
        key -= (26 * times);
    }

    int text_length = strlen(text);

    //Loops through the text and shifts each character by the key
    for (int i = 0; i < text_length; i++)
    {
        char character = text[i];
        int char_index = text[i];

        //Shifts uppercase letters
        if (char_index > 64 && char_index < 91)
        {
            char_index += key;
            if (char_index > 90)
            {
                char_index -= 26;
            }
        }

        //Shifts lowercase letters
        if (char_index > 96 && char_index < 123)
        {
            char_index += key;
            if (char_index > 122)
            {
                char_index -= 26;
            }
        }
        char new_character = (char) char_index;
        text[i] = new_character;
    }
    return text;
}