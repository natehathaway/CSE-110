
from sunau import AUDIO_FILE_ENCODING_MULAW_8


#Inputs
adjective = input("Please input an adjective: ")
animal = input("Please input an animal: ")
verb1 = input("Please input a verb ending in 'ing': ")
exclamation = input("Please input an exclamation: ")
verb2 = input("Please input a verb: ")
verb3 = input("Please input a verb: ")

#Additional inputs
adjective2 = input("Please input an adjective: ")
adjective3 = input("Please input an adjective: ")
animal2 = input("Please input an animal: ")
verb4 = input("Please input a verb ending in 'ing': ")

#Mad Lib
print('The other day, I was really in trouble. It all started when I saw a very ' + adjective + " " + animal + " " + verb1 + ' down the hallway. "' + exclamation.capitalize() + '!"' ' I yelled. But all I could think to do was to ' + verb2 + ' over and over. Miraculously, that caused it to stop, but not before it tried to ' + verb3 + ' right in front of my family. It was such a ' + adjective2 + ' experience. No one would believe me if I told them that there was a very ' + adjective3 + " " + animal2 + " " + verb4 + " at school.")