# coding: utf-8

# import modules


# additional code

import labyrinth_map
import variables



def main():
    """
        Main function
    """

    # to know wich line's number we are checking
    nb_current_line = 0

    # the line which is currently printing
    line_printed = ""

    # check line by line
    # for each line of the labyrinth map
    for line in labyrinth_map.labyrinth :

        # to know wich column's number we are checking
        nb_current_column = 0

        # check column by column
        # while the number of the column is less than the length of the labyrinth's line
        while nb_current_column < len(labyrinth_map.labyrinth[0]):

            # check if the avatar is located in the place
            # if the numbers of the column and of the line match with the avatar's place, print the symbol of the avatar "€"
            if nb_current_line == variables.y_avatar and nb_current_column == variables.x_avatar :
                line_printed = f"{line}€"
            # if not, print item of the labyrinth
            else :
                line_printed = str(line) + str(labyrinth_map.labyrinth[nb_current_line][nb_current_column])

            # increment the column's number to switch to the next column
            nb_current_column += 1
        
        # increment the line's number to switch to the next line
        nb_current_line += 1

        # print the line
        print(line_printed)
        


















# Program main entry
if __name__ == "__main__":
    main()