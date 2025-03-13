import numpy as np
import matplotlib.pyplot as plt
import os

#eniig ter chigeer ni gpt hiisen bolohoor bi uuro ch oilgohgui bna

def load_matrix_from_string(matrix_string):
    """Load a matrix from a string with space-separated values."""
    lines = matrix_string.strip().split('\n')
    return np.array([[int(num) for num in line.split()] for line in lines])

def normalize_matrix(matrix):
    """Normalize the matrix to a standard size for comparison."""
    # Resize to a standard size (e.g., 32x32)
    from scipy.ndimage import zoom
    target_size = (32, 32)
    # Calculate zoom factors
    zoom_factors = (target_size[0] / matrix.shape[0], target_size[1] / matrix.shape[1])
    # Resize the matrix
    resized = zoom(matrix, zoom_factors, order=0)  # order=0 for nearest-neighbor interpolation
    return resized

def preprocess_matrix(matrix):
    """Preprocess matrix to handle different formats and orientations."""
    # Ensure binary values
    matrix = (matrix > 0).astype(int)
    
    rows_with_data = np.where(np.any(matrix != 1, axis=1))[0] 
    cols_with_data = np.where(np.any(matrix != 1, axis=0))[0]
    
    if len(rows_with_data) > 0 and len(cols_with_data) > 0:
        min_row, max_row = rows_with_data.min(), rows_with_data.max()
        min_col, max_col = cols_with_data.min(), cols_with_data.max()
        matrix = matrix[min_row:max_row+1, min_col:max_col+1]
    
    return matrix

def compare_matrices(matrix1, matrix2):
    """Compare two matrices to determine if they represent the same letter."""
    # Preprocess matrices
    processed1 = preprocess_matrix(matrix1)
    processed2 = preprocess_matrix(matrix2)
    
    # Normalize to the same size
    norm1 = normalize_matrix(processed1)
    norm2 = normalize_matrix(processed2)
    
    # Calculate similarity
    similarity = np.mean(norm1 == norm2)
    
    # Check if the similarity is above a threshold
    threshold = 0.8  # 80% similarity threshold
    return similarity >= threshold, similarity

def read_matrix_from_file(file_path):
    """Read a matrix from a file."""
    with open(file_path, 'r') as f:
        content = f.read()
    return load_matrix_from_string(content)

def visualize_matrices(matrix1, matrix2, processed1, processed2, norm1, norm2):
    """Visualize the original and processed matrices."""
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    
    axs[0, 0].imshow(matrix1, cmap='binary')
    axs[0, 0].set_title('Original Matrix 1')
    
    axs[0, 1].imshow(processed1, cmap='binary')
    axs[0, 1].set_title('Processed Matrix 1')
    
    axs[0, 2].imshow(norm1, cmap='binary')
    axs[0, 2].set_title('Normalized Matrix 1')
    
    axs[1, 0].imshow(matrix2, cmap='binary')
    axs[1, 0].set_title('Original Matrix 2')
    
    axs[1, 1].imshow(processed2, cmap='binary')
    axs[1, 1].set_title('Processed Matrix 2')
    
    axs[1, 2].imshow(norm2, cmap='binary')
    axs[1, 2].set_title('Normalized Matrix 2')
    
    plt.tight_layout()
    plt.show()

def main():
    
    '''1 useg taaruuldag code '''
    
    # file1_path = "split\\1.txt"
    # file2_path = "alphabet\\binary\\b.txt"
    
    # try:
    #     # Load matrices from files
    #     matrix1 = read_matrix_from_file(file1_path)
    #     matrix2 = read_matrix_from_file(file2_path)
        
    #     # Preprocess matrices
    #     processed1 = preprocess_matrix(matrix1)
    #     processed2 = preprocess_matrix(matrix2)
        
    #     # Normalize to the same size
    #     norm1 = normalize_matrix(processed1)
    #     norm2 = normalize_matrix(processed2)
        
    #     # Compare matrices
    #     is_same, similarity = compare_matrices(matrix1, matrix2)
        
    #     # Print results
    #     print(f"Similarity score: {similarity:.2f}")
    #     if is_same:
    #         print("The matrices represent the same letter")
    #     else:
    #         print("The matrices represent different letters")
        
        # Visualize matrices
        #visualize_matrices(matrix1, matrix2, processed1, processed2, norm1, norm2)
        
    # except Exception as e:
    #     print(f"Error: {e}")
    
    
    '''buh usgiig ni taruulna'''
    
    # bi yag yaj yu bichsenee uuro ch sain oilgohgui baina
    alphabet_folder = "alphabet\\binary"
    text_folder = "split"
    
    guess = []
    for i in range(1,18):
        text_loc = f"{i}.txt"
        matrix_text = read_matrix_from_file(os.path.join(text_folder, text_loc))
        possible_matches = dict()
        for alphabet_loc in os.listdir(alphabet_folder):
            letter, _ = os.path.splitext(alphabet_loc)
            matrix_alphabet = read_matrix_from_file(os.path.join(alphabet_folder, alphabet_loc))
            is_same, similarity = compare_matrices(matrix_text, matrix_alphabet)
            possible_matches[letter] = similarity
        max_key = max(possible_matches, key=possible_matches.get)
        print(max_key, " : ", possible_matches[max_key])
        guess += max_key
    print(guess)
        
# If running this script directly
if __name__ == "__main__":
    main()