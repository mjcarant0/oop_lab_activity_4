from tv import TV # import tv class
    
def main():
    tv1 = TV() # tv no. 1
    tv2 = TV() # tv no. 2
        
    tv1.turnOn() # turn on tv1
    tv1.setChannel(30) # setting the channel
    tv1.setVolume(3) # setting the volume level
    
    tv2.turnOn() # turn on tv2
    tv2.setChannel(3) # setting the channel
    tv2.setVolume(2) # setting the volume level

    # print each tv's info
    print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
    print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")
    
if __name__ == "__main__": # ensures it's working
    main()