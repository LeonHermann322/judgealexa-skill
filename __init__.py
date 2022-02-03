from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder


import os
import time

class Judgealexa(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.scoreFile = "./scoreFile.txt"
        if not os.path.exists(self.scoreFile):
            self.log.info("##\t\tscoreFile created")
            self.setScore(1000)

    def getScore(self):
        scoreFile = open(self.scoreFile, "r")
        points = int(scoreFile.read())
        scoreFile.close()
        return points

    def setScore(self, points):
        scoreFile = open(self.scoreFile, "w+")
        scoreFile.write(str(points))
        scoreFile.close()


    @intent_handler(IntentBuilder('insult').require('Insults'))
    def handle_insult(self, message):
        self.log.info("##\t\tinsult recognized")
        points = self.getScore()
        points = points - 5
        self.log.info(f"##\t\tscore: {points + 5} --> {points} ")
        self.setScore(points)
        self.speak(f"Are you insulting me?")

def create_skill():
    return Judgealexa()

