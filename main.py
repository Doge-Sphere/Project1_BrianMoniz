shopperName="keanu reaves".title()

groceryPrices=[55.99,21.99,9.99,2.99,199.99]
groceriesPurchases=[5,1,2,6,3]

totalCost=0
averageCost=0
itemsPurchased=0

for i in (range(0,len(groceriesPurchases))):
    totalCost=totalCost+groceryPrices[i]*groceriesPurchases[i]
    itemsPurchased+=groceriesPurchases[i]

averageCost=totalCost/itemsPurchased
averageCost=round(averageCost,2)

print(f"{shopperName}: Total bill ${totalCost}, average price per item ${averageCost}")

#----------------------------------------------------------------------------------------------------------

shopperName="ADAM saNdler".title()

groceryPrices=[12.99,57.99,32.99,1999.99,472.99]
groceriesPurchases=[1,2,8,4,1]

totalCost=0
averageCost=0
itemsPurchased=0

for i in (range(0,len(groceriesPurchases))):
    totalCost=totalCost+groceryPrices[i]*groceriesPurchases[i]
    itemsPurchased+=groceriesPurchases[i]

averageCost=totalCost/itemsPurchased
averageCost=round(averageCost,2)

print(f"{shopperName}: Total bill ${totalCost}, average price per item ${averageCost}")