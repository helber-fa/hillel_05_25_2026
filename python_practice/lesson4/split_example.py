sent = '"Would you tell me, please, which way I ought to go from here?"'

my_phrases = sent.split("please")
print(my_phrases)
print(type(my_phrases))

print(f"first phrase = {my_phrases[0]}")
print(f"second phrase = {my_phrases[1]}")

print(sent.split(" "))

copy_sent = '"Would you      tell me,   please, which      way I ought    to go from here?"'

space_split = copy_sent.split(" ")
default_split = copy_sent.split()

print(space_split)

# for element in default_split:
#     new_element = f"this element is: {element}"
#     print(new_element)
sentence_to_check = default_split

correct_sentence = True
for element in sentence_to_check:
    if element == "":
        correct_sentence = False

print(f"Sentence correct: {correct_sentence}")

# print(space_split)
# print(default_split)