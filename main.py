# Groan-Off entry: one original one-line dad joke.
# Pure Python standard library only.
# Writes the joke to /output/entry.txt (1-140 chars, single line, UTF-8).
#
# Revision notes: v1 ("staged a protest ... sick of being leafed alone
# all day") was wordy and buried the pun under filler. v2 tightens the
# setup ("went on strike"), uses spoken contractions ("they're tired"),
# and ends the line on the pun itself ("leafed alone") so the groan
# lands as the last word. Candidates rejected: toaster-divorce
# (two competing puns, muddier), trampoline "bounce back" (worn pun),
# dog reality-show (twist but no pun), GPS scenic route (funny but
# long and more anecdote than dad pun).

import os

JOKE = "My houseplants went on strike \u2014 they said they're tired of being leafed alone."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
