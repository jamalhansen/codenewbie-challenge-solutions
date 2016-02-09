import re


from madness.prompt import Prompt

def clean_prompt(prompt):
    return re.sub('[{}]', '', prompt).strip()

class Madness:
    def __init__(self):
        self.story = None

    def get_prompts(self):
        blanks, self.pieces = self.split_story()
        self.prompts = [Prompt(clean_prompt(blank)) for blank in blanks]
        return self.prompts

    def split_story(self):
        split = re.split("({[^}]+})", self.story)
        story = []
        prompt = []

        for item in split:
            if item[0] == "{":
                prompt.append(item)
            else:
                story.append(item)

        return (prompt, story)

    def ensue_hilarity(self):
        completed = ""
        for i, piece in enumerate(self.pieces):
            completed += piece
            completed += self._get_prompt(i)

        return completed

    def _get_prompt(self, index):
        if len(self.prompts) > index:
            return self.prompts[index].value
        else:
            return ""
