# check the grade of a paragraph of text
def main():
    paragraph = str(input("Text:"))
    letters = 0
    words = len(paragraph.split())
    sentences = 0

    # loop through each character of the text
    for character in paragraph:
        if character.isalpha():
            letters += 1
        if character in [".", "!", "?"]:
            sentences += 1

    # calculate the grade of the text
    grade = int(round(0.0588 * ((letters / words) * 100) - 0.296 * ((sentences / words) * 100) - 15.8))

    # output the grade
    if grade > 15:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f'Grade {grade}')


main()