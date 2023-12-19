from collections import Counter

def most(text):

    filtered_text = [char for char in text if char.strip()]
    
    if not filtered_text:
        return None
    
    char_count = Counter(filtered_text)
    

    most_common = char_count.most_common(1)

    return most_common[0][0]


sample_text = "Lose john poor same it case do year we. Full how way even the sigh. Extremely nor furniture fat questions now provision incommode preserved. Our side fail find like now. Discovered travelling for insensible partiality unpleasing impossible she. Sudden up my excuse to suffer ladies though or. Bachelor possible marianne directly confined relation as on he."
result = most(sample_text)
print(f"Eng ko'p qaytarilgan simvol '{result}'")