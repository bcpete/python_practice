text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

def character_count(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] = dict.get(char) +1
        else:
            dict[char] = 1
    return dict

print(character_count(text))
