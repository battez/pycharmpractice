# https://www.codewars.com/kata/59cf0ba5d751dffef300001f/train/python
#
# note there actually is a python method "count" that returns no times it exists
def vertical_histogram_of(s):

    # this will store the distribution and let us update even if missing key
    from collections import defaultdict
    dd_counts = defaultdict(int)

    # convert the string into its ascii values to make checking simple
    ascii_vals = map(ord, list(s))

    for val in ascii_vals:
        if(val >= 65) and (val <=90):
            dd_counts[val] += 1

    # the string we will return
    output = ""
    if not dd_counts:
        return output

    # ensure keys are sorted alphabetically: (do not need this in python 3.6 up really)
    dd_counts = dict(sorted(dd_counts.items()))
    last_key = list(dd_counts)[-1]

    # output as the spec. requires
    unit = "*"
    space = ' '

    # output each row going downward for a grid of height = maximum count
    height = max(dd_counts.values())
    for row in range(height, 0 , -1):
        row_output = ""

        for key, count in dd_counts.items():
            if (row - count) > 0:
                row_output += space
            else:
                row_output += unit

            # need to add a space between columns according to instructions:
            if key != last_key:
                row_output += space

        # need to trim right hand whitespace according to the Codewars tests :(
        output += (row_output.rstrip() + "\n")

    # finally print the row of keys after converting to letter again
    output += " ".join(map (chr, dd_counts.keys() ))
    return output

# simple test
print(vertical_histogram_of("AA@@ABBC"))










