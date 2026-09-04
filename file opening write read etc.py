file = open("greetings.txt", "w")
file.write("Hello!\nWelcome to Python.\nKeep Learning!")
file.close()

file = open("story.txt", "r")
story = file.read()
print(story)
file.close()
