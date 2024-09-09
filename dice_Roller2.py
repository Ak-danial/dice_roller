import random
class dice_roll:
    def __init__(self):       
       print("Welcome1!..")
    
    # def no_of_Roll(self):
    #    a = int(input("Enter how many times you want to roll"))
    #    return a
    def win_sum(self):
       a = int(input("How much you want to win \n"))
       return a
    def turn(self):
       opt =["a","b"]
       a = random.choice(opt)
       return a
    # def roll_dice(self):       
      
    #    print(a)
    #    return a
    def check_winner(self):     
    #    i = 0
      
       win_amount = self.win_sum() 
       turn = "a"
    #    no_of_roll = self.no_of_Roll()
       sum_of_a= 0
       sum_of_b= 0
       while(True):          
            if turn=="a":                
                if sum_of_a>=win_amount:
                    return print("a is winner")
               
                else:
                    n = random.randint(1,6)
                    print(f"A rolls ,{n} ")
                    # no = self.roll_dice()
                    sum_of_a = sum_of_a + n
                    print(f"Sum of a is, {sum_of_a}") 
                    turn = "b"      
            else:
               if sum_of_b >=win_amount:
                   return print("a is winner")
               else:
                     no =  random.randint(1,6)
                     print(f"B rolls ,{no}")
                     sum_of_b = sum_of_b + no
                     print(f"Sum of b is, {sum_of_b}")
                     turn = "a"
            #    i = i+1
                    
                  
k = dice_roll()
k.check_winner()
 