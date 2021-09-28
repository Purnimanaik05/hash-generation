import hashlib

print('\n Hashing Algorithms\n')
print('1)md5')
print('2)sha1')
print('3)sha224')
print('4)sha256')
print('5)sha384')
print('6)sha512')

msg = input('\n Enter message:')
cont = 'yes'
while cont == 'yes':
    algo = input('\n Enter Hashing algorithm:')
    if algo == 'md5':
        print('\nMessage:',msg)
        result = hashlib.md5(msg.encode())
        print('\n The hexadecimal equivalent of md5 is:')
        print (result.hexdigest())
              
        cont = input('\n Continue?')

    elif algo == 'sha1':
        print('\nMessage:',msg)
        result = hashlib.sha1(msg.encode())
        print('\n The hexadecimal equivalent of sha1 is:')
        print (result.hexdigest())
              
        cont = input('\n Continue?')

    elif algo == 'sha224':
        print('\nMessage:',msg)
        result = hashlib.sha224(msg.encode())
        print('\n The hexadecimal equivalent of sha224 is:')
        print (result.hexdigest())
              
        cont = input('\n Continue?')

    elif algo == 'sha256':
        print('\nMessage:',msg)
        result = hashlib.sha256(msg.encode())
        print('\n The hexadecimal equivalent of sha256 is:')
        print (result.hexdigest())
              
        cont = input('\n Continue?')

    elif algo == 'sha384':
        print('\nMessage:',msg)
        result = hashlib.sha384(msg.encode())
        print('\n The hexadecimal equivalent of sha384 is:')
        print (result.hexdigest())
              
        cont = input('\n Continue?')

    else :
        algo == 'sha512'
        print('\nMessage:',msg)
        result = hashlib.sha512(msg.encode())
        print('\n The hexadecimal equivalent of sha512 is:')
        print (result.hexdigest())
              
        cont = input('\n Continue?')

   
    
              
              
