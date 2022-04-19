def calcSize(currentSize, requestedSize, DatastoreSize):

 

    currentTotal = (DatastoreSize-currentSize)/DatastoreSize

    print("\n  Current Datastore free space is ", round(currentTotal*100, 2) , "%")

 

    newTotal = (DatastoreSize-requestedSize)/DatastoreSize

    #Provide some information about the current free space as percentage

    if (newTotal >= 0) :

        print("  Free space after expanding vmdk would be ", round(newTotal*100, 2) , "%")

    else :

        print("  Note: Requested size is greater than current datastore size")

 

    if (newTotal*100 < 20) :

        print("\n**Expansion is needed**")

        calcSize = DatastoreSize

        #increment datastore size by 1GB until it reaches 20% free

        while (newTotal*100 < 20) :

            calcSize += 1

            newTotal = (calcSize-requestedSize)/calcSize

      

        print("\n  Your new datastore size should be", calcSize, "GB")

        print("  Your total free space will be", round((calcSize-requestedSize)/calcSize*100, 2), "%")

        print("\n**Increase your datastore by", (calcSize-DatastoreSize), "GB** \n")

    elif (newTotal*100 >= 20) :

        print("\n**No Expansion is required**\n")

 

 

currentSize = 0

while (currentSize <= 0) :

    currentSize = int(input("Current datastore used size? (in GB) "))

 

requestedSize = 0

while (requestedSize <= 0) :

    requestedSize = int(input("How much space are we adding? (in GB) "))

requestedSize = requestedSize+currentSize

 

DatastoreSize = 0

while (DatastoreSize <= currentSize) :

    DatastoreSize = int(input("Current Total Datastore LUN size? (in GB) " ))

 

calcSize(currentSize, requestedSize, DatastoreSize)

input("Press enter to exit...")
