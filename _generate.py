#!/usr/bin/env python
# generate index.md file (write to stdout)

import os
from typing import List

frontmatter = '''
Magic: The Gathering Comprehensive Rules

These rules are effective as of September 24, 2021.

Introduction

This document is the ultimate authority for Magic: The Gathering® competitive game play. It consists of a series of numbered rules followed by a glossary. Many of the numbered rules are divided into subrules, and each separate rule and subrule of the game has its own number. (Note that subrules skip the letters “l” and “o” due to potential confusion with the numbers “1” and “0”; subrule 704.5k is followed by 704.5m, then 704.5n, then 704.5p, for example.)

Changes may have been made to this document since its publication. You can download the most recent version from the Magic rules website at Magic.Wizards.com/Rules. If you have questions, you can get the answers from us at Support.Wizards.com.

Contents

1. Game Concepts
100. General
101. The Magic Golden Rules
102. Players
103. Starting the Game
104. Ending the Game
105. Colors
106. Mana
107. Numbers and Symbols
108. Cards
109. Objects
110. Permanents
111. Tokens
112. Spells
113. Abilities
114. Emblems
115. Targets
116. Special Actions
117. Timing and Priority
118. Costs
119. Life
120. Damage
121. Drawing a Card
122. Counters

2. Parts of a Card
200. General
201. Name
202. Mana Cost and Color
203. Illustration
204. Color Indicator
205. Type Line
206. Expansion Symbol
207. Text Box
208. Power/Toughness
209. Loyalty
210. Hand Modifier
211. Life Modifier
212. Information Below the Text Box

3. Card Types
300. General
301. Artifacts
302. Creatures
303. Enchantments
304. Instants
305. Lands
306. Planeswalkers
307. Sorceries
308. Tribals
309. Dungeons
310. Planes
311. Phenomena
312. Vanguards
313. Schemes
314. Conspiracies

4. Zones
400. General
401. Library
402. Hand
403. Battlefield
404. Graveyard
405. Stack
406. Exile
407. Ante
408. Command

5. Turn Structure
500. General
501. Beginning Phase
502. Untap Step
503. Upkeep Step
504. Draw Step
505. Main Phase
506. Combat Phase
507. Beginning of Combat Step
508. Declare Attackers Step
509. Declare Blockers Step
510. Combat Damage Step
511. End of Combat Step
512. Ending Phase
513. End Step
514. Cleanup Step

6. Spells, Abilities, and Effects
600. General
601. Casting Spells
602. Activating Activated Abilities
603. Handling Triggered Abilities
604. Handling Static Abilities
605. Mana Abilities
606. Loyalty Abilities
607. Linked Abilities
608. Resolving Spells and Abilities
609. Effects
610. One-Shot Effects
611. Continuous Effects
612. Text-Changing Effects
613. Interaction of Continuous Effects
614. Replacement Effects
615. Prevention Effects
616. Interaction of Replacement and/or Prevention Effects

7. Additional Rules
700. General
701. Keyword Actions
702. Keyword Abilities
703. Turn-Based Actions
704. State-Based Actions
705. Flipping a Coin
706. Rolling a Die
707. Copying Objects
708. Face-Down Spells and Permanents
709. Split Cards
710. Flip Cards
711. Leveler Cards
712. Double-Faced Cards
713. Meld Cards
714. Substitute Cards
715. Saga Cards
716. Adventurer Cards
717. Class Cards
718. Controlling Another Player
719. Ending Turns and Phases
720. The Monarch
721. Restarting the Game
722. Subgames
723. Merging with Permanents
724. Day and Night
725. Taking Shortcuts
726. Handling Illegal Actions

8. Multiplayer Rules
800. General
801. Limited Range of Influence Option
802. Attack Multiple Players Option
803. Attack Left and Attack Right Options
804. Deploy Creatures Option
805. Shared Team Turns Option
806. Free-for-All Variant
807. Grand Melee Variant
808. Team vs. Team Variant
809. Emperor Variant
810. Two-Headed Giant Variant
811. Alternating Teams Variant

9. Casual Variants
900. General
901. Planechase
902. Vanguard
903. Commander
904. Archenemy
905. Conspiracy Draft

Glossary

Credits
'''.strip()
frontmatter_lines = frontmatter.split('\n')
frontmatter_len = len(frontmatter_lines)
frontmatter_header = '''
# Magic: The Gathering Comprehensive Rules

These rules are effective as of September 24, 2021.

## Introduction

This document is the ultimate authority for Magic: The Gathering® competitive game play. It consists of a series of numbered rules followed by a glossary. Many of the numbered rules are divided into subrules, and each separate rule and subrule of the game has its own number. (Note that subrules skip the letters “l” and “o” due to potential confusion with the numbers “1” and “0”; subrule 704.5k is followed by 704.5m, then 704.5n, then 704.5p, for example.)

Changes may have been made to this document since its publication. You can download the most recent version from the Magic rules website at Magic.Wizards.com/Rules. If you have questions, you can get the answers from us at Support.Wizards.com.

### Contents

#### 1. Game Concepts

##### 100. General
##### 101. The Magic Golden Rules
##### 102. Players
##### 103. Starting the Game
##### 104. Ending the Game
##### 105. Colors
##### 106. Mana
##### 107. Numbers and Symbols
##### 108. Cards
##### 109. Objects
##### 110. Permanents
##### 111. Tokens
##### 112. Spells
##### 113. Abilities
##### 114. Emblems
##### 115. Targets
##### 116. Special Actions
##### 117. Timing and Priority
##### 118. Costs
##### 119. Life
##### 120. Damage
##### 121. Drawing a Card
##### 122. Counters

#### 2. Parts of a Card
##### 200. General
##### 201. Name
##### 202. Mana Cost and Color
##### 203. Illustration
##### 204. Color Indicator
##### 205. Type Line
##### 206. Expansion Symbol
##### 207. Text Box
##### 208. Power/Toughness
##### 209. Loyalty
##### 210. Hand Modifier
##### 211. Life Modifier
##### 212. Information Below the Text Box

#### 3. Card Types
##### 300. General
##### 301. Artifacts
##### 302. Creatures
##### 303. Enchantments
##### 304. Instants
##### 305. Lands
##### 306. Planeswalkers
##### 307. Sorceries
##### 308. Tribals
##### 309. Dungeons
##### 310. Planes
##### 311. Phenomena
##### 312. Vanguards
##### 313. Schemes
##### 314. Conspiracies

4. Zones
400. General
401. Library
402. Hand
403. Battlefield
404. Graveyard
405. Stack
406. Exile
407. Ante
408. Command

5. Turn Structure
500. General
501. Beginning Phase
502. Untap Step
503. Upkeep Step
504. Draw Step
505. Main Phase
506. Combat Phase
507. Beginning of Combat Step
508. Declare Attackers Step
509. Declare Blockers Step
510. Combat Damage Step
511. End of Combat Step
512. Ending Phase
513. End Step
514. Cleanup Step

6. Spells, Abilities, and Effects
600. General
601. Casting Spells
602. Activating Activated Abilities
603. Handling Triggered Abilities
604. Handling Static Abilities
605. Mana Abilities
606. Loyalty Abilities
607. Linked Abilities
608. Resolving Spells and Abilities
609. Effects
610. One-Shot Effects
611. Continuous Effects
612. Text-Changing Effects
613. Interaction of Continuous Effects
614. Replacement Effects
615. Prevention Effects
616. Interaction of Replacement and/or Prevention Effects

7. Additional Rules
700. General
701. Keyword Actions
702. Keyword Abilities
703. Turn-Based Actions
704. State-Based Actions
705. Flipping a Coin
706. Rolling a Die
707. Copying Objects
708. Face-Down Spells and Permanents
709. Split Cards
710. Flip Cards
711. Leveler Cards
712. Double-Faced Cards
713. Meld Cards
714. Substitute Cards
715. Saga Cards
716. Adventurer Cards
717. Class Cards
718. Controlling Another Player
719. Ending Turns and Phases
720. The Monarch
721. Restarting the Game
722. Subgames
723. Merging with Permanents
724. Day and Night
725. Taking Shortcuts
726. Handling Illegal Actions

8. Multiplayer Rules
800. General
801. Limited Range of Influence Option
802. Attack Multiple Players Option
803. Attack Left and Attack Right Options
804. Deploy Creatures Option
805. Shared Team Turns Option
806. Free-for-All Variant
807. Grand Melee Variant
808. Team vs. Team Variant
809. Emperor Variant
810. Two-Headed Giant Variant
811. Alternating Teams Variant

9. Casual Variants
900. General
901. Planechase
902. Vanguard
903. Commander
904. Archenemy
905. Conspiracy Draft

Glossary

Credits
'''.strip()

def process_frontmatter(rules: List[str]) -> str:
    assert rules[:frontmatter_len] == frontmatter_lines, rules[:10]
    rules = rules[frontmatter_len:]
    return frontmatter_header + '\n\n'


def main(rules: List[str]) -> str:
    result = process_frontmatter(rules)
    result += f'Rules have {len(rules)} lines.\n'
    result += f'First line {repr(rules[0])}\n'
    result += f'Second line {repr(rules[1])}\n'
    result += f'Third line {repr(rules[2])}\n'
    return result


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), '_rules.txt')) as f:
        rules = f.read().split('\n')
    result = main(rules)
    with open(os.path.join(os.path.dirname(__file__), 'index.md'), 'w') as f:
        f.write(result)