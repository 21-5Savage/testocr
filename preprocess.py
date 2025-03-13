import converter
import os
import numpy as np



#binary dursleliig matrix-d hadgalna
def read_binary(file_path):
    binary_matrix = np.loadtxt(file_path, dtype=int)  
    return binary_matrix

def splitter(file_path):
    
    matrix = read_binary(file_path)
    
    #loop init stuff
    num_cols = len(matrix[0])  
    
    cont = 0
    first = 0
    last = 0

    #minii test case 17n char-tai uchraas range(1,18)
    #ireeduid heden char baigaagaa uuro medej oldog bolgoh heregtei
    for i in range(1, 18):
        
        
        '''
        logic
        0 aguulsan tasaldaagui bagana uudiig 1 char gej uzne
        tasaldval useg duussan gej uzne
        0 aguulsan ehnii bagana = first
        first baganaas tasaldaagui 0 aguulsan baganuudiin suuliin bagana = last

        first - > (single char) -> last
        
        '''
        cont = 0
        for col in range(last + 1, num_cols):  
            for row in range(len(matrix)):  
                if matrix[row][col] == 0 and cont == 0:  
                    cont = col
                    first = col
                elif matrix[row][col] == 0 and cont != 0:
                    if col - 1 == cont:
                        cont = col
                    else:
                        last = cont
                        break
        
        #17 char-aa bugdiig ni index-tei file uudad hadgalna
        file_path = f"split\\{i}.txt"
        with open(file_path, "a") as file:
            #text file hooson bish bol arilgaad shineer bichne
            file.truncate(0)
            
            for row in range(len(matrix)):                          #muruur guih iterator
                    for col in range(first, last + 1):              #baganaar guih iterator
                        file.write(str(matrix[row][col]))
                        file.write(" ")
                    file.write("\n")
        #hooson zai ustgah function
        remove_space(file_path)
            
def remove_space(file_path):
    
    # matrix-d huulj avna
    matrix = read_binary(file_path)  # Read the binary matrix from file

    # hooson bish muruudiig hadgalna
    rows_with_zero = [row for row in matrix if 0 in row]  # hooson bish muruud

    with open(file_path, "a") as file:  
        # umnuh dursleliig ustgana
        file.truncate(0)
        
        # hooson bish zaig huulna
        for row in rows_with_zero:                         
            file.write(" ".join(map(str, row)) + "\n")  

            
def main():
    #see testocr\converter.py 
    converter.converter("example\\test.png", "example\\output.txt")
    
    splitter("example\\output.txt")
if __name__ == "__main__":
    main()
    