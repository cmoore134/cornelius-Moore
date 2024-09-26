letter_dict = {
  'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
  'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1,
  'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}


stop_word = ['quit', 'q']

def calculate_word_value(word):
 
  word = word.upper()  # Convert word to uppercase for consistency
  total_value = sum(letter_dict.get(letter, 0) for letter in word)
  return total_value

def main():
  while True:
      word = input('>:')
      if word.lower() in stop_word:
          print("Goodbye")
          break
      else:
          word_value = calculate_word_value(word)
          print(f"{word.upper()} is worth {word_value} points.")

if __name__ == "__main__":
  main()