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

def find_ver2(text):
    working_text = text
    for i in proprietary_terms:
        if i in working_text:
            working_text = working_text.replace(i, '*Censored Information*')
    return working_text
    
email2_censor = find_ver2(email_two)
print(email2_censor)
print(email_two)

def find_ver3(text):
    working_text = text
    for i in proprietary_terms:
        if i in working_text:
            working_text = working_text.replace(i, '*Censored Information*')
    for bad in negative_words:
        count = 0
        if working_text.count(bad) >= 2:
            count + working_text.count(bad)
            working_text.replace(bad, '')
            return count 


#print(email_three)
#email3_censor = find_ver3(email_three)
#print(email3_censor)

