Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-22
Purpose: Provide informtion on the Elder Scrolls games and their world, Tamriel, its location, races, and lore.

To run the program you should start with the command: python3 tamriel.py

This will provide the information on what type of items you can get information on.

The optional command -r will allow you to use one of the keywords to look up information.

My procedure for creating the project

Process:
    1.) Use new.py to make a new file 'tamriel.py'
    2.) Create csv with select information about the Elder Scrolls and Tamriel:
        -   locations: the planes of reality related to Tamriel, countries in Tamriel, provinces, and cities
        -   races: a file with the different races
        -   beings: other types of beings outside of the races e.g. dragons, daedra
        -   games: list of the elder scrolls games and info about them
    3.) Build the following functionality:
        -   read csv files
        -   take inputs: -r nothing entered after will provide a list of all options e.g. -r
        -   for provided request type return a list of all the information of that type.
    4.) Design test for the program create test.py
    5.) Copy code to a new repository.

To run test.py use:
    make test command


Possible next steps for program:
    -   make csv file more comprehensive
    -   allow searching for particular term by addind a second optional argument -s --search where every row in the CSV with the term in it is returned.
    -   add a -e --everything that prints the whole CSV
