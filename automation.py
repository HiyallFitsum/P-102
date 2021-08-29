import time

class ChoreOperator():
    def __init__(self, chore):
        self.chore = chore

    def executeChores(self):
       self.chore = input("What chore do you want done? Dish_Washing, Sweeping, Mopping, or Folding_Clothes? ")

       if self.chore == "Dish_Washing":
            print("Set to Dish_Washing:")
            dishNumber = int(input("How many dishes would you like to be washed? "))
            washingTime = dishNumber*60 
            startTime = time.time()
            dishChoreTime = startTime + washingTime
            print("The dishes will be completly washed in", washingTime/60,"minute/s")
            if dishChoreTime >= time.time():
                print("The dishes are washed.")
                    
        
       elif self.chore == "Sweeping":
            print("Set to Sweeping:")
            floorNumber = int(input("How many floors would you like to be sweeped? "))
            sweepingTime = floorNumber*2400
            sweepingChoreTime = time.time()
            print("The floors will be completly sweeped in", sweepingTime/60,"minutes")
            if sweepingChoreTime >= sweepingTime:
                print("The floors are sweeped.")


       elif self.chore == "Mopping":
            print("Set to Mopping:")
            mopFloorNumber = int(input("How many floors would you like to be mopped? "))
            moppingTime = mopFloorNumber*1800
            moppingChoreTime = time.time()
            print("The floors will be completly mopped in", moppingTime/60,"minutes")
            if moppingChoreTime >= moppingTime:
                print("The floors are mopped.")

       elif self.chore == "Folding_Clothes":
            print("Set to Folding_Clothes:")
            clothesNumber = int(input("How many clothes would you like to be folded? "))
            foldingTime = clothesNumber*60 
            clothesChoreTime = time.time()
            print("The clothes will be completly folded in", foldingTime/60,"minute/s")
            if clothesChoreTime >= foldingTime:
                print("The clothes are folded.")

john = ChoreOperator("Dish_Washing")
john.executeChores()
