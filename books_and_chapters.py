
most_chapters = -1
most_book = ""

with open("books_and_chapters.txt") as books_and_chapters:
    for line in books_and_chapters:
        parts = line.split(":")
        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
        if chapters > most_chapters:
            most_chapters = chapters
            most_book = book


print(f"The book with the most chapters is {most_book}, with {most_chapters} chapters.")
