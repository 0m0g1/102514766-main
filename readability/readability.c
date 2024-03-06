#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>

//Prototyping functions
int calculate_grade(string paragraph);
int count_words(string paragraph);
int count_sentences(string paragraph);
int count_letters(string paragraph);

//The main function
int main(void)
{
    //Initializing variables
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    //Calculating the Grade
    int grade = round(0.0588 * letters / words * 100  - 0.296 * sentences / words * 100 - 15.8);

    //Outputing the grade
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 15)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }
}

//Counts the number of letters in the paragraph
int count_letters(string paragraph)
{
    int parlen = strlen(paragraph);
    int letters = 0;

    //Checks if a character in the paragraph is a letter
    for (int i = 0; i < parlen; i++)
    {
        char character = paragraph[i];
        int character_index = paragraph[i];
        if (isupper(character))
        {
            character_index -= 65;
        }
        else
        {
            character_index -= (25 + 7 + 65);
        }
        if (character_index > -1 && character_index < 26)
        {
            letters += 1;
        }
    }
    return letters;
}

//Counts the number of words in the paragraph
int count_words(string paragraph)
{
    int words = 1;
    int parlen = strlen(paragraph);

    //Checks if a character in the paragraph is a space
    for (int i = 0; i < parlen; i++)
    {
        int character = paragraph[i];
        if (character == 32)
        {
            words += 1;
        }
    }
    return words;
}

//Counts the number of words in the paragraph
int count_sentences(string paragraph)
{
    int sentences = 0;
    int parlen = strlen(paragraph);

    //Checks if a character in the paragraph is a fullstop, exclamation mark or question mark
    for (int i = 0; i < parlen; i++)
    {
        int character = paragraph[i];
        if (character == 46 || character == 63 || character == 33)
        {
            sentences += 1;
        }
    }
    return sentences;
}