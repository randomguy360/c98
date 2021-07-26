def countwords():
     filename = input('file name:')
     words = 0
     file = open(filename)
     for l in file:
             q = l.split()
             words = words+ len(q)
     print('words: ')
     print(words)

countwords()