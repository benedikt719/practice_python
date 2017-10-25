
# My thought

def Beers():
    beers = 99

    while beers > 0:

        print("%s bottles of beer on the wall, %s bottles of beer" % (beers, beers))

        beers -= 1

        print("Take one down and pass it around, %s bottles of beer on the wall.\n" % beers)

        if beers == 1:
            print('1 bottle of beer on the wall, 1 bottles of beer.\n'
                  'Take one down and pass it around, 0 bottle of beer on the wall.\n\n'
                  'No more bottles of beer on the wall, no more bottles of beer.\n'
                  'Go to the store and buy some more, 99 bottles of beer on the wall.')

            break


# how simple this code is!

Start = 99


def example_beers(i, leading):
    if i < 0:
        i = Start
    _n = "N" if leading else "n"
    _s = "s" if i != 1 else ""
    _i = str(i) if i != 0 else _n + "o more"
    return _i + ' bottle' + _s


take_or_buy = lambda i: "Go to the store and buy sone more" if i == 0 else "Take one down pass it around"

for i in range(Start, -1, -1):
    print(example_beers(i, True) + ' of beer on the wall,' + example_beers(i, False) + " of beer.")
    print(take_or_buy(i) + ", " + example_beers(i, False) + ' of beer on the wall')
    print('')

#nothing
