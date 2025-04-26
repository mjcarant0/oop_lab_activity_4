from tv import TV # import tv class
    
def main():
    tv1 = TV() # tv no. 1
    tv2 = TV() # tv no. 2
        
    tv1.turnOn() # turn on tv1
    tv1.setChannel(30) # setting the channel
    
    tv2.turnOn() # turn on tv2
    tv2.setChannel(3) # setting the channel

if __name__ == "__main__": # ensures it's working
    main()