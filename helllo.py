n=3
for i in range(n) :
    name=input('enter your password  ').upper()
    name.isascii()
    nme=input('confirm your password  ').upper()
    if name=='' and nme=='':
        print('you have entered  nothing')
    elif name==nme:
        print('password matched')

    else:
        print('password dont match')
        print('first password \t', name)
        print('confirmation password  \t ', nme)
