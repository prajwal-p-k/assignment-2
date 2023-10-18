def madlibs():
    noun = input("Choose a noun: ")
    verb = input("Choose a verb: ")
    adjective = input("Choose an adjective: ")
    adverb = input("Choose an adverb: ")
    place = input("Choose a place: ")

    story = f"Once upon a time, in {place}, there was a {adjective} {noun}. " \
            f"It loved to {verb} {adverb}."

    return story

if __name__ == "__main__":
    print(madlibs())
