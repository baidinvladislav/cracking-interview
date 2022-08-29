import os


# their solution
# Time complexity: O(n)
# Space complexity: O(1)
def find_duplicate_files(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]

    # We'll track tuples of (duplicate_file, original_file)
    duplicates = []

    while len(stack) > 0:
        current_path = stack.pop()

        # If it's a directory,
        # put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # If it's a file
        else:
            # Get its contents
            try:
                with open(current_path) as file:
                    file_contents = file.read()
                    print('Can read file!')
            except UnicodeDecodeError as err:
                print(f'Impossible to open this file: {err}')
                continue

            # Get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # If we've seen it before
            if file_contents in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_contents]
                if current_last_edited_time > existing_last_edited_time:
                    # Current file is the dupe!
                    duplicates.append((current_path, existing_path))
                else:
                    # Old file is the dupe!
                    # So delete it
                    duplicates.append((existing_path, current_path))
                    # But also update files_seen_already to have
                    # the new file's info
                    files_seen_already[file_contents] = (current_last_edited_time, current_path)

            # If it's a new file, throw it in files_seen_already
            # and record the path and the last edited time,
            # so we can delete it later if it's a dupe
            else:
                files_seen_already[file_contents] = (current_last_edited_time, current_path)

    return duplicates


find_duplicate_files('/Users/baydin/Documents')
