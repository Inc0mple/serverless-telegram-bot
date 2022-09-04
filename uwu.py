import re
from random import randint
# import pandas as pd

random_message = ['*Clears throat*', '*sweating  profusely*', '*Looks down at the ground, twirling thumbs*', '*wipes sweat off brow*', '*wipes away tears*', '*stands taller*', '*boyfriend walks into room*', '*Looks down nervously*', '*Stammers at first as I try to confess my feelings*', '*looks away shvly*', '*Looks away*', '* stands up straight*', '*nuzzles*', '*o4  *', '* OwO Do you like them? *', '*UwU*', '*pounces on foreign affairs*', '*glomps unemployment rate, my tail swishing*', '*Notices the national deficit*', '*cries*', '*pouts more and snuggles up to you*', '*  He doesn’t need to knowwww *', '*Gets close to your face*', '*has massive diarrhea*', '*nuzzles*', '*o4  *', '* OwO Do you like them? *', '*UwU*', '*takes of sunglasses*', '*pulls out a couple of hundred dollar bills*', '*grabs your waist*', '*-*', '*smiles at the ground*', '*tickles your feet from the bottom of the bed*', '*palms are sweaty*', '*knees weak*', '*arms are heavy*', '*theres vomit on my sweater already*', "*mom's spaghetti*", '*UwU*', '*tips fedora*', '*  Me *', '*UwU*', '*giggles*', '*blushes and looks down shyly*', '*waddles up to you*', '*blushes beet red*', '*looks away in embarrassment*', '*blank stare*', '*waves paw*', '*reveals tail*', '*extends hand*',
                  '*gives shy look*', '*sticks out tongue*', '*thinks in  my head of plan*', '*grins*', '*wags tail*', '*giggles*', '*frowns*', '*cat ears twitch*', '*looks down*', '*tears up*', '*nods*', '*excessively starting to sweat*', '*struggles*', '*UwU*', '*owo*', '*UwU*', '*hugs*', '*eyes pop out Oops Oh noo  *', '*UwU*', '*hats off*', '*bows down*', '*cringes*', '*smiles shyly*', '*UwU*', '*Starts crying*', '*boop*', '*hugs you*', '*owo*', '* "will you marry me" *', '*owo*', '*UwU*', '*blushes*', '* UWAgh! *', '*owo*', '*UwU*', '*UwU*', '*UwU*', '*owo*', '* a *', '*_*', '*smiles*', '*smiles*', '*reveals my secret*', '*thinks*', '*thinks*', '*blushes*', '*pouts*', '*Giggles evilly*', '*stutters profusely*', '*wipes forehead*', '*stutters profusely*', '*wipes forehead*', '*stops*', '*smiles bright*', '*hugs*', '*runs off dancing*', '*gives a rose *', '*offers a hand *', '*clears throat*', '*smiles longingly*', '*shifts closer*', '*gains confidence*', '*crosses arms angrily*', '*gets nervous*', '*hides*', '*smiles slyly*', '*holds you tighter*', '*owo*', '*glubs sadly*', '*goe2 two sleep*', '*growls angrily and raises tail in caution*', '*glomps and nuzzles*', '*curls up in ur lap*', '*curls on top of ur head*', '*dislocates lower jaw*', '*eats U alive*']
kaomojiJoy = [" (* ^ ω ^)", " (o^▽^o)", " (≧◡≦)",
              " ☆⌒ヽ(*\"､^*)chu", " ( ˘⌣˘)♡(˘⌣˘ )", " xD"]
kaomojiEmbarassed = [" (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)..", " (*^.^*)..,",
                     "..,", ",,,", "... ", ".. ", " mmm..", "O.o"]
kaomojiConfuse = [" (o_O)?", " (°ロ°) !?", " (ーー;)?", " owo?"]
kaomojiSparkles = [" *:･ﾟ✧*:･ﾟ✧ ", " ☆*:・ﾟ ", "〜☆ ", " uguu.., ", "-.-"]
kaomojiCombined = kaomojiJoy + kaomojiEmbarassed + kaomojiConfuse + kaomojiSparkles


