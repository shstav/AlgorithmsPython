"""
Solution to Google Code Jam's 'The Repeater':
    https://code.google.com/codejam/contest/2994486/dashboard
"""


def the_repeater_solution(input_strings):
  if can_be_solved(input_strings):
    sequence_vectors = [sequence_vector(s) for s in input_strings]
    min_moves = 0
    for letter_sequence_lengths in map(list, zip(*sequence_vectors)):
      sequence_median_length = get_median(letter_sequence_lengths)
      moves_vector = [abs(sequence_median_length - sequence_length)
          for sequence_length in letter_sequence_lengths]
      min_moves += sum(moves_vector)
    return min_moves
  else:
    return "Fegla Won"


def can_be_solved(input_strings):
    normalized_strings = [normalized_string(s) for s in input_strings]
    return len(set(normalized_strings)) == 1


"""
Replaces each sequence in the string with a single letter:
    aaabbcccc => 'abc'
    mmmmaaggk => 'magk'
"""
def normalized_string(input_string):
  result = ""
  prev_char = ""
  for char in input_string:
    if char != prev_char:
      result += str(char)
    prev_char = char
  return result


"""
Replaces each sequence in the string with a single letter:
    aaabbcccc => [3, 2, 4]
    mmmmaaggk => [3, 2, 2, 1]
"""
def sequence_vector(input_string):
  result = []
  prev_char = input_string[0]
  curr_char_count = 0
  for char in input_string:
    if char != prev_char:
      result.append(curr_char_count)
      curr_char_count = 1
    else:
      curr_char_count += 1
    prev_char = char
  result.append(curr_char_count)
  return result


def get_median(input_list):
  middle_index = len(input_list) / 2
  return sorted(input_list)[middle_index]


