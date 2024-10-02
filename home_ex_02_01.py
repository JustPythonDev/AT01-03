def count_vowels(s):
    vowels = "aeiouy"  # Список гласных букв (включая заглавные)
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count