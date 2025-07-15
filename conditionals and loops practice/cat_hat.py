def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time \
    for i in range(len(str)):
        x = str.count('cat')
        y = str.count('hat')
        if x == y :
            return True
        elif x == 0 and y == 0:
            return True
        else:
            return False
    
    

        

cat_hat(word)