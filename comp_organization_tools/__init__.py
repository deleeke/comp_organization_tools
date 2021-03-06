# Filename: __init__.py
from __future__ import print_function
import math
version='1.0.0'

hex_bin_dict = { '0' : '0000',
             '1' : '0001',
             '2' : '0010',
             '3' : '0011',
             '4' : '0100',
             '5' : '0101',
             '6' : '0110',
             '7' : '0111',
             '8' : '1000',
             '9' : '1001',
             'A' : '1010',
             'B' : '1011',
             'C' : '1100',
             'D' : '1101',
             'E' : '1110',
             'F' : '1111'}

bin_hex_dict = { '0000' : '0',
                 '0001' : '1',
                 '0010' : '2',
                 '0011' : '3',
                 '0100' : '4',
                 '0101' : '5',
                 '0110' : '6',
                 '0111' : '7',
                 '1000' : '8',
                 '1001' : '9',
                 '1010' : 'A',
                 '1011' : 'B',
                 '1100' : 'C',
                 '1101' : 'D',
                 '1110' : 'E',
                 '1111' : 'F'}


def binToDec(num, verbose=True):
    '''Converts two's complement binary integer to decimal (base ten). 

    Interperets string of 0's and 1's or integer consisting of 0's and 1's as a two's complement integer and converts to base 10.

    Args:
        num    (string or int): Binary number to be converted -- no spaces allowed
    
    Optional Args:
        verbose          (bool): By default, set to true. Prints out all the steps taken.

    Returns:
        integer value of binary string '''

    num_str = str(num)
    if verbose:
        print ('Convert %s to decimal' %num_str)
    result = 0
    isNeg = False
    if num_str[0] == '1':
        if verbose:
            print ("If negative, take two's complement")
        isNeg = True
        num_str = twosComplement(num_str)

    for i in range(1,(len(num_str) +1)):
        result += ((int(num_str[-i]))*2**(i-1))
    #undo two's complement
    if (isNeg):
        result = -result
    return result

def twosComplement(num, verbose=True):
    if verbose:
        print ("Two's complement of %s" %num)
    num_str = str(num)
    return_str1 = ''
    return_str2 = ''
    # flip bits
    for i in range(len(num_str)):
        if (num_str[i] == '0'):
            return_str1 += '1'
        else:
            return_str1 += '0'
    if verbose:
        print ('flipped bits')
        print ("%s --> %s" %(num_str, return_str1))
    # add 1
    overflow = True
    for i in range(1, len(return_str1) + 1):
        if return_str1[-i] == '0':
            index_to_flip = len(return_str1) - i
            print ("Index after which need to flip bits to add one is %s" %index_to_flip)
            overflow = False
            break
        if ((i == len(return_str1)) and overflow):
            print ('overflow')
            print (return_str1)
            return return_str1
    for i in range(len(return_str1)):
        if i < index_to_flip:
            return_str2 += return_str1[i]
        else:
            if (return_str1[i] == '0'):
                return_str2 += '1'
            else:
                return_str2 += '0'
    print ("Two's complement of %s --> %s --> %s" %(num_str, return_str1, return_str2))
    return return_str2


def bitsToEncode(N):
    '''Returns number of bits it takes to encode N possible states'''
    return int(math.ceil(math.log(N,2)))

def decToBin(num, wordsize=0, verbose=True):
    '''Converts base 10 integer to binary.

    Binary representation uses two's complment to signify negative values

    Args:
        num               (int): Number to be converted
    
    Optional Args:
        wordsize          (int): By default, this will size the binary string to whatever will hold the number. If a insufficient wordsize is specified, overflow will occur -- but this is by design.
        verbose          (bool): By default, set to true. Prints out all the steps taken.

    Returns:
        string representing two's complement binary value.
    '''
    if wordsize == 0:
        if num > 0:
            wordsize = int(math.log(num, 2)) +1
        else:
            wordsize = 4
    if verbose:
        print ("Convert decimal %s to binary" %num)
    isNeg = False
    if num < 0:
        num = -num
        isNeg = True
    return_str = ''
    if (isNeg == False):
        return_str += '0'

    for i in range(1, wordsize+1):
        num_decreased = num - (2**(wordsize - i))
        if (0 <= num_decreased <= num):
            return_str += '1'
            num = num_decreased
        else:
            return_str +='0'
    if isNeg:
        return_str = twosComplement(return_str)
    return return_str

def hexToBinary(hex_num, seperator='', verbose=True):
    '''Converts hexadecimal to binary.

    Interperets string of characters from {0 ... 9} and {A ... F} as a hexadecimal number 
    and returns its value in two's complement binary.

    Args:
        hex_str        (string): Hex number to be converted -- no spaces allowed, no leading 0x
    
    Optional Args:
        verbose          (bool): By default, set to true. Prints out all the steps taken.

    Returns:
        string representing two's complement binary value
    '''
    hex_num = str(hex_num)
    return_str = ''
    pretty_str = ''
    for i in range(len(hex_num)):
        pretty_str += hex_bin_dict[hex_num[i]] + " "
        return_str += hex_bin_dict[hex_num[i]] + seperator
    if verbose:    
        print ('hex 0x%s --> %s in binary' %(hex_num, pretty_str))
    return return_str

def hexToDec(hex_num, verbose=True):
    result = binToDec(hexToBinary(hex_num, verbose=verbose), verbose=verbose)
    if verbose:
        print ("hex 0x%s --> %s in decimal" %(hex_num, result))
    return result

def decToHex(dec_int, verbose=True):
    return binToHex(decToBin(dec_int, wordsize=63, verbose=verbose), verbose=verbose)

def binToHex(bin_str, wordsize=64, verbose=True):
    '''Converts binary to hexadecimal.

    Interperets string of 0's and 1's or integer consisting of 0's and 1's as a two's complement integer.

    Args:
        bin_str (string or int): Binary number to be converted -- no spaces allowed
    
    Optional Args:
        wordsize          (int): Number of bits that hexadecimal number will represent. Must be multiple of 4.
        verbose          (bool): By default, set to true. Prints out all the steps taken.

    Returns:
        string representing two's complement hexadecimal value.
    '''
    bin_str = str(bin_str)
   # bin_str = decToBin(binToDec(bin_str, verbose=verbose), wordsize)
    if verbose:
        print ("Convert binary %s to hex" %bin_str)
    hex_num = ''
    i = 0
    while(i+3 <= wordsize):
        nibble = ''
        for k in range(4):
            nibble += bin_str[i+k]
        hex_num += bin_hex_dict[nibble]
        i += 4
    if verbose:
        print ('%s --> 0x%s in hex' %(bin_str, hex_num))
    return hex_num