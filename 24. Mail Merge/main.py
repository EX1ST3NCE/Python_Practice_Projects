with open("Input/Names/invited_names.txt") as names:
    names_list = names.read().split("\n")

    for name in names_list:
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", 'w') as files:
            file_content = open("Input/Letters/starting_letter.txt").read().replace("[name]", name)
            files.write(file_content)

    files.close()
    names.close()
