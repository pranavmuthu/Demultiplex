# Author: <PRANAV MUTHURAMAN> <pmuthura@uoregon.edu>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module


'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
__version__ = "0.4"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning
                            '''

DNA_bases = "ACTG"
RNA_bases = "ACUG"

def convert_phred(letter: str) -> int:
    '''
    This function takes a ASCII value representing the Quality score and converts it to the decimal value - 33 (Phred 33)
    Input: A
    Expected output: 32

    parameter: string score
    return: int decimal_score
    '''
    dec = ord(letter)
    decimal_score = dec - 33

    return decimal_score


def average_qual(qual_line: str) -> float:
    '''
    This function take a quality string and returns the average quality score of that line
    Input: AAAIII
    Expected output: 36

    parameter: string qual_line
    return: float avg_qual
    '''
    len_score = len(qual_line)
    total_score = 0

    for score in qual_line:
            total_score += convert_phred(score)
    avg_qual = total_score/len_score

    return avg_qual

def contain_N(index: str) -> int:
    '''
    This function takes a string of 2 indexes seperated with a '-' and returns the number of Ns it contains
    Input: AACTTGCC-ANCTNGCC
    Expected output: 2

    parameter: string index
    return: int num_ns
    '''
    num_ns = 0
    for char in index:
        if char.upper() == "N":
            num_ns += 1
    
    return num_ns

def if_match(index: str) -> bool:
    '''
    This function takes a string of 2 indexes seperated with a '-' and returns True if they match and False is they are different 
    Input: AACTTGCC-AACTTGCC
    Expected output: True

    parameter: string index
    return: bool match_flag
    '''
    index1 = index[0:7]
    index2 = index[9:16]
    if index1 == index2:
        return True
    else:
        return False

def reverse_comp(index: str) -> str:
    '''
    This function takes a string of 1 index and returns a string of the reverse complement 
    Input: AACTTGCC
    Expected output: GGCAAGTT

    parameter: string index
    return: string rev_comp
    '''
    reverse = index[::-1]
    complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C', 'N': 'N'}
    rc = ''
    for base in reverse:
        rc = str(rc + complements[base])
    
    return rc

    
def validate_base_seq():
    '''docstring'''
    pass


def gc_content():
    '''docstring'''
    pass


def oneline_fasta():
    '''docstring'''
    pass


if __name__ == "__main__":
    # write tests for functions above
    pass