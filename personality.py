#This lab creates an artificial personality using matrices and lookup

# Get the mode of interaction from the user
# Params: none
    #return ["reward", "punish", "joke", "threaten"] # Returns: an integer indicating one of reward, punish, joke, or threaten
def getInteraction():
    action = int(input("Enter an action(0-reward, 1-punish, 2-joke, 3-threaten, 9-quit): "))# TODO prompt user to choose an action
    return action # return a corresponding integer

def lookupEmotion(currEmotion, action):# Based on a given emotion and action, determine the next emotional state
#    currEmotion = ["anger", "disgust", "fear", "happiness", "sadness", "surprise"]# currEmotion - a current emotion
    emotionMatrix = [[0, 2, 3, 1, 5, 4],
                     [1, 3, 0, 1, 1, 2],
                     [1, 5, 3, 5, 2, 0],
                     [4, 2, 5, 2, 1, 3]]# TODO do the matrix lookup
    return emotionMatrix[action][currEmotion]# return an integer corresponding to an emotion

def primaryLoop():
    currEmotion = 0
    while True:
        action = getInteraction() #get next interaction
        if action == "9":
            break
        currEmotion = lookupEmotion(currEmotion, action) #lookup new emotion
        showEmotion(currEmotion) #show emotion

def showEmotion(currEmotion):
    response = ["I am angry.", "I am disgusted.", "I am fearful.", "I am happy! :)", "I am sad :(", "I am surprised!"]
    print(response[currEmotion])
#    if currEmotion == 0:
#        print("I am angry.")
#    if currEmotion == 1:
#        print("I am disgusted.")
#    if currEmotion == 2:
#        print("I am fearful.")
#    if currEmotion == 3:
#        print("I am happy! :)")
#    if currEmotion == 4:          
#        print("I am sad :(")
#    if currEmotion == 5:
#        print("I am surprised!")
                    

def main():
#    showEmotion()
    primaryLoop()

main()
    
