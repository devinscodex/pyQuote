# Initial Program Logic

1. fill folder with quote(s)
2. program will scan folder, adding only excel files to list
3. user selects from list which file(s) to process


# File Processing

1. scan file, report how many rows and sheets in file
2. for each sheet, scan each row looking for "x" in the first column
3. add unmarked rows to one list, marked rows in another

4. from here i'll need to determine if the row is a single line or the top of a group
    if the top of a group, add the entire group of rows to the "marked" list to hide

5. once all sheets are scanned, unhide all unmarked rows and hide all marked rows
6. save file, process next in list until all files are complete



# SCRATCH NOTES 📝

can pandas find which rows are hidden?


