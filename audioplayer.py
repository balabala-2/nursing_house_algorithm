# -*- coding: utf-8 -*-
'''
audio player
'''

# import library
from subprocess import call
import pygame

# play audio
def play_audio(audio_name):
    try:
        pygame.mixer.init()
        print(audio_name)
        pygame.mixer.music.load(audio_name)
        pygame.mixer.music.play(1)
        while pygame.mixer.music.get_busy():  # 在音频播放为完成之前不退出程序
            pass

    except KeyboardInterrupt as e:
        print(e)
    finally:
        pass

if __name__ == '__main__':
    play_audio('./audios/smile.mp3')
    