messages ='iLoveYourScript'
string_es =[]
def string_m(m_strings):
    for m in m_strings:
        if ord(m)<=ord('Z'):
            string_es.append('-')
            string_es.append(m.lower())
        else:
            string_es.append(m)
    messages =''.join(string_es)
    return print(messages)
string_m(messages)
