def _create(parms):
    try: (int(parms['light']))
    except ValueError:
        return {'status': 'error: non-integer light value'}
    
    if (int(parms['light']) > 9):
        result = {'status': 'error: above bound light value'}
    elif (int(parms['light']) < 0):
        result = {'status': 'error: below bound light value'}
        
    return result
