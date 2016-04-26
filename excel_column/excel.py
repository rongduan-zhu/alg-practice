#!/usr/bin/env python

def main():
  char_index = dict(enumerate([c for c in xrange(ord('A'), ord('Z') + 1)]))

  assert letter_int('A') == 1
  assert letter_int('CV') == 100
  assert letter_int('RT') == 488
  assert letter_int('ADM') == 793
  assert letter_int('Z') == 26
  assert letter_int('ZZ') == 702
  assert letter_int('AZ') == 52
  assert letter_int('ZA') == 677

  assert int_letter(1) == 'A'
  assert int_letter(100) == 'CV'
  assert int_letter(488) == 'RT'
  assert int_letter(793) == 'ADM'
  assert int_letter(26) == 'Z'
  assert int_letter(702) == 'ZZ'
  assert int_letter(52) == 'AZ'
  assert int_letter(677) == 'ZA'

def letter_int(sequence):
  num = 0
  power = 0

  for letter in sequence[::-1]:
    num += (ord(letter) - ord('A') + 1) * 26 ** power
    power += 1

  return num

def int_letter(num):
  sequence = ''

  while num > 0:
    if num % 26 != 0:
      sequence = chr(num % 26 + ord('A') - 1) + sequence
    else:
      sequence = 'Z' + sequence
      num -= 1

    num /= 26

  return sequence

if __name__ == '__main__':
  main()
