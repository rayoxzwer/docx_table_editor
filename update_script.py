from docx import Document
doc = Document('resident.docx')

# Redefine the function to ensure proper timecode editing
def convert_timecode(timecode):
    parts = timecode.split(":")
    minutes = int(parts[1])
    seconds = int(parts[2]) + 1  # Add 1 second
    # Handle carryover from seconds to minutes
    if seconds >= 60:
        minutes += 1
        seconds -= 60
    return f"{minutes:02}:{seconds:02}"

# Flag to start editing after 02:20 IRVING's line
editing_started = False

# Process the paragraphs in the document
for paragraph in doc.paragraphs:
    if not editing_started:
        # Check for the 02:20 IRVING's line as the starting point
        if "02:20" in paragraph.text and "IRVING" in paragraph.text:
            editing_started = True
    else:
        # Process paragraphs with timecodes after the starting point
        words = paragraph.text.split()
        for i, word in enumerate(words):
            if ":" in word and word.count(":") == 3:  # Check for timecode format
                words[i] = convert_timecode(word)
        paragraph.text = " ".join(words)

# Save the modified document again
output_path = 'Updated_Script_v3.docx'
doc.save(output_path)

output_path