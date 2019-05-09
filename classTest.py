class student(object):
    def __init__(self, score):
        self.score = score

def getStuSocre(stu):
    return stu.score

if __name__=='__main__':
    s = student(80)
    score = getStuSocre(s)
    print(score)

