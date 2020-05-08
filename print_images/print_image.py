import qrcode


class Print_Image(object):
    def __init__(self, org, name, voice, telephone, email):
        self.org = org
        self.name = name
        self.voice = voice
        self.telephone = telephone
        self.email = email

    def get_vard(self, path):
        template = "BEGIN:VCARD\nORG:{}\nFN:{}\nVOICE:{}\nTEL:{}\nEMAIL:{}\nEND:VCARD" \
            .format(self.org, self.name, self.voice, self.telephone, self.email)
        print(template)
        img = qrcode.make(template)
        img.save(path +'{}.png'.format(self.name))
        pass
