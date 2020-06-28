import numpy as np
import matplotlib.pyplot as plt


class MODEL:
    '''
    质点模型的二维坐标，偏转角，速度，车轮间距，间隔时间
    '''

    def __init__(self, x, y, theta, v, l, dt):
        # X坐标，Y坐标，偏转角，速度，车轮间距，间隔时间
        self.x = x
        self.y = y
        self.theta = theta
        self.v = v
        self.l = l
        self.dt = dt

    def update(self, vt, deltat):
        # 更新状态值
        dx = self.v * np.cos(self.theta)
        dy = self.v * np.sin(self.theta)
        dtheta = self.v * np.tan(deltat)/self.l
        self.x += dx * self.dt
        self.y += dy * self.dt
        self.theta += dtheta * self.dt

    def plot_duration(self, length, width):
        '''
        持续显示
        '''
        plt.scatter(self.x, self.y, color='g')
        plt.axis([0, length, -width / 2, width/2])

    def plot_dynamic_duration(self, length, width):
        '''
        机器动态持续显示
        '''
        plt.scatter(self.x, self.y, color='g')
        plt.axis([self.x - length / 2, self.x + length / 2,
                  self.y - width / 2, self.y + width / 2])

    def plot_dynamic_path(self, length, width):
        '''
        静止路径动态显示
        '''
        plt.scatter(self.x, self.y, color='g')
        plt.axis([self.x - length * 2 / 3, self.x +
                  length / 3, -width / 2, width / 2])


if __name__ == "__main__":
    input("质点模型，任意键退出")