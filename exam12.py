
Coke_stock=10
Sprit_stock=20
Beer_stock= 15

Coke_price= 2
Sprit_price= 5
Beer_price= 13



total= 0
coke_purchase = 0
Sprit_purchase = 0
beer_purchase = 0



print "We still have %d Coke($%d), %d Sprint($%d) %d Beer($%d) in machine,\nWhat do you want?" % (Coke_stock, Coke_price, Sprit_stock, Sprit_price, Beer_stock, Beer_price)





while True:
    print "If you want something\n press\n C for Coke\n S for Sprint\n B for Beer.\n F for Finish."
    choice = raw_input("> ")

    if choice == "c":
        print "you just purchase 1 coke. that's $%d." % Coke_price
        Coke_stock = Coke_stock - 1
        coke_purchase =coke_purchase + 1
        print "coke has %d left." % Coke_stock
        print  "you have %d added" % coke_purchase
    elif choice == "s":
        print "you just purchase 1 sprit. that's $%d." % Sprit_price
        Sprit_stock = Sprit_stock - 1
        Sprit_purchase = Sprit_purchase + 1
        print "sprite has %d left." % Sprit_stock
        print  "you have %d added" % Sprit_purchase

    elif choice == "b":
        print "you just purchase 1 beer. that's $%d." % Beer_price
        Beer_stock = Beer_stock - 1
        beer_purchase = beer_purchase + 1
        print "beer has %d left." % Beer_stock
        print  "you have %d added" % beer_purchase

    elif choice == "f":
        print "-" * 30
        print  "Thank you for purchasing."
        print "-" * 30
        print "\n"

        print "Following is your purchase for today:"


        print "\tCK-%d $%d\n \tSP-%d $%d\n \tB-%d $%d" % (coke_purchase,coke_purchase * Coke_price, Sprit_purchase, Sprit_purchase * Sprit_price,beer_purchase,beer_purchase * Beer_price)

        print "\n"
        print "-" * 30
        print "Total is $  %d" % (coke_purchase * Coke_price + Sprit_purchase * Sprit_price +beer_purchase * Beer_price)
        print "-" * 30
        exit()

    else:
        print "Thank you!"
        exit()











