def w(msg):
    while True:
        try:

            return int(input(msg))


        except ValueError:

            print('nuh uh')


print('Enter 1 if equation = (x = y * z)\n')
print('Enter 2 if equation = (x * y = x * z)\n')
choice = w('enter choice:')
while True:
    if choice == 1:
        e = input('enter what variable you want to solve for: ')
        if e == 'x':
            a = input('enter if its addition, subtraction,division, or multiplication: ')
            if a == 'addition':
                print('x = y + z')
                d = input('does x have a coefficient:')
                if d == 'yes':
                    print('Cx = y + z')
                    C = int(input('enter coefficient: '))
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = C / (y + z)
                    print('x =', x)
                if d == 'no':
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = y + z
                    print('x =', x)
            if a == 'subtraction':
                print('x = y - z')
                d = input('does x have a coefficient:')
                if d == 'yes':
                    m = int(input('enter coefficient: '))
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = m / (y - z)
                    print('x =', x)
                if d == 'no':
                    y = int(input('enter y: '))
                    z = int(input('enter z: '))
                    x = y - z
                    print('x =', x)
        if e == 'y':
            aa = input('enter if its addition or subtraction: ')
            if aa == 'addition':
                print('x = y + z')
                x = int(input('enter x: '))
                z = int(input('enter z: '))
                y = x - z
                print('y =', y)
            if aa == 'subtraction':
                print('x = y - z')
                x = int(input('enter x: '))
                z = int(input('enter z: '))
                y = x + z
                print('y =', y)
            if aa == 'multiplication':
                print('y = x * z')
                y = int(input('enter y: '))
                z = int(input('enter z: '))
                x = y / z
                print('x =', x)
            if aa == 'division':
                print('y = x / z')
                y = int(input('enter y: '))
                z = int(input('enter z: '))
                x = y * z
                print('x =', x)
        if e == 'z':
            aaa = input('enter if its addition or subtraction: ')
            if aaa == 'addition':
                print('x = y + z')
                x = int(input('enter x: '))
                y = int(input('enter y: '))
                z = x - y
                print('z =', z)
            if aaa == 'subtraction':
                print('x = y - z')
                x = int(input('enter x: '))
                y = int(input('enter y: '))
                z = x + y
                print('z =', z)
            if aaa == 'multiplication':
                print('x = y * z')
                y = int(input('enter y: '))
                z = int(input('enter z: '))
                x = y * z
                print('x =', x)
            if aaa == 'division':
                print('x = y / z')
                y = int(input('enter y: '))
                z = int(input('enter z: '))
                x = y / z
                print('x =', x)

    if choice == 2:
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
                        print('Cx * y = z * Cx')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('Cx + y = z * Cx')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx + y = z + Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = (z - y) / (C - c)
                                print(x)
                            if c == 'subtraction':
                                print('Cx + y = z - Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = (z - y) / (C + c)
                                print(x)
                            if c == 'multiplication':
                                print('Cx + y = z * Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = y / (z * c - C)
                                print(x)
                            if c == 'division':
                                print('Cx + y = z / Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = y / (z / c - C)
                                print(x)

                        if w == 'subtraction':
                            print('Cx - y = z * Cx')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx - y = z + Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = (z + y) / (C - c)
                                print(x)
                            if c == 'subtraction':
                                print('Cx - y = z - Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = (z + y) / (C + c)
                                print(x)
                            if c == 'multiplication':
                                print('Cx - y = z * Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = y / (z * c + C)
                                print(x)
                            if c == 'division':
                                print('Cx - y = z / Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = y / (z / c + C)
                                print(x)

                        if w == 'multiplication':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx * y = z + Cx')
                                C = int(input('enter the left side coefficient: '))
                                c = int(input('enter the right side coefficient: '))
                                y = int(input('enter y: '))
                                z = int(input('enter z: '))
                                x = c - (C * y)
                                print(x)
                            if c == 'subtraction':
                                print('Cx * y = z - Cx')

                            if c == 'multiplication':
                                print('Cx * y = z * Cx')

                            if c == 'division':
                                print('Cx * y = z / Cx')

                        if w == 'division':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx / y = z + Cx')
                            if c == 'subtraction':
                                print('Cx / y = z - Cx')
                            if c == 'multiplication':
                                print('Cx / y = z * Cx')
                            if c == 'division':
                                print('Cx / y = z / Cx')
                if m == 'no':
                    print('Cx * y = z * x')
                    w = input('what is the left side opperation(addition, subtraction, multiplication, or division):')
                    if w == 'addition':
                        print('Cx + y = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('Cx + y = z + x')
                        if c == 'subtraction':
                            print('Cx + y = z - x')
                        if c == 'multiplication':
                            print('Cx + y = z * x')
                        if c == 'division':
                            print('Cx + y = z / x')

                    if w == 'subtraction':
                        print('Cx - y = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('Cx - y = z + x')
                        if c == 'subtraction':
                            print('Cx - y = z - x')
                        if c == 'multiplication':
                            print('Cx - y = z * x')
                        if c == 'division':
                            print('Cx - y = z / x')

                    if w == 'multiplication':
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('Cx * y = z + x')
                        if c == 'subtraction':
                            print('Cx * y = z - x')
                        if c == 'multiplication':
                            print('Cx * y = z * x')
                        if c == 'division':
                            print('Cx * y = z / x')

                    if w == 'division':
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('Cx / y = z + x')
                        if c == 'subtraction':
                            print('Cx / y = z - x')
                        if c == 'multiplication':
                            print('Cx / y = z * x')
                        if c == 'division':
                            print('Cx / y = z / x')

                if d == 'no':
                    print('x * y = z * x')
                    m = input('does the right side x have a coefficient: ')
                    if m == 'yes':
                        print('x * y = z * Cx')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('x + y = z * Cx')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x + y = z + Cx')
                            if c == 'subtraction':
                                print('x + y = z - Cx')
                            if c == 'multiplication':
                                print('x + y = z * Cx')
                            if c == 'division':
                                print('x + y = z / Cx')

                        if w == 'subtraction':
                            print('x - y = z * Cx')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x - y = z + Cx')
                            if c == 'subtraction':
                                print('x - y = z - Cx')
                            if c == 'multiplication':
                                print('x - y = z * Cx')
                            if c == 'division':
                                print('x - y = z / Cx')

                        if w == 'multiplication':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x * y = z + Cx')
                            if c == 'subtraction':
                                print('x * y = z - Cx')
                            if c == 'multiplication':
                                print('x * y = z * Cx')
                            if c == 'division':
                                print('x * y = z / Cx')
                        if w == 'division':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x / y = z + Cx')
                            if c == 'subtraction':
                                print('x / y = z - Cx')
                            if c == 'multiplication':
                                print('x / y = z * Cx')
                            if c == 'division':
                                print('x / y = z / Cx')
                    if m == 'no':
                        print('x * y = z * x')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('x + y = z * x')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x + y = z + x')
                            if c == 'subtraction':
                                print('x + y = z - x')
                            if c == 'multiplication':
                                print('x + y = z * x')
                            if c == 'division':
                                print('x + y = z / x')

                        if w == 'subtraction':
                            print('x - y = z * x')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x - y = z + x')
                            if c == 'subtraction':
                                print('x - y = z - x')
                            if c == 'multiplication':
                                print('x - y = z * x')
                            if c == 'division':
                                print('x - y = z / x')

                        if w == 'multiplication':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x * y = z + x')
                            if c == 'subtraction':
                                print('x * y = z - x')
                            if c == 'multiplication':
                                print('x * y = z * x')
                            if c == 'division':
                                print('x * y = z / x')

                        if w == 'division':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x / y = z + x')
                            if c == 'subtraction':
                                print('x / y = z - x')
                            if c == 'multiplication':
                                print('x / y = z * x')
                            if c == 'division':
                                print('x / y = z / x')

            if f == 'xz':
                print('x * y = x * z')
                d = input('does the left side x have a coefficient: ')
                if d == 'yes':
                    print('Cx * y = x * z')
                    m = input('does the right side x have a coefficient: ')
                    if m == 'yes':
                        print('Cx * y = Cx * z')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('Cx + y = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx + y = Cx + z')
                            if c == 'subtraction':
                                print('Cx + y = Cx - z')
                            if c == 'multiplication':
                                print('Cx + y = Cx * z')
                            if c == 'division':
                                print('Cx + y = Cx / z')

                        if w == 'subtraction':
                            print('Cx - y = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx - y = Cx + z')
                            if c == 'subtraction':
                                print('Cx - y = Cx - z')
                            if c == 'multiplication':
                                print('Cx - y = Cx * z')
                            if c == 'division':
                                print('Cx - y = Cx / z')

                        if w == 'multiplication':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx * y = Cx + z')
                            if c == 'subtraction':
                                print('Cx * y = Cx - z')
                            if c == 'multiplication':
                                print('Cx * y = Cx * z')
                            if c == 'division':
                                print('Cx * y = Cx / z')
                        if w == 'division':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('Cx / y = Cx + z')
                            if c == 'subtraction':
                                print('Cx / y = Cx - z')
                            if c == 'multiplication':
                                print('Cx / y = Cx * z')
                            if c == 'division':
                                print('Cx / y = Cx / z')
                        if m == 'no':
                            print('Cx * y = x * z')
                            w = input(
                                'what is the left side opperation(addition, subtraction, multiplication, or division):')
                            if w == 'addition':
                                print('Cx + y = x * z')
                                c = input(
                                    'what is the right side opperation(addition, subtraction, multiplication, or division):')
                                if c == 'addition':
                                    print('Cx + y = x * z')
                                if c == 'subtraction':
                                    print('Cx + y = x - z')
                                if c == 'multiplication':
                                    print('Cx + y = x * z')
                                if c == 'division':
                                    print('Cx + y = x / z')

                            if w == 'subtraction':
                                print('Cx - y = z * x')
                                c = input(
                                    'what is the right side opperation(addition, subtraction, multiplication, or division):')
                                if c == 'addition':
                                    print('Cx - y = x + z')
                                if c == 'subtraction':
                                    print('Cx - y = x - z')
                                if c == 'multiplication':
                                    print('Cx - y = x * z')
                                if c == 'division':
                                    print('Cx - y = x / z')

                            if w == 'multiplication':
                                print('Cx * y = x * z')
                                c = input(
                                    'what is the right side opperation(addition, subtraction, multiplication, or division):')
                                if c == 'addition':
                                    print('Cx * y = x + z')
                                if c == 'subtraction':
                                    print('Cx * y = x - z')
                                if c == 'multiplication':
                                    print('Cx * y = x * z')
                                if c == 'division':
                                    print('Cx * y = x / z')

                            if w == 'division':
                                print('Cx / y = x * z')
                                c = input(
                                    'what is the right side opperation(addition, subtraction, multiplication, or division):')
                                if c == 'addition':
                                    print('Cx / y = x + z')
                                if c == 'subtraction':
                                    print('Cx / y = x - z')
                                if c == 'multiplication':
                                    print('Cx / y = x * z')
                                if c == 'division':
                                    print('Cx / y = x / z')

                if d == 'no':
                    print('x * y = x * z')
                    m = input('does the right side x have a coefficient: ')
                    if m == 'yes':
                        print('x * y = Cx * z')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('x + y = z * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x + y = Cx + z')
                            if c == 'subtraction':
                                print('x + y = Cx - z')
                            if c == 'multiplication':
                                print('x + y = Cx * z')
                            if c == 'division':
                                print('x + y = Cx / z')

                        if w == 'subtraction':
                            print('x - y = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x - y = Cx + z')
                            if c == 'subtraction':
                                print('x - y = Cx - z')
                            if c == 'multiplication':
                                print('x - y = Cx * z')
                            if c == 'division':
                                print('x - y = Cx / z')

                        if w == 'multiplication':
                            print('x * y = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x * y = Cx + z')
                            if c == 'subtraction':
                                print('x * y = Cx - z')
                            if c == 'multiplication':
                                print('x * y = Cx * z')
                            if c == 'division':
                                print('x * y = Cx / z')
                        if w == 'division':
                            print('x / y = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x / y = Cx + z')
                            if c == 'subtraction':
                                print('x / y = Cx - z')
                            if c == 'multiplication':
                                print('x / y = Cx * z')
                            if c == 'division':
                                print('x / y = Cx / z')
                    if m == 'no':
                        print('x * y = x * z')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('x + y = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x + y = x + z')
                            if c == 'subtraction':
                                print('x + y = x - z')
                            if c == 'multiplication':
                                print('x + y = x * z')
                            if c == 'division':
                                print('x + y = x / z')

                        if w == 'subtraction':
                            print('x - y = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x - y = x + z')
                            if c == 'subtraction':
                                print('x - y = x - z')
                            if c == 'multiplication':
                                print('x - y = x * z')
                            if c == 'division':
                                print('x - y = x / z')

                        if w == 'multiplication':
                            print('x * y = x * z'')')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x * y = x + z')
                            if c == 'subtraction':
                                print('x * y = x - z')
                            if c == 'multiplication':
                                print('x * y = x * z')
                            if c == 'division':
                                print('x * y = x / z')

                        if w == 'division':
                            print('x / y = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('x / y = x + z')
                            if c == 'subtraction':
                                print('x / y = x - z')
                            if c == 'multiplication':
                                print('x / y = x * z')
                            if c == 'division':
                                print('x / y = x / z')
        if a == 'yx':
            print('y * x = z * x')
            f = input('enter the right sides order(zx or xz):')
            if f == 'zx':
                print('y * x = z * x')
                d = input('does the left side x have a coefficient: ')
                if d == 'yes':
                    print('y * Cx = z * x')
                    m = input('does the right side x have a coefficient: ')
                    if m == 'yes':
                        print('y * Cx = z * Cx')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('y + Cx = z * Cx')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y + Cx = z + Cx')
                            if c == 'subtraction':
                                print('y + Cx = z - Cx')
                            if c == 'multiplication':
                                print('y + Cx = z * Cx')
                            if c == 'division':
                                print('y + Cx = z / Cx')

                    if w == 'subtraction':
                        print('y - Cx = z * Cx')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y - Cx = z + Cx')
                        if c == 'subtraction':
                            print('y - Cx = z - Cx')
                        if c == 'multiplication':
                            print('y - Cx = z * Cx')
                        if c == 'division':
                            print('y - Cx = z / Cx')

                    if w == 'multiplication':
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y * Cx = z + Cx')
                        if c == 'subtraction':
                            print('y * Cx = z - Cx')
                        if c == 'multiplication':
                            print('y * Cx = z * Cx')
                        if c == 'division':
                            print('y * Cx = z / Cx')
                    if w == 'division':
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y / Cx = z + Cx')
                        if c == 'subtraction':
                            print('y / Cx = z - Cx')
                        if c == 'multiplication':
                            print('y / Cx = z * Cx')
                        if c == 'division':
                            print('y / Cx = z / Cx')
                if m == 'no':
                    print('y * Cx = z * x')
                    w = input('what is the left side opperation(addition, subtraction, multiplication, or division):')
                    if w == 'addition':
                        print('y + Cx = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y + Cx = z + x')
                        if c == 'subtraction':
                            print('y + Cx = z - x')
                        if c == 'multiplication':
                            print('y + Cx = z * x')
                        if c == 'division':
                            print('y + Cx = z / x')

                    if w == 'subtraction':
                        print('y - Cx = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y - Cx = z + x')
                        if c == 'subtraction':
                            print('y - Cx = z - x')
                        if c == 'multiplication':
                            print('y - Cx = z * x')
                        if c == 'division':
                            print('y - Cx = z / x')

                    if w == 'multiplication':
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y * Cx = z + x')
                        if c == 'subtraction':
                            print('y * Cx = z - x')
                        if c == 'multiplication':
                            print('y * Cx = z * x')
                        if c == 'division':
                            print('y * Cx = z / x')

                    if w == 'division':
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y / Cx = z + x')
                        if c == 'subtraction':
                            print('y / Cx = z - x')
                        if c == 'multiplication':
                            print('y / Cx = z * x')
                        if c == 'division':
                            print('y / Cx = z / x')

            if d == 'no':
                print('y * x = z * x')
                m = input('does the right side x have a coefficient: ')
                if m == 'yes':
                    print('y * x = z * Cx')
                    w = input('what is the left side opperation(addition, subtraction, multiplication, or division):')
                    if w == 'addition':
                        print('y + x = z * Cx')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y + x = z + Cx')
                        if c == 'subtraction':
                            print('y + x = z - Cx')
                        if c == 'multiplication':
                            print('y + x = z * Cx')
                        if c == 'division':
                            print('y + x = z / Cx')

                    if w == 'subtraction':
                        print('y - y = z * Cx')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y - x = z + Cx')
                        if c == 'subtraction':
                            print('y - x = z - Cx')
                        if c == 'multiplication':
                            print('y - x = z * Cx')
                        if c == 'division':
                            print('y - x = z / Cx')

                    if w == 'multiplication':
                        print('y * x = z * Cx')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y * x = z + Cx')
                        if c == 'subtraction':
                            print('y * x = z - Cx')
                        if c == 'multiplication':
                            print('y * x = z * Cx')
                        if c == 'division':
                            print('y * x = z / Cx')
                    if w == 'division':
                        print('y / x = z * Cx')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y / x = z + Cx')
                        if c == 'subtraction':
                            print('y / x = z - Cx')
                        if c == 'multiplication':
                            print('y / x = z * Cx')
                        if c == 'division':
                            print('y / x = z / Cx')
                if m == 'no':
                    print('y * x = z * x')
                    w = input('what is the left side opperation(addition, subtraction, multiplication, or division):')
                    if w == 'addition':
                        print('y + x = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y + x = z + x')
                        if c == 'subtraction':
                            print('y + x = z - x')
                        if c == 'multiplication':
                            print('y + x = z * x')
                        if c == 'division':
                            print('y + x = z / x')

                    if w == 'subtraction':
                        print('y - x = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y - x = z + x')
                        if c == 'subtraction':
                            print('y - x = z - x')
                        if c == 'multiplication':
                            print('y - x = z * x')
                        if c == 'division':
                            print('y - x = z / x')

                    if w == 'multiplication':
                        print('y * x = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y * x = z + x')
                        if c == 'subtraction':
                            print('y * x = z - x')
                        if c == 'multiplication':
                            print('y * x = z * x')
                        if c == 'division':
                            print('y * x = z / x')

                    if w == 'division':
                        print('y / x = z * x')
                        c = input(
                            'what is the right side opperation(addition, subtraction, multiplication, or division):')
                        if c == 'addition':
                            print('y / x = z + x')
                        if c == 'subtraction':
                            print('y / x = z - x')
                        if c == 'multiplication':
                            print('y / x = z * x')
                        if c == 'division':
                            print('y / x = z / x')

            if f == xz:
                print('y * x = x * z')
                d = input('does the left side x have a coefficient: ')
                if d == 'yes':
                    print('y * Cx = x * z')
                    m = input('does the right side x have a coefficient: ')
                    if m == 'yes':
                        print('y * Cx = Cx * z')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('y + Cx = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y + Cx = Cx + z')
                            if c == 'subtraction':
                                print('y + Cx = Cx - z')
                            if c == 'multiplication':
                                print('y + Cx = Cx * z')
                            if c == 'division':
                                print('y + Cx = Cx / z')

                        if w == 'subtraction':
                            print('y - Cx = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y - Cx = Cx + z')
                            if c == 'subtraction':
                                print('y - Cx = Cx - z')
                            if c == 'multiplication':
                                print('y - Cx = Cx * z')
                            if c == 'division':
                                print('y - Cx = Cx / z')

                        if w == 'multiplication':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y * Cx = Cx + z')
                            if c == 'subtraction':
                                print('y * Cx = Cx - z')
                            if c == 'multiplication':
                                print('y * Cx = Cx * z')
                            if c == 'division':
                                print('y * Cx = Cx / z')
                        if w == 'division':
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y / Cx = Cx + z')
                            if c == 'subtraction':
                                print('y / Cx = Cx - z')
                            if c == 'multiplication':
                                print('y / Cx = Cx * z')
                            if c == 'division':
                                print('y / Cx = Cx / z')
                    if m == 'no':
                        print('y * Cx = x * z')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('y + Cx = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y + Cx = x * z')
                            if c == 'subtraction':
                                print('y + Cx = x - z')
                            if c == 'multiplication':
                                print('y + Cx = x * z')
                            if c == 'division':
                                print('y + Cx = x / z')

                        if w == 'subtraction':
                            print('y - Cx = z * x')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y - Cx = x + z')
                            if c == 'subtraction':
                                print('y - Cx = x - z')
                            if c == 'multiplication':
                                print('y - Cx = x * z')
                            if c == 'division':
                                print('y - Cx = x / z')

                        if w == 'multiplication':
                            print('y * Cx = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y * Cx = x + z')
                            if c == 'subtraction':
                                print('y * Cx = x - z')
                            if c == 'multiplication':
                                print('y * Cx = x * z')
                            if c == 'division':
                                print('y * Cx = x / z')

                        if w == 'division':
                            print('y / Cx = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y / Cx = x + z')
                            if c == 'subtraction':
                                print('y / Cx = x - z')
                            if c == 'multiplication':
                                print('y / Cx = x * z')
                            if c == 'division':
                                print('y / Cx = x / z')

                if d == 'no':
                    print('y * y = x * z')
                    m = input('does the right side x have a coefficient: ')
                    if m == 'yes':
                        print('y * x = Cx * z')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('y + x = z * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y + x = Cx + z')
                            if c == 'subtraction':
                                print('y + x = Cx - z')
                            if c == 'multiplication':
                                print('y + x = Cx * z')
                            if c == 'division':
                                print('y + x = Cx / z')

                        if w == 'subtraction':
                            print('y - x = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y - x = Cx + z')
                            if c == 'subtraction':
                                print('y - x = Cx - z')
                            if c == 'multiplication':
                                print('y - x = Cx * z')
                            if c == 'division':
                                print('y - x = Cx / z')

                        if w == 'multiplication':
                            print('y * x = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y * x = Cx + z')
                            if c == 'subtraction':
                                print('y * x = Cx - z')
                            if c == 'multiplication':
                                print('y * x = Cx * z')
                            if c == 'division':
                                print('y * x = Cx / z')
                        if w == 'division':
                            print('y / x = Cx * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y / x = Cx + z')
                            if c == 'subtraction':
                                print('y / x = Cx - z')
                            if c == 'multiplication':
                                print('y / x = Cx * z')
                            if c == 'division':
                                print('y / x = Cx / z')
                    if m == 'no':
                        print('y * x = x * z')
                        w = input(
                            'what is the left side opperation(addition, subtraction, multiplication, or division):')
                        if w == 'addition':
                            print('y + x = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y + x = x + z')
                            if c == 'subtraction':
                                print('y + x = x - z')
                            if c == 'multiplication':
                                print('y + x = x * z')
                            if c == 'division':
                                print('y + x = x / z')

                        if w == 'subtraction':
                            print('y - x = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y - x = x + z')
                            if c == 'subtraction':
                                print('y - x = x - z')
                            if c == 'multiplication':
                                print('y - x = x * z')
                            if c == 'division':
                                print('y - x = x / z')

                        if w == 'multiplication':
                            print('y * x = x * z'')')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y * x = x + z')
                            if c == 'subtraction':
                                print('y * x = x - z')
                            if c == 'multiplication':
                                print('y * x = x * z')
                            if c == 'division':
                                print('y * x = x / z')

                        if w == 'division':
                            print('y / x = x * z')
                            c = input(
                                'what is the right side opperation(addition, subtraction, multiplication, or division):')
                            if c == 'addition':
                                print('y / x = x + z')
                            if c == 'subtraction':
                                print('y / x = x - z')
                            if c == 'multiplication':
                                print('y / x = x * z')
                            if c == 'division':
                                print('y / x = x / z')









