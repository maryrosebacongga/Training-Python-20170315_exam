Bottle_Water_qt = 2
Coke_qt = 5
Sprit_qt = 20
Coffee_qt = 2
Bottle_Water_p = 30
Coke_p = 20
Sprit_p = 10
Coffee_p = 30



print "The total value of our stocks is %d." % (Bottle_Water_p * Bottle_Water_qt + Coke_p * Coke_qt + Sprit_p * Sprit_qt + Coffee_p * Coffee_qt)
print "The Sprit qt and the total value of our stock after we sold 5 Sprit is %d." % (Sprit_qt - 5)
print "If we take 30% off for the coffee, how much we earn less on sold two of coffee", Coffee_p * Coffee_qt * .3