def find_duplicates(files):
    # init data structures
    buffer = {}
    duplicates = []
    # looping through files
    for current_file in files:
        # add to store new element
        if current_file not in buffer:
            buffer[current_file] = current_file.time
        # compare saved file with similar file
        else:
            # identify duplicate
            if buffer[current_file].time < current_file.time:
                duplicate = current_file
            else:
                duplicate = buffer[current_file]

            # save duplicate
            duplicates.append(duplicate)

    # collected duplicates
    return duplicates
