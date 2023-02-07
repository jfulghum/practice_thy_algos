def number_to_words(n):
    words_for_numbers_less_than_20 = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }

    words_for_tens = {
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    if n < 20:
        return words_for_numbers_less_than_20[n]
    elif n < 100:
        return words_for_tens[n // 10 * 10] + ('' if n % 10 == 0 else ' ' + number_to_words(n % 10))
    elif n < 1000:
        return number_to_words(n // 100) + ' hundred' + ('' if n % 100 == 0 else ' ' + number_to_words(n % 100))
    elif n < 1000000:
        return number_to_words(n // 1000) + ' thousand' + ('' if n % 1000 == 0 else ' ' + number_to_words(n % 1000))
    else:
        return 'Number too large'
      
print(number_to_words(20))      
print(number_to_words(21))
