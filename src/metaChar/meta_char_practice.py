
import re

print("QUESTION 1: Extract Phone Number")

text = "My phone number is 123-456-7890"
pattern = r"\b\d{3}-\d{3}-\d{4}\b"

result = re.findall(pattern, text)
print("Phone number:", result)


print("\nQUESTION 2: Extract Email")

text = "My email is abc@gmail.com"
pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

result = re.findall(pattern, text)
print("Email:", result)


print("\nQUESTION 3: Uppercase Words")

text = "Alice and Bob are Good Friends."
pattern = r"\b[A-Z][a-zA-Z]*\b"

result = re.findall(pattern, text)
print("Words:", result)
print("Count:", len(result))


print("\nQUESTION 4: Split Sentence")

sentence = "Hello! How are you doing?"
pattern = r"\b\w+\b"

result = re.findall(pattern, sentence)
print("Words:", result)