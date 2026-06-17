def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    reversed_text = clean_text[::-1]

    return clean_text == reversed_text


def result(text):
    print(is_palindrome(text))


user_text = input("Enter text: ")
result(user_text)