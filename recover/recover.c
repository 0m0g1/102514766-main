#include <stdio.h>
#include <stdlib.h>

const int SIZE = 512;

//Recover jpg images from a file
int main(int argc, char *argv[])
{
    //Checks for correct function usage
    if (argc != 2)
    {
        printf("Usage ./recover input.JPEG");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    FILE *output = NULL;

    if (input == NULL)
    {
        printf("There was an error opening the file\n");
        return 1;
    }

    int jpg_counter = 0;
    unsigned char buffer[SIZE];

    //Reads data from the input file
    while (fread(buffer, sizeof(unsigned char), SIZE, input) == SIZE)
    {
        //Checks if the array of data is a valid jpg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output != NULL)
            {
                fclose(output);
            }
            //Creates a filename for the output
            char filename[8];
            sprintf(filename, "%03d.jpg", jpg_counter++);
            output = fopen(filename, "w");
            if (output == NULL)
            {
                fclose(output);
                printf("Error opening output file\n");
                return 1;
            }
        }

        //Writes to the output file
        if (output != NULL)
        {
            fwrite(buffer, sizeof(unsigned char), SIZE, output);
        }
    }
    fclose(output);
    fclose(input);
    return 0;
}