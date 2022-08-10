def test():
    # Пробы с хэштэгом
    hashtags = [word[1:] for word in get_post_by_pk(5)['content'].split() if word[0] == '#']
    set(hashtags)
    print(hashtags)
