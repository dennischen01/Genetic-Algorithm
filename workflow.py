import numpy as np

def evaluate_func(x):
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    return 4*a**2 - 3 * b + 5*c**3 - 6*d
class task(object):
    def __init__(self,taskResource,finished,front,next):
        """
        :param taskResource:所需要的资源
        :param finished:是否结束
        :param front:前一个任务
        :param next:后一个任务
        """
        self.taskResource = taskResource
        #结束了才能开始后面的
        self.finished = finished
        #front 前一个任务,若没有,为-1
        self.front = front
        #next 后一个任务,若没有,为-1
        self.next = next

class resource(object):
    def __init__(self,resourceMem,cost):
        self.resourceMem = resourceMem
        self.cost = cost

class DE(object):
    def __init__(self,n,m_size,f,cr,iterate_times,x_l,x_u):
        self.n = n
        self.m_size = m_size
        self.f = f
        self.cr = cr
        self.iterate_times = iterate_times
        self.x_l = x_l
        self.x_u = x_u

    def start(self):
        """
        :param n:维度
        :param m_size:个体数
        :param f:缩放因子
        :param cr:交叉概率
        :param iterate_times:迭代次数
        :param x_l:最小边界
        :param x_u:最大边界
        """

        #初始化第一代
        x_all = np.zeros((self.iterate_times, self.m_size, self.n))
        for i in range(self.m_size):
            x_all[0][i] = self.x_l + np.random.random() * (self.x_u - self.x_l)
        #print("x_all[0] = ",x_all[0])
        for g in range(self.iterate_times - 1):
            for i in range(self.m_size):
                # 变异操作,对第g代随机抽取三个组成一个新的个体,对于第i个个体来说,原来的第i个个体和它无关
                x_g_without_i = np.delete(x_all[g], i , 0)
                np.random.shuffle(x_g_without_i)
                h_i = x_g_without_i[1] + self.f * (x_g_without_i[2] - x_g_without_i[3])
                #处理变异操作后有可能超过区间
                h_i = [h_i[item] if h_i[item] < self.x_u[item] else self.x_u[item] for item in range(self.n)]
                h_i = [h_i[item] if h_i[item] > self.x_l[item] else self.x_l[item] for item in range(self.n)]
                #交叉操作,对变异后的个体,根据随机数与交叉阈值确定最后的个体
                v_i = np.array([x_all[g][i][j] if np.random.random() > self.cr else h_i[j] for j in range(self.n)])
                print("g =",g,"i=",i)
                print("v_i = ",v_i)
                #根据评估函数确定是否更新新的个体
                if evaluate_func(x_all[g][i]) > evaluate_func(v_i):
                    x_all[g+1][i] = v_i
                else:
                    x_all[g+1][i] = x_all[g][i]
        evaluate_result = [evaluate_func(x_all[self.iterate_times - 1][i]) for i in range(self.m_size)]
        print("x_all = ",x_all)
        best_x_i = x_all[self.iterate_times - 1][np.argmin(evaluate_result)]
        print("evaluate_result = ",evaluate_result)
        print("best_x_i=",best_x_i)




if __name__ == '__main__':
    #de = DE(4,10,0.5,0.3,2,np.array([0,1,0,2]),np.array([5,6,8,4]))
    #de.start()
    taskArr = []
    task0 = task(-1, 0, [-1], [-1])
    taskArr.append(task0)
    task1 = task(5, 0, [-1], [2,3])
    taskArr.append(task1)
    task2 = task(10, 0, [1], [4])
    taskArr.append(task2)
    task3 = task(20, 0, [1], [4])
    taskArr.append(task3)
    task4 = task(7, 0, [2,3], [-1])
    taskArr.append(task4)
    print(str(taskArr))



