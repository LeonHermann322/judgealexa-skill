from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder


import os
import time

class Judgealexa(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.scoreFile = "/home/leonhermann/.config/mycroft/skills/Judgealexa/scoreFile.txt"
        if not os.path.exists(self.scoreFile):
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
        points = self.getScore()
        points = points - 5
        self.setScore(points)
        self.log.info("Insult recognized!")
        self.speak(f"Are you insulting me?")

def create_skill():
    return Judgealexa()

