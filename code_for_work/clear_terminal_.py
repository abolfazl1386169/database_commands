# for clear trminal in python you type [print("\033c")]
# for example :
import time 
x = 1
while x <= 10 :
    print(x)
    time.sleep(1)
    print("\033c")
    x += 1
print("is secsessful!")