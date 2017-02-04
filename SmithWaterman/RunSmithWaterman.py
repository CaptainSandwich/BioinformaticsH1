import SmithWaterman
import AlignmentTools

file1 = SmithWaterman.get_file_data("Enter first file name: ")
file2 = SmithWaterman.get_file_data("Enter second file name: ")

file1list = list(file1)
file2list = list(file2)

file1len = len(file1list)
file2len = len(file2list)

matrix = SmithWaterman.create_matrix(file1len, file2len)

AlignmentTools.fill_matrix(file1list, file2list, matrix)

alignment = SmithWaterman.do_alignment(file1list, file2list, matrix)

print(''.join(alignment[0]))
print(''.join(alignment[1]))
print(''.join(alignment[2]))
