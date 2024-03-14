import wikipedia


def wiki(key):
    wikipedia.set_lang('uz')
    # wikipedia.set_lang('ru')
    try:
        result = wikipedia.summary(key)
    except wikipedia.exceptions.PageError:
        result = 'Ma`lumot topilmadi'
    except wikipedia.exceptions.DisambiguationError:
        result = 'Bu kalit so`z bilan juda ko`p ma`lumot topildi.\n' \
                    'Iltimos batafsil kiriting'
    return result

print(wiki('Москва'))