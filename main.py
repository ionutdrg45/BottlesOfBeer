
def bottles_of_beer(beer_num):
    if beer_num < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer.""")
        return

    tmp = beer_num
    beer_num -= 1
    print("""{} bottles of beer on the wall. {} bottles of beer. Take one down, pass it
    around, {} bottles of beer on the wall""".format(tmp, tmp, beer_num))
    bottles_of_beer(beer_num)

bottles_of_beer(10)