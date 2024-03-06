#include "helpers.h"
#include <math.h>
#include <cs50.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average_color = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3);
            image[i][j].rgbtRed = average_color;
            image[i][j].rgbtGreen = average_color;
            image[i][j].rgbtBlue = average_color;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buffer[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            buffer[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = buffer[i][width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = buffer[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = buffer[i][width - j - 1].rgbtBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width]) {
  // Create a copy of the image.
  RGBTRIPLE copy[height][width];
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      copy[i][j] = image[i][j];
    }
  }

  // Blur the image.
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      // Get the average of the surrounding pixels.
      int red = (copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed +
                 copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed +
                 copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed) / 9;
      int green = (copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen +
                   copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen +
                   copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen) / 9;
      int blue = (copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue +
                   copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue +
                   copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue) / 9;

      // Set the pixel's color to the average.
      image[i][j].rgbtRed = red;
      image[i][j].rgbtGreen = green;
      image[i][j].rgbtBlue = blue;
    }
  }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width]) {
  // Create a copy of the image.
  RGBTRIPLE copy[height][width];
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      copy[i][j] = image[i][j];
    }
  }

  // Calculate the Sobel gradients.
  int sobel_x[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
  int sobel_y[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

  // Iterate over each pixel in the image.
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      // Calculate the magnitude of the gradient for each color channel.
      int magnitude_red = 0;
      int magnitude_green = 0;
      int magnitude_blue = 0;
      for (int k = 0; k < 3; k++) {
        for (int l = 0; l < 3; l++) {
          magnitude_red += (copy[i + k - 1][j + l - 1].rgbtRed * sobel_x[k][l]) + (copy[i + k - 1][j + l - 1].rgbtRed * sobel_y[k][l]);
          magnitude_green += (copy[i + k - 1][j + l - 1].rgbtGreen * sobel_x[k][l]) + (copy[i + k - 1][j + l - 1].rgbtGreen * sobel_y[k][l]);
          magnitude_blue += (copy[i + k - 1][j + l - 1].rgbtBlue * sobel_x[k][l]) + (copy[i + k - 1][j + l - 1].rgbtBlue * sobel_y[k][l]);
        }
      }

      // Normalize the magnitudes.
      magnitude_red = magnitude_red / 9;
      magnitude_green = magnitude_green / 9;
      magnitude_blue = magnitude_blue / 9;

      // Set the pixel's color to the magnitude.
      image[i][j].rgbtRed = magnitude_red;
      image[i][j].rgbtGreen = magnitude_green;
      image[i][j].rgbtBlue = magnitude_blue;
    }
  }
}
