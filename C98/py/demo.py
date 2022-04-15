def count():
    filename=input("enter the file name- ")
    wordsno = 0

    file = open(filename, 'r')

    for line in file:
        words = line.split( )

        wordsno= wordsno+len(words)
    print(wordsno)

count()
