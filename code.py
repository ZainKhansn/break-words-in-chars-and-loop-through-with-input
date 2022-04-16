#splits word into letters
def split(word):
    return [char for char in word]

# Word used
fire_camp = "fire_camp"
word = fire_camp
#loops as many times the word is long
for letter in fire_camp:
  letter = str(letter)
  let = input("Press " + letter + "!: ")
  if let == letter:
    continue
  else:
    quit()
