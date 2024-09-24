print('hello world')

enemyDict={
    'blorgo' : {
        'size' : 'huge',
        'damage' : [100],
        'hp' : [500],
        'speed' : [10],
        'attribute' : 'tank, weilds a huge sword',
    },
    'drannon' : {
        'size' : 'tiny',
        'damage' : [20],
        'hp' : [100],
        'speed' : [30],
        'attribute' : 'small little creature that is a speed demon',
    },
    'throg' : {
        'size' : 'human sized',
        'damage' : [100],
        'hp' : [400],
        'speed' : [18],
        'attribute' : 'super intelligent, amazing at reading attacks',
    },
    'brackon' : {
        'size' : 'biggest of them all',
        'damage' : [150],
        'hp' : [800],
        'speed' : [20],
        'attribute' : 'looks akin to a dragon with no wings',
    },
    'gorgon' : {
        'size' : 'small as a dog',
        'damage' : [80],
        'hp' : [200],
        'speed' : [25],
        'attribute' : 'can fly using its wings',

    },
}


print(enemyDict)
d=input('do you want to change the stats of an enemy? : ')

if d == 'yes':
    enemyDict[input("ok, what enemy do you want to change: ")][input('what is the quality you want to change: ')] = [int(input('ok, enter the changed value:'))]

print(enemyDict)


if d == 'no':
    print("ok.")
