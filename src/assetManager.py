import pygame, os
from config import *

class AssetManager():
    def __init__(self, path):
        self.__sounds = {}
        self.__imgs = {}
        self.__fonts = {}

        self.__result = []
        self.path = path

    def __scanFolder(self, path, fileformats):
        listdir = os.listdir(path=path)

        for entity in listdir:
            if(os.path.isdir(path + '/' + entity)):
                self.__scanFolder(path + '/' + entity, fileformats)

            if(os.path.isfile(path + '/' + entity)):
                for fileformat in fileformats:
                    if(entity.find(fileformat) > 0):
                        self.__result.append(path + '/' + entity)

    def __loadResources(self, type):
        if(type == 'images'):
            self.__scanFolder(self.path, ['.png'])
        if(type == 'sounds'):
            self.__scanFolder(self.path, ['.mp3', '.MP3'])

    def loadSounds(self):
        InfoLogger.info("LOADING SOUNDS")
        self.__loadResources('sounds')

        for file in self.__result:
            tmp = file.split('/')
            name = tmp[len(tmp) - 1].split('.')[0]
            print(file)
            self.__sounds[name] = pygame.mixer.Sound(file)
            # self.__sounds[name] = file

        self.__result.clear()

        DebugLogger.debug("------ SOUNDS ------")
        for i in self.__sounds:
            DebugLogger.debug(i + ' = ' + str(self.__sounds[i]))

    def loadImages(self):
        InfoLogger.info("LOADING IMAGES")
        self.__loadResources('images')
        
        for file in self.__result:
            tmp = file.split('/')
            name = tmp[len(tmp) - 1].split('.')[0]
            self.__imgs[name] = pygame.image.load(file)

        self.__result.clear()

        DebugLogger.debug("------ IMAGES ------")
        for i in self.__imgs:
            DebugLogger.debug(i + ' = ' + str(self.__imgs[i]))

    def loadFonts(self):
        InfoLogger.info("LOADING FONTS")

        self.__fonts['UI'] = pygame.freetype.Font("media/fonts/BD_Cartoon_Shout.ttf", FONT_SIZE)
        self.__fonts['HUD'] = pygame.freetype.Font("media/fonts/joystixmonospace.ttf", FONT_SIZE)
        self.__fonts['strategy'] = pygame.freetype.Font("media/fonts/kingdomCome.TTF", FONT_SIZE)

        DebugLogger.debug("------ FONTS ------")
        for i in self.__fonts:
            DebugLogger.debug(i + ' = ' + str(self.__fonts[i]))

    def getSound(self, sound):
        return self.__sounds[sound]
    
    def getImage(self, img):
        return self.__imgs[img]
    
    def getFont(self, font):
        return self.__fonts[font]

    def setAllVolumes(self, value):
        for sound in self.__sounds:
            self.__sounds[sound].set_volume(value)

    def setSoundVolume(self, sound, value):
        sound.set_volume(value)