# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:22:57 2020

@author: wwwds
"""


from pygame import mixer
file='Hoyna_Hoyna_(From_Gang_Leader).mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()