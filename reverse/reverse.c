#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3)
    {
        printf("usage ./reverse input.wav output.wav\n");
    }

    // Open input file for reading
    FIlE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Error opening file\n");
        return 1;
    }

    // Read header
    FILE *output = fopen(argv[2], "wb");
    if (output == NULL)
    {
        printf("Eroor oppening output file\n");
        return 1;
    }

    // Use check_format to ensure WAV format
    // TODO #4

    // Open output file for writing
    // TODO #5

    // Write header to file
    // TODO #6

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

int check_format(WAVHEADER header)
{
    // TODO #4

    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return 0;
}