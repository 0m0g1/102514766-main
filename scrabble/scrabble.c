#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // This compares the scores of both players and outputs the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 == score2)
    {
        printf("Tie\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }
}

//Calculates the scores for each word
int compute_score(string word)
{
    int score = 0;
    int word_length = strlen(word);

    //Loops through a word and calculates the score for each letter in the word
    for (int i = 0; i < word_length; i++)
    {
        char letter = word[i];
        int letter_index = word[i];
        //Checks 
        if (isupper(letter))
        {
            letter_index -= 65;
        }
        else
        {
            letter_index -= (25 + 7 + 65);
        }
        //Checks if the the character is a letter and add the points of the letter to the score if it is a score
        if (letter_index > -1 && letter_index < 26)
        {
            score += POINTS[letter_index];
        }
    }
    return score;
}
