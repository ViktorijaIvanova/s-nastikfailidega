def kirjuta_faili(f,mas):
    """
    """
    fail=open(f,'w',encoding="utf-8-sig")
    for element in mas:
        fail.write(element+'\n')
    fail.close()

rus=["яблоко","дом","улица","комната"]
kirjuta_faili("rus.txt",rus)
est=["õun","maja","täna","tuba"]
kirjuta_faili("est.txt",est)

def translate(word):
    """
    """
    est =("est.txt")
    rus =("rus.txt")
    index = -1
    for i in range(len(rus)):
        if word.lower() == rus[i].lower():
            index = i
        break
    if index != -1:
        return est[index]
    else:
        print("Sõna sõnastikus pole.")
        choice = input("Kas soovite selle sõnaraamatusse lisada? (jah/ei) ")
    if choice.lower() == "jah":
        add_word_to_dict(word, "rus.txt", "est.txt")
    return None

def translate_est_to_rus(word):
    """
    """
    est = loe_failist("est.txt")
    rus = loe_failist("rus.txt")
    index = -1
    for i in range(len(est)):
        if word.lower() == est[i].lower():
            index = i
        break
    if index != -1:
        return rus[index]
    else:
        print("Sõna sõnastikus pole.")
        choice = input("Kas soovite selle sõnaraamatusse lisada? (jah/ei) ")
    if choice.lower() == "jah":
        add_word_to_dict(word, "est.txt", "rus.txt")
    return None

def add_word_to_dict(word, dict_file, translation_file):
    """
    """
    dict = loe_failist(dict_file)
    translation = loe_failist(translation_file)
    dict.append(word)
    translation.append(input(f"Sisestage sõna „{word}” tõlge: "))
    kirjuta_faili(dict_file, dict)
    kirjuta_faili(translation_file, translation)
    print("Sõna on sõnastikku lisatud.")
    return

