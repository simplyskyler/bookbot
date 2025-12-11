import sys
from stats import word_count, number_of, sort_dct

def main():
	print("Usage: python3 main.py <path_to_book>")
	#sys.exit(1)
	book_path = sys.argv[1]
	text = get_book(book_path)
	words = word_count(text)
	num_words = number_of(text)
	sorted_dct = sort_dct(num_words)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {words} total words")
	print("--------- Character Count -------")
	for item in sorted_dct:
		ch = item["char"]
		if ch.isalpha():
			print(f"{ch}: {item['num']}")
	print("============= END ===============")

def get_book(path):
        with open(path) as b:
                return b.read()

main()
