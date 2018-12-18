import yaml


class MyUser(object):
    def __init__(self, name):
        self.name = name


user = MyUser('Peter')
serialized = yaml.dump(user)
filename = 'serialized.yaml'

with open(filename, 'w') as file_object:
    file_object.write(serialized)

filename = 'untrusted.yaml'
with open(filename) as file_object:
    raw_data = file_object.read()

try:
    deserialized = yaml.load(raw_data)
    print(deserialized.name)
except:
    print('Error during deserialization')
