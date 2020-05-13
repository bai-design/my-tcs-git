import qrcode


class Print_Image(object):
    """实现生成二维码图片功能"""
    def __init__(self, org, name, telephone, email):
        """
            构造函数，初始化以下参数：

            self.org：部门（职位）
            self.name：姓名
            self.telephone：电话
            self.email: 邮箱

        """
        self.org = org
        self.name = name
        self.telephone = telephone
        self.email = email

    def get_vard(self, path):
        """生成二维码图片"""
        # 构造vCard格式字符串
        template = "BEGIN:VCARD\nORG:{}\nFN:{}\nTEL:{}\nEMAIL:{}\nEND:VCARD" \
            .format(self.org, self.name, self.telephone, self.email)
        print(template)
        # 制作二维码图片
        img = qrcode.make(template)
        # 图片保存路径
        image_path = path + '%s.png'%(self.name)
        # 保存图片
        img.save(image_path)


