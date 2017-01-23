def convert_to_roman(n):
    if not isinstance(n, int):
        return 'Please enter number'
    if n < 1 or n > 3999:
        return 'number out of range (must be between 1 and 4000)'
        
    numerals = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    
    if n in numerals:
        return numerals[n]
        
    length = len(str(n))
    roman_num = ''
    for i in str(n):
        if length == 0:
            break
        dig_num = pow(10, length - 1)
        if int(i) in numerals:
            roman_num += numerals[dig_num * int(i)]
        elif int(i) < 4:
            roman_num += numerals[dig_num] * int(i)
        elif (int(i) == 4) or (int(i) == 9):
            roman_num += numerals[dig_num] + numerals[dig_num * (int(i) + 1)]
        elif int(i) > 5:
            roman_num += numerals[dig_num * 5] + (numerals[dig_num] * (int(i) - 5))
        length -= 1
    
    return roman_num
    
    
if __name__ == '__main__':
    assert convert_to_roman(34) == 'XXXIV', '34'
    assert convert_to_roman(156) == 'CLVI', '156'
    assert convert_to_roman(675) == 'DCLXXV', '675'
    assert convert_to_roman(3999) == 'MMMCMXCIX', '3999'
