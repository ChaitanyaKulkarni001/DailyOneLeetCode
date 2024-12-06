   
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

res = []
current_line = []
current_length = 0

# Step 1: Accumulate words into lines.
for word in words:
    if current_length + len(current_line) + len(word) > maxWidth:
        res.append(current_line)
        current_line = []
        current_length = 0
    current_line.append(word)
    current_length += len(word)

# Append the last line.
if current_line:
    res.append(current_line)

# Step 2: Justify lines.
output = []
for i, line in enumerate(res):
    if i == len(res) - 1:  # Last line (left-justified)
        output.append(" ".join(line).ljust(maxWidth))
    else:
        total_spaces = maxWidth - sum(len(word) for word in line)
        num_gaps = len(line) - 1
        if num_gaps == 0:  # Single word in line
            output.append(line[0].ljust(maxWidth))
        else:
            # Distribute spaces
            space_between = total_spaces // num_gaps
            extra_spaces = total_spaces % num_gaps
            for j in range(extra_spaces):
                line[j] += " "  # Add extra space to leftmost gaps
            output.append((" " * space_between).join(line))

# Print the result.
for line in output:
    print(f'"{line}"')
