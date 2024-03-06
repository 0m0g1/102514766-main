#include <string.h>
#include <strings.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of indexes in the hash table
const unsigned int HASH_INDEXES = 50000;

node *table[HASH_INDEXES];

// Returns true if word is in dictionary else false
bool check(const char *word)
{

    int index = hash(word);

    //A pointer to the head of a table
    node *cursor = table[index];

    //for loop to go through the list until the final node is reached and returns true if the node is found
    for (node *temp = cursor; temp != NULL; temp = temp -> next)
    {
        if (strcasecmp(temp -> word, word) == 0)
        {
            return true;
        }
    }
    return false;
}


// Hashes word to a number to get its index
unsigned int hash(const char *word)
{
    unsigned int index = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        index += tolower(word[i]);
        index = (index * tolower(word[i])) % HASH_INDEXES;
    }
    return index;
}

int words_counter = 0;

// Loads dictionary into memory
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        fprintf(stderr, "There has been an error");
        return false;
    }

    //word_buffer is a list of the word's characters
    char word_buffer[LENGTH + 1];

    //Loads words into word_buffer
    while (fscanf(file, "%s", word_buffer) != EOF)
    {
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            return 1;
        }

        //Copy a word_buffer into the new node
        strcpy(newNode -> word, word_buffer);
        newNode -> next = NULL;
        int index = hash(word_buffer);
        if (table[index] == NULL)
        {
            table[index] = newNode;
        }
        else
        {
            newNode->next = table[index];
            table[index] = newNode;
        }
        words_counter++;
    }
    fclose(file);
    return true;
}


// Returns the number of words in the dictionary
unsigned int size(void)
{
    return words_counter;
}

// Unloads dictionary from memory
bool unload(void)
{
    node *temp = NULL;
    node *cursor = NULL;

    //Loop through the hash table and free memory
    for (int i = 0; i < HASH_INDEXES; i++)
    {
        cursor = table[i];
        while (cursor != NULL)
        {
            temp = cursor;
            cursor = cursor -> next;
            free(temp);
        }
    }
    return true;
}