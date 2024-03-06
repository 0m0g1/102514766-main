#include <stdio.h>
#include <stdbool.h>

#define BLOCK_SIZE 512

int main()
{
    FILE *file = fopen("card.raw", "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    unsigned char buffer[BLOCK_SIZE];
    int count = 0;
    FILE *output = NULL;

    while (fread(buffer, sizeof(unsigned char), BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output != NULL)
            {
                fclose(output);
            }

            char filename[8];
            sprintf(filename, "%03i.jpg", count++);
            output = fopen(filename, "w");
            if (output == NULL)
            {
                fclose(file);
                printf("Could not create output file.\n");
                return 1;
            }
        }

        if (output != NULL)
        {
            fwrite(buffer, sizeof(unsigned char), BLOCK_SIZE, output);
        }
    }

    fclose(output);
    fclose(file);

    return 0;
}