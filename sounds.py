# Module imports
import pygame

class Sounds:
    # Class Initialization
    def __init__(self) -> None:
        pass
    
    # Code that will load all sounds into memory.
    def store_sounds(self):
        # Sounds
        sound_paddle_hit_one=pygame.mixer.Sound("paddle_hit_one.wav")
        sound_paddle_hit_two = pygame.mixer.Sound("paddle_hit_two.wav")
        sound_score=pygame.mixer.Sound("score.wav")
        
        # Background Music
        pygame.mixer.music.load("follow_me_music.wav")
    
    # Command to play music until further notice.
    def play_music(self):
        pygame.mixer.music.play(-1)

        # Command to set the volume of music. 
        pygame.mixer.music.set_volume(0.7)

    # Command to stop currently played music.
    def stop_music(self):
        pygame.mixer.music.stop()

    # Commands to play certain sounds from memory.
    def play_sound_paddle_hit_one(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound("paddle_hit_one.wav"))

    def play_sound_paddle_hit_two(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound("paddle_hit_two.wav"))

    def play_sound_score(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound("score.wav"))

    # Command that will print off the documentation.
    # The documentation must be printed due to legal reasons.
    def print_documentation(self):
        file=open("Music and Sound Effects Documentation.txt")
        content=file.read()
        print(content)
        file.close()
    def play_sound_score(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound("score.wav"))

    # Command that will print off the documentation.
    # The documentation must be printed due to legal reasons.
    def print_documentation(self):
        file=open("Music and Sound Effects Documentation.txt")
        content=file.read()
        print(content)
        file.close()
