class Apple(object):
    name = 'by'
    sex = ('male','female')
    langue =['English']
    def __init__(self,color,taste):
        self.color = color
        self.taste = taste
        self.__subject = 'rose'
    def return_subject(self):
        return self.__subject
    def _eat(self):
        print('Apple is fruit')
        print('We can eat')
    def __roll(self):
        print('Aplle can roll')
    def round(self):
        return self.__roll()
class Red_Delicious(Apple):
    def __init__(self,color,taste,shape):
        super().__init__(color,taste)
#        self.color ='blue'
        self.shape = shape
    def __str__(self):
        return 'This is a class'
    def apple_attribute(self):
        print('Color of Apples is %s;'%self.color)
        print('Taste of Apples is %s;' % self.taste)
        print('Shape of Apples is %s;' % self.shape)
    def _eat(self):
        super()._eat()
#       print('My favorite fruite is apple')
if __name__ == '__main__':
    fruit = Red_Delicious('red','sweet','snake')
    print(fruit.return_subject())
    fruit.round()
    print(Red_Delicious.mro())
    fruit.apple_attribute()
    fruit._eat()
    print(fruit)
    print('My name is %s'%Apple.name)
    print('My sex is {}'.format(Apple.sex))
    print('I learn langue:%r'%Apple.langue)
    c = Apple('green','sweets')
    c.name ='sy'
    c.sex ='female'
    c.langue.insert(0,'China')
    print('My name is %s'%c.name)
    print('My sex is {}'.format(c.sex))
    print('I learn langue:%r'%c.langue)
#    Apple.name ='BS'
#   Apple.sex='FM'
    b = Apple('black','sweet')
    print('My name is %s'%b.name)
    print('My sex is {}'.format(b.sex))
    print('I learn langue:%r'%b.langue)

