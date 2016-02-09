#!/usr/bin/python3

import sys
from os.path import join
from os import getcwd

from madness.madness import Madness

story = sys.argv[1]
cwd = getcwd()

# Get the story text
story_path = join(cwd, "stories", story)
f = open(story_path, "rb")
text = f.read()
f.close()

# Read story and get prompts
builder = Madness()
builder.story = text.decode()
prompts = builder.get_prompts()

for prompt in prompts:
    prompt.value = input("Enter {0}: ".format(prompt.text))

print("\n------Your Story------\n\n")
print(builder.ensue_hilarity())
