import numpy as np
class task(object):
    def __init__(self,size):
        self.size = size
        self.taskResource = []
        for i in range(size):
            self.taskResource.append(np.random.randint(10,20))