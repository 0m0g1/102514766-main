#include <cs50.h>
#include<stdio.h>

//This is the function that draws the 2-gap pyramid
void draw(int height)
{
    //Initializing the variables
    int mid = height + 1;
    int height_index;
    int column_index;

    //This for loop checks if the cursor is not passed the given height
    for (height_index = 1; height_index <= height; height_index++)
    {
        //This for loop checks if the cursor is not based the rows maximum length and ends the line if the end is reached
        for (column_index = 1; column_index < mid + 3 + height_index; column_index++)
        {
            //This if statement checks if the cursor is not in between the pyramid and prints two spaces if its in the middle
            if (column_index <= mid + 1 + height_index)
            {
                if (column_index > height - height_index || column_index >= mid + 1 + height_index)
                {
                    if (column_index != mid && column_index != mid + 1)
                    {
                        printf("#");
                    }
                    else
                    {
                        printf(" ");
                    }
                }
                else
                {
                    printf(" ");
                }
            }
            else
            {
                printf("\n");
            }
        }
    }
}

//This is the main function that initializes the code
//This ask for the height of the pyramid
int main()
{
    int height = get_int("What is your height?");
    if (height > 0 && height < 9)
    {
        draw(height);
    }
    else
    {
        main();
    }
}