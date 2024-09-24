def w(msg):

    while True:
        try:

            return int(input(msg))

        except ValueError:

            print ('nuh uh')

print ('Enter 1 if equation = (x = y +/-/*/div z)\n')
print('Enter 2 if equation = (x = y */div z)\n')
choice = w('enter choice:')
while True:
    if choice == 1:
        e=input('enter what variable you want to solve for: ')
        if e == 'x':
            a=input('enter if its addition, subtraction,division, or multiplication: ')
            if a == 'addition':
                print('x = y + z')
                d=input('does x have a coefficient:')
                if d == 'yes':
                    print('Cx = y + z')
                    C=int(input('enter coefficient: '))
                    y=int(input('enter y: '))
                    z=int(input('enter z: '))
                    x=C/(y+z)
                    print ('x =',x)
                if d == 'no':
                    y=int(input('enter y: '))
                    z=int(input('enter z: '))
                    x=y+z
                    print ('x =',x)
            if a == 'subtraction':
                print('x = y - z')
                d=input('does x have a coefficient:')
                if d == 'yes':
                    m=int(input('enter coefficient: '))
                    y=int(input('enter y: '))
                    z=int(input('enter z: '))
                    x=m/(y-z)
                    print ('x =',x)
                if d == 'no':
                    y=int(input('enter y: '))
                    z=int(input('enter z: '))
                    x=y-z
                    print ('x =',x)
        if e == 'y':
            aa=input('enter if its addition or subtraction: ')
            if aa == 'addition':
                print('x = y + z')
                x=int(input('enter x: '))
                z=int(input('enter z: '))
                y=x-z
                print ('y =',y)
            if aa == 'subtraction':
                print('x = y - z')
                x=int(input('enter x: '))
                z=int(input('enter z: '))
                y=x+z
                print ('y =',y)
            if aa == 'multiplication':
                print('y = x * z')
                y=int(input('enter y: '))
                z=int(input('enter z: '))
                x=y/z
                print ('x =',x)
            if aa == 'division':
                print('y = x / z')
                y=int(input('enter y: '))
                z=int(input('enter z: '))
                x=y*z
                print ('x =',x)
        if e == 'z':
            aaa=input('enter if its addition or subtraction: ')
            if aaa == 'addition':
                print('x = y + z')
                x=int(input('enter x: '))
                y=int(input('enter y: '))
                z=x-y
                print ('z =',z)
            if aaa == 'subtraction':
                print('x = y - z')
                x=int(input('enter x: '))
                y=int(input('enter y: '))
                z=x+y
                print ('z =',z)
            if aaa == 'multiplication':
                print('x = y * z')
                y=int(input('enter y: '))
                z=int(input('enter z: '))
                x=y*z
                print ('x =',x)
            if aaa == 'division':
                print('x = y / z')
                y=int(input('enter y: '))
                z=int(input('enter z: '))
                x=y/z
                print ('x =',x)


    if choice == 2:
        e = input('enter what variable you want to solve for: ')
        if e == 'x':
            a = input('enter the order of the variables on the left side(xy or yx): ')
            if a == 'xy':
                print('x * y = z * x')
                f = input('enter the right sides order(zx or xz):')
                if f == 'zx':
                    print('x * y = z * x')
                    d = input('does the left side x have a coefficient: ')
                    if d == 'yes':
                        print('Cx * y = z * x')
                        m = input('does the right side x have a coefficient: ')
                        if m == 'yes':
                            print('Cx * y = z * x')
                            y = int(input('enter y: '))
                            z = int(input('enter z: '))
                            x = (y - z) * m
                            print('x =', x)
                        if m == 'no':
                            print('Cx * y = z * x')
                            y = int(input('enter y: '))
                            z = int(input('enter z: '))
                            x = (y - z) * m
                            print('x =', x)
                    if d == 'no':
                        print('x * y = z * n')
                        m = input('does the right side x have a coefficient: ')
                        if m == 'yes':


                        y = int(input('enter y: '))
                        z = int(input('enter z: '))
                        x = (y - z) * m
                        print('x =', x)


                if f == 'xz':
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = y + z
                    print('x =', x)
            if a == 'yx':
                print('y * x = z * n')
                d = input('does x have a coefficient:')
                if d == 'yes':
                    print('Cx = y - z')
                    m = int(input('enter coefficient: '))
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = (y - z) * m
                    print('x =', x)
                    if d == 'no':
                        y = int(input('enter y: '))
                        z = int(input('enter z: '))
                        x = y - z
                        print('x =', x)

            if a == 'multiplication':
                print('x = y * z')
                d = input('does x have a coefficient:')
                if d == 'yes':
                    print('Cx = y * z')
                    m = int(input('enter coefficient: '))
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = (y * z) * m
                    print('x =', x)
                if d == 'no':
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = y * z
                    print('x =', x)
            if a == 'division':
                print('x = y / z')
                d = input('does x have a coefficient:')
                if d == 'yes':
                    print('Cx = y / z')
                    m = int(input('enter coefficient: '))
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = (y / z) * m
                    print('x =', x)
                if d == 'no':
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = y / z
                    print('x =', x)
        if e == 'y':
            a = input('enter if its addition, subtraction, multiplication, or division: ')
            if a == 'addition':
                print('x = y + z')
                d = input('does y have a coefficient:')
                if d == 'yes':
                    print('x = Cy + z')
                    m = int(input('enter coefficient: '))
                    x = int(input('enter x: '))
                    z = int(input('enter z: '))
                    y = (x - z) / m
                    print('y =', y)
                if d == 'no':
                    x = int(input('enter x: '))
                    z = int(input('enter z: '))
                    y = x - z
                    print('y =', y)
            if a == 'subtraction':
                print('x = y - z')
                d = input('does y have a coefficient:')
                if d == 'yes':
                    print('x = Cy - z')
                    m = int(input('enter coefficient: '))
                    x = int(input('enter x: '))
                    z = int(input('enter z: '))
                    y = (x + z) / m
                    print('y =', y)
                    if d == 'no':
                        x = int(input('enter x: '))
                        z = int(input('enter z: '))
                        y = x + z
                        print('y =', y)

            if a == 'multiplication':
                print('x = y * z')
                d = input('does x have a coefficient:')
                if d == 'yes':
                    print('x = Cy * z')
                    m = int(input('enter coefficient: '))
                    x = int(input('enter x: '))
                    z = int(input('enter z: '))
                    y = (x / z) / m
                    print('y =', y)
                if d == 'no':
                    x = int(input('enter x: '))
                    z = int(input('enter z: '))
                    y = x / z
                    print('y =', y)
            if a == 'division':
                print('x = y / z')
                d = input('does x have a coefficient:')
                if d == 'yes':
                    print('x = Cy / z')
                    m = int(input('enter coefficient: '))
                    x = int(input('enter x: '))
                    z = int(input('enter z: '))
                    y = (x * z) / m
                    print('y =', y)
                if d == 'no':
                    x = int(input('enter x: '))
                    z = int(input('enter z: '))
                    y = x * z
                    print('y =', y)
        if e == 'z':
            a = input('enter if its addition, subtraction, multiplication, or division: ')
            if a == 'addition':
                print('x = y + z')
                d = input('does z have a coefficient:')
                if d == 'yes':
                    print('x = y + Cz')
                    m = float(input('enter coefficient: '))
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = (x - y) / m
                    print('z =', z)
                if d == 'no':
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = x - y
                    print('z =', z)
            if a == 'subtraction':
                print('x = y - z')
                d = input('does z have a coefficient:')
                if d == 'yes':
                    print('x = y - Cz')
                    m = float(input('enter coefficient: '))
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = (x - y) / m
                    print('z =', z)
                if d == 'no':
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = x - y
                    print('z =', z)

            if a == 'multiplication':
                print('x = y * z')
                d = input('does z have a coefficient:')
                if d == 'yes':
                    print('x = y * Cz')
                    m = float(input('enter coefficient: '))
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = (x / y) / m
                    print('z =', z)
                if d == 'no':
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = x / y
                    print('z =', z)
            if a == 'division':
                print('x = y / z')
                d = input('does z have a coefficient:')
                if d == 'yes':
                    print('x = y / Cz')
                    m = float(input('enter coefficient: '))
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = (y / x) / m
                    print('z =', z)
                if d == 'no':
                    x = float(input('enter x: '))
                    y = float(input('enter y: '))
                    z = y / x
                    print('z =', z)

