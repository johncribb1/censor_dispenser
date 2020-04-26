# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_one)

def find(word_phrase, text):
    working_txt = ''
    if word_phrase in text:
      working_txt = text.replace(word_phrase, '*Censored Information*')
      return working_txt
    else:
        return 'No such instances of ' + word_phrase

#email1_censor = find('learning algorithms', email_one)
#print(email1_censor)


proprietary_terms = ["she",'she', "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def find_ver2(text):
    working_text = text
    for i in proprietary_terms:
        if i in working_text:
            working_text = working_text.replace(i, '*Censored Information*')
    return working_text
    
#email2_censor = find_ver2(email_two)
#print(email2_censor)
#print(email_two)

def find_ver3(text):
    working_text = text
    for i in proprietary_terms:
        if i in working_text:
            working_text = working_text.replace(i, '*Censored Information*')
    return working_text
    
def negative_count(text):
    
    working_text = []
    
    for x in text.split(" "):
        x1 = x.split("\n")
        for word in x1:
            working_text.append(word)
    
    count = 0
    for i in range(0,len(working_text)):
      if (working_text[i] in negative_words) == True:
        count += 1
        if count > 2:
          word_clean = working_text[i]
          for x in punctuation:
            word_clean = word_clean.strip(x)
          censored_word = ""
          for x in range(0,len(word_clean)):
            censored_word = censored_word + "X"
          working_text[i] = working_text[i].replace(word_clean, censored_word)
    return " ".join(working_text)
    

email3_term_remove = find_ver3(email_three)
email3_censor = negative_count(email3_term_remove)
print(email3_censor)

def censor_four(input_text, censored_list):
  input_text_words = []
  for x in input_text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      input_text_words.append(word)
  for i in range(0,len(input_text_words)):
    checked_word = input_text_words[i].lower()
    for x in punctuation:
      checked_word = checked_word.strip(x)
    if checked_word in censored_list:

      # Censoring the targeted word
      word_clean = input_text_words[i]
      censored_word = ""
      for x in punctuation:
        word_clean = word_clean.strip(x)
      for x in range(0,len(word_clean)):
        censored_word = censored_word + "X"
      input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)

      # Censoring the word before the targeted word
      word_before = input_text_words[i-1]
      for x in punctuation:
        word_before = word_before.strip(x)
      censored_word_before = ""
      for x in range(0,len(word_before)):
        censored_word_before = censored_word_before + "X"
      input_text_words[i-1] = input_text_words[i-1].replace(word_before, censored_word_before)

      # Censoring the word after the targeted word
      word_after = input_text_words[i+1]
      for x in punctuation:
        word_after = word_after.strip(x)
      censored_word_after = ""
      for x in range(0,len(word_after)):
        censored_word_after = censored_word_after + "X"
      input_text_words[i+1] = input_text_words[i+1].replace(word_after, censored_word_after)
  return " ".join(input_text_words)

censor_all = proprietary_terms + negative_words

print(censor_four(email_four, censor_all))

