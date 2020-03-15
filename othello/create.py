'''
    Created on Mar 8, 2020
    
    @author:    Tae Myles
'''
import hashlib

def __checkBoundary(input):
    for parameter in ('light', 'dark', 'blank'):
        if (parameter == None):
            return {'status': 'error: Null ' + parameter +  ' value'}
        try: int(input(parameter))
        except ValueError:
            return {'status': 'error: non-integer ' + parameter + 'value'}
        if (int(input(parameter)) > 9):
            return {'status': 'error: above bound' + parameter + 'value'} 
        elif (int(input(parameter)) < 0):
            return {'status': 'error: below bound' + parameter + 'value'}
        
    if (input['size'] == None):
        return {'status': 'error: Null size value'}
    try: (int(input['size']))
    except ValueError:
        return {'status': 'error: non-integer size value'}
    if (int(input['size']) > 16):
        return {'status': 'error: above bound size value'}
    elif (int(input['size']) < 6):
        return {'status': 'error: below bound size value'}
    elif (int(input['size']) % 2 != 0):
        return {'status': 'error: Odd size value'}
    
    if (int(input['light']) == int(input['dark'])):
        return {'status': 'error: light is equal to dark value'}
    if (int(input['light']) == int(input['blank'])):
        return {'status': 'error: blank is equal to light value'}
    if (int(input['dark']) == int(input['blank'])):
        return {'status': 'error: dark is equal to blank value'}
    
            
def __setBoard(boardDict):
    board = boardDict['board']
    light = int(boardDict['tokens']['light'])
    dark = int(boardDict['tokens']['dark'])
    numberOfElements = len(board)
    
    if (numberOfElements == 36):
        board[14] = light
        board[15] = dark
        board[20] = dark
        board[21] = light
    if (numberOfElements == 64):
        board[27] = light
        board[28] = dark
        board[35] = dark
        board[36] = light
    if (numberOfElements == 100):
        board[44] = light
        board[45] = dark
        board[54] = dark
        board[55] = light
    if (numberOfElements == 144):
        board[65] = light
        board[66] = dark
        board[77] = dark
        board[78] = light
    if (numberOfElements == 196):
        board[90] = light
        board[91] = dark
        board[104] = dark
        board[105] = light
    if (numberOfElements == 256):
        board[119] = light
        board[120] = dark
        board[135] = dark
        board[136] = light

def _create(parms):
    if ('light' not in parms.keys()):
        parms['light'] = 1
    if ('dark' not in parms.keys()):
        parms['dark'] = 2
    if ('blank' not in parms.keys()):
        parms['blank'] = 0
    if ('size' not in parms.keys()):
        parms['size'] = 8
        
    __checkBoundary(parms)
    
    result = {'board': [int(parms['blank'])] * (int(parms['size']) ** 2), 
              'tokens': {'light': int(parms['light']), 'dark': int(parms['dark']),
                         'blank': int(parms['blank'])
                         },
              'status': 'ok',
              'integrity': ''}
    
    # Setting up the board according to size
    __setBoard(result)

    # Sha256 Hex digest
    light = result['tokens']['light']
    dark = result['tokens']['dark']
    blank = result['tokens']['blank']
    
    message = ''
    for i in result['board']:
        message = message + str(i)
        
    message = message + "/" + str(light) + "/" + str(dark) + "/" + str(blank) + "/" + str(dark)
    sha256HexDigest = hashlib.sha256(message.encode('utf-8')).hexdigest()
    result['integrity'] = sha256HexDigest
    return result
