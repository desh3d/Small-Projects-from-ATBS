#JUST SOME NPC TRYING CODE

class npc():
    def __init__(self, types,appear, accent, weapons):
        self.types = types
        self.appear = appear
        self.accent = accent
        self.weapons = weapons

    def __add__(self, other):
        return npc(self.types + other.types, self.appear + other.appear, self.accent + other.accent, self.weapons + other.weapons)
peasent = npc('farmer','fields','scottish','none')
soldier = npc('troop','camp','persian','sword')

newreq = peasent + soldier

print(newreq.types)
print(newreq.appear)
