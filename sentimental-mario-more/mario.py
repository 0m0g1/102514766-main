# Draw a two height pyramid
def draw():
    try:
        height, height_index = int(input("what is the height?")), 1

        # Draw a pyramid when the height is greater than 0 and less than 9
        if height > 0 and height < 9:
            while height_index <= height:
                print(f'{" "*(height-height_index)}{"#"*height_index}  {"#"*height_index}')
                height_index += 1
        else:
            draw()
    except:
        draw()


draw()