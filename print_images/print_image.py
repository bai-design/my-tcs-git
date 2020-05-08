import qrcode


class Print_Image(object):
    def __init__(self, org, name, telephone, email):
        self.org = org
        self.name = name
        self.telephone = telephone
        self.email = email

    def get_vard(self, path):
        template = "BEGIN:VCARD\nORG:{}\nFN:{}\nTEL:{}\nEMAIL:{}\nEND:VCARD" \
            .format(self.org, self.name, self.telephone, self.email)
        print(template)
        img = qrcode.make(template)
        image_path = path + '%s.png'%(self.name)
        img.save(image_path)
