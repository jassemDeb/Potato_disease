import split_folders

# Define input and output folders
input_folder = 'PlantVillage'  # Replace this with your input folder name
output_folder = 'dataset'

# Perform the splitting
split_folders.ratio(input_folder, output=output_folder, seed=1337, ratio=(.7, .1, .2))
