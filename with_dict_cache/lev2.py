from csv import reader


cache = {}
def levenshtein_distance(string_1, string_2):
    
    '''
    cache check
    '''

    keyname = '|'.join([string_1, string_2])
    if keyname in cache:
        return cache[keyname]

    if keyname in cache:
        return cache[keyname]

    '''
    start function
    '''
    moves = 0
    movesf = 0
    movesb =0

    if len(string_1) >= len(string_2):

        moves += len(string_1) - len(string_2)
        # print(moves)

        for i in range(len(string_2)):
            if string_2[i] != string_1[i]:
                movesf += 1
        # print(movesf)
        for i in range(1,len(string_2)+1):
            if string_2[-i] != string_1[-i]:
                movesb += 1
        # print(movesb)
        if movesf<movesb:
            moves += movesf
        else:
            moves += movesb

    if len(string_2) > len(string_1):

        moves += len(string_2) - len(string_1)

        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                movesf += 1
        for i in range(1,len(string_1)+1):
            if string_1[-i] != string_2[-i]:
                movesb += 1
        
        if movesf<movesb:
            moves += movesf
        else:
            moves += movesb

    
    cache[keyname] = moves

    return moves


with open('/Users/rh/Desktop/Py/xda-api/wordlist.csv', 'r') as f:
    doc = reader(f)
    for row in doc:
        print(levenshtein_distance(row[0], row[1]))