def uwuinate(textInput):
  if (not textInput):
    "Hey silly willy, type something first before trying to uwuinate you...baka!"
  textInput = textInput.lower()
  textArr = textInput.split(' ')
  newArr = [uwuWord(text) for text in textArr]
  random = randint(0, len(random_message) - 1)
  random2 = randint(0, len(kaomojiCombined) - 1)
  final = "".join(newArr) + \
      random_message[random] + " " + kaomojiCombined[random2]
  return final


def uwuWord(word):
  uwu = ""

  lastChar = word[len(word) - 1]
  end = ""
  random = 0
  if (lastChar == '.' or lastChar == '?' or lastChar == '!' or lastChar == ','):
    word = word[:-1]

    end = lastChar
    if (end == '.'):
      random = randint(0, 2)
      if (random == 0):
        random = randint(0, len(kaomojiJoy) - 1)
        end = kaomojiJoy[random]
      else:
        random = randint(0, len(random_message) - 1)
        end = random_message[random]
    elif (end == '?'):
      random = randint(0, 1)
      if (random == 0):
        random = randint(0, len(kaomojiConfuse) - 1)
        end = kaomojiConfuse[random]

    elif (end == '!'):
      random = randint(0, 1)
      if (random == 0):
        random = randint(0, len(kaomojiJoy) - 1)
        end = kaomojiJoy[random]

    elif (end == ','):
      random = randint(0, 2)
      if (random == 0):
        random = randint(0, len(kaomojiEmbarassed) - 1)
        end = kaomojiEmbarassed[random]

    random = randint(0, 3)
    if (random == 0):
      random = randint(0, len(kaomojiSparkles) - 1)
      end = kaomojiSparkles[random]

  if (word.find('l') > -1):
    if (word[-2:] == "le" or word[-2:] == "ll"):
      uwu += word[0: -2].replace("l", 'w').replace("r",
                                                   'w') + word[-2:] + end + ' '

    elif (word[-3:] == "les" or word[-3:] == "lls"):
      uwu += word[0: -3].replace("l", 'w').replace("r",
                                                   'w') + word[-3:] + end + ' '

    else:
      uwu += word.replace("l", 'w').replace("r", 'w') + end + ' '

  elif (word.find('r') > -1):
    if (word[-2:] == "er" or word[-2:] == "re"):
      uwu += word[0: -2].replace("r", 'w') + word[-2:] + end + ' '

    elif (word[-3:] == "ers" or word[-3:] == "res"):
      uwu += word[0: -3].replace("r", 'w') + word[-3:] + end + ' '

    else:
      uwu += word.replace("r", 'w') + end + ' '

  elif word == "my":
      word = "mwy"
      uwu += word + end + ' '
  elif word == "to":
      word = "tuwu"
      uwu += word + end + ' '
  elif word == "had":
      word = "hawd"
      uwu += word + end + ' '
  elif word == "you":
      word = "yuw"
      uwu += word + end + ' '
  elif word == "go":
      word = "gow"
      uwu += word + end + ' '
  elif word == "and":
      word = "awnd"
      uwu += word + end + ' '
  elif word == "have":
      word = "haw"
      uwu += word + end + ' '

  else:
    word = word.replace("ll", "w").replace("r", "w").replace(
        "l", "w").replace("th", "d").replace("fu", "fwu")
    uwu += word + end + ' '
  uwu = uwu.replace("you're", "ur")
  uwu = uwu.replace("youre", "ur")
  uwu = uwu.replace("fuck", "fwickk")
  uwu = uwu.replace("shit", "poopoo")
  uwu = uwu.replace("bitch", "meanie")
  uwu = uwu.replace("asshole", "b-butthole")
  uwu = uwu.replace("dick", "peenie")
  uwu = uwu.replace("penis", "peenie")
  uwu = re.sub(r"/\bcum\b/g", "cummies", uwu)
  uwu = re.sub(r"/\bsemen\b/g", " cummies ", uwu)
  uwu = re.sub(r"/\bass\b/g", " boi pussy ", uwu)
  uwu = re.sub(r"/\bdad\b/g", "daddy", uwu)
  uwu = re.sub(r"/\bfather\b/g", "daddy", uwu)
  if (len(uwu) > 2 and uwu[0].isalpha()):
    # print("hi")
    random = randint(0, 4)
    if (random == 0):
      uwu = uwu[0] + '-' + uwu

  return uwu
