import re
import string, random
# break ceaser cipher with sequency analysis
original_sentence = input(">>: ")
# the lowercase version of the original sentence
original_sentence_lowercase = original_sentence.lower()

# decryption takes place with lowercase characters
most_common_words_file = "1-1000.txt"

#Note: usa.txt is the shortest textfile available without Welsh, Scottish, etc. accents, containing only american english words and special abbreviations
all_words_file = "US.txt"

def remove_non_letters(sentence):
    STR = string.ascii_letters + " "
    for chr in sentence:
        if chr not in STR:
            sentence = sentence.replace(chr, "")
        else: pass

    return sentence.strip()


def encrypt(sentence, ascii_lower):
    charlist = []
    for char in sentence:
        if char not in charlist and char in ascii_lower:
            charlist.append(char)
        else: pass

    random_sample = random.sample(ascii_lower, k=len(charlist))
    for i in charlist:
        sentence = sentence.replace(i, random_sample[charlist.index(i)].upper())

    return sentence.lower()

#this function checks if a word's structure matches another word's structure such as: 'the' and 'abc' or 'qwr', etc.: this function will be used for finding the right words for substitution
def word_identity(word):
    id = []
    w_id = ""

    # part 1
    for char in word:
        if char not in w_id:
            w_id += char
        else:
            pass
    id.append(len(w_id))

    # part 2
    enumerate_results = []
    for result in enumerate(list(word)):
        enumerate_results.append(result)

    for char in w_id:
        container = []
        for r in enumerate_results:
            if char in r:
                container.append(r[0])
            else:
                pass
        id.append(container)

    return id  # 'the', id = [3, [0], [1], [2]], which means: 3 different characters, at indices 0,1,2

def match(word, match):
    if len(match) == len(word):
        if word_identity(match) == word_identity(word):
            return True
        else:
            return False
    else:
        return False

# update the sentence by substitution
def update_sentence(target, match, sentence):
    for char in sentence:
        if char != char.upper() and char in match:
            sentence = sentence.replace(char, target[match.index(char)].upper())
    return sentence

def generate_pattern(target):
    # generate the pattern from the target by using the re module
    final_target = ""
    for chr in target:
        if chr != chr.upper():
            final_target += '[a-z]'
        else:
            final_target += chr.lower()

    return final_target

# Find matching words in the sentence for the target by using: re.match() and word_identity checker function
def match_sample_target(pattern, sample, target):
    if re.match(pattern, sample) and word_identity(target) == word_identity(sample):
        return True
    else:
        return False

# could be done by set(ls) as well
def remove_duplicates(ls):
    for i in ls:
        if ls.count(i) > 1:
            ls.remove(i)
        else:
            continue

    return ls

# we need an algorithm to choose which word is most likely to be predicted the best, with most uppercase characters
def choosing_algorithm(sentence):
    potential_words = []
    for word in sentence.split(" "):
        if word == word.upper():
            pass
            continue
        else:
            for char in word:
                if char == char.upper():
                    potential_words.append(word)

                else:
                    pass

    potential_words = list(set(potential_words))

    # make the correct order
    counter_list = []
    for word in potential_words:
        n = 0
        for char in word:
            if char == char.upper():
                n += 1

            else:
                pass
                continue
        counter_list.append(n)

    if counter_list != [] and potential_words != []:
        upper_maximum = max(counter_list)
        next_word = potential_words[counter_list.index(upper_maximum)]
        return next_word
    else:
        return None

# we need a function to find all words in textfile that match a certain pattern
def find_matches_in_wordlist(textfile, pattern, target):
    all_matches = []
    for word in open(textfile, "r").readlines():
        word = word.replace("\n", "").lower()
        if match_sample_target(pattern, word, target):  # we need pattern and target for checking word identity match
            all_matches.append(word)  # instead of return word --> which would give the first and only one word

        else:
            pass
            continue

    return all_matches

# we are supposed to create a loop, but before: initialize the whole processes by finding the most common word that matches any word from the sentence
def prepare(target, sentence, all_words_file):
    # generate the pattern for the word
    pattern = generate_pattern(target)

    # find the matching words in sentence
    matching_words = []
    for word in sentence.split(" "):
        if match_sample_target(pattern, word, target):
            matching_words.append(word)
        else:
            continue

    # omit duplications
    matching_words = remove_duplicates(matching_words)
    updated_list = []
    # update the sentence by subtituting the characters of the target word to the matching word, then to the whole sentence

    for word in matching_words:
        updated_sentence = update_sentence(target, word, sentence)
        updated_list.append(updated_sentence)
    # choose the next word to find matches
    '''next_word = choosing_algorithm(updated_sentence)
    # generate pattern again
    pattern2 = generate_pattern(next_word)
    # Note: next_word and pattern2 are both needed for checking word identity in match_sample_target() function
    matching_words_2 = find_matches_in_wordlist(all_words_file, pattern2, next_word)  # in this case all possible words

    updated_sentence = update_sentence(matching_words_2[0], next_word, updated_sentence)'''
    return updated_list

#if the checker function is valid(True)
def complete(sentence):
    next_word = choosing_algorithm(sentence)
    if next_word is not None:
        next_pattern = generate_pattern(next_word)

        matching_words = find_matches_in_wordlist(all_words_file, next_pattern,
                                                  next_word)

        # from this point the tree should be continued
        sentence_list = []

        for i in matching_words:
            sentence_list.append(update_sentence(i, next_word, sentence))

        return sentence_list

    else:
        return None

#if checker function is False, then next_word(choosing_algorithm) returns None, thus a new word should be found
def got_stuck(sentence):
    all_matches = None
    WORD = None

    #the sentence contains only words that have only capital letters or only lowercase letters
    for word in sentence.split(" "):
        if word == word.lower():
            WORD = word
            all_matches = find_matches_in_wordlist(all_words_file, generate_pattern(word), word)
            break

    for match_ in all_matches:
        if any([i.upper() in sentence for i in match_]):
            all_matches.remove(match_)
        else: pass #this part removes all characters that have been used as a replacer before

    sentence_list = []
    # list with all matches done
    if all_matches != None:
        for i in all_matches:
            sentence_list.append(update_sentence(i, WORD, sentence))

        return sentence_list
    else:
        print("Sentence failed.")
        return None #in this case the program fails to find a meaningful word to update and leaves the word unassigned

#valid = True: update sentence, valid = False: no words with both capital and lowercase, thus use got_stuck function
def checker(sentence):
    valid = False
    for word in sentence.split(" "):
        if re.search(r"[^A-Z]", word) and re.search(r"[^a-z]", word): #it means that the word contains not only uppercase and not only lowercase letters: thus it contains both
            valid = True
            break
        else: pass
    return valid


def recursion(sentence):
    if checker(sentence) == True:
        completed = complete(sentence)
        for i in completed:
            if i.upper() != i:
                recursion(i)
            else:
                print(i) #sentence is done
    else: #False
        completed = got_stuck(sentence)
        for i in completed:
            if i.upper() != i:
                recursion(i)
            else:
                print(i) #sentence is done

original_sentence_lowercase = remove_non_letters(original_sentence_lowercase)
print("Original sentence:", original_sentence_lowercase)
encrypted_sentence = encrypt(original_sentence_lowercase, string.ascii_lowercase)
print("Encrypted sentence:", encrypted_sentence)

for target in open(most_common_words_file, "r"):
    print("${0}$".format(target.rstrip()))
    try:
        target = target.rstrip()
        prepared_sentences = prepare(target, encrypted_sentence, all_words_file)
        for sentence in prepared_sentences:
            recursion(sentence)
    except IndexError:
        pass

#dr.