import math


class CelestialBody:
    def __init__(self, mass=5.972e24, distance_km=384400):
        # self.orbiting = orbiting

        self.gx = 0
        self.gy = -10
        self.g = 9.81

        self.dt = 3600
        self.distance = distance_km * 1000

        self.G = 6.67259e-11
        self.M = 5.972e24

        self.v0 = math.sqrt(self.G * self.M / self.distance)

        self.x = 0
        self.y = self.distance

        self.vx = self.v0
        self.vy = 0

        self.ax = 0
        self.ay = 0

    def calc_U(self):  # katy Q  R
        Ux = -self.x / self.distance
        Uy = -self.y / self.distance
        return Ux, Uy

    def calc_U_2(self, dt):  # AA AB
        x, y = self.calc_position_2(dt)
        distance = self.calc_distance(x, y)
        Ux = -x / distance
        Uy = -y / distance
        return Ux, Uy

    def calc_a(self):  # S    T U
        a = self.G * self.M / self.distance ** 2
        ax = a * self.calc_U()[0]
        ay = a * self.calc_U()[1]
        return ax, ay

    def calc_a_2(self, dt):
        x, y = self.calc_position_2(dt)
        distance = self.calc_distance(x, y)
        a = self.G * self.M / distance ** 2
        ax = a * self.calc_U_2(dt)[0]
        ay = a * self.calc_U_2(dt)[1]
        return ax, ay

    def calc_distance(self, x, y):  # P
        distance = math.sqrt(x ** 2 + y ** 2)
        return distance

    def calc_W(self, x, y):
        return -x, -y

    def calc_g(self):
        return self.G * self.M / (self.distance)

    def calc_position(self, dt):  # x=F y=G
        x = self.x + self.calc_v(dt / 2)[0] * dt
        y = self.y + self.calc_v(dt / 2)[1] * dt
        return x, y

    def calc_position_2(self, dt):
        x = self.x + self.vx * dt / 2
        y = self.y + self.vy * dt / 2
        return x, y

    def calc_v(self, dt):
        vx = self.vx + self.ax * dt
        vy = self.vy + self.ay * dt
        return vx, vy

    def euler_movement(self, dt, t_max):
        times = [0]
        x_positions = [self.x]
        y_positions = [self.y]
        curr_percentage = 0
        while (times[-1] < t_max):
            if times[-1]/t_max - curr_percentage >0.01:
                curr_percentage+=0.01
                print(f'{times[-1]*100/t_max}%')
            self.distance = self.calc_distance(self.x, self.y)
            self.ax, self.ay = self.calc_a()
            self.x, self.y = self.calc_position(dt)
            self.vx, self.vy = self.calc_v(dt)

            times.append(times[-1] + dt)
            x_positions.append(self.x)
            y_positions.append(self.y)
        return times, x_positions, y_positions

    def euler_movement_2(self, dt, t_max):
        times = [0]
        x_positions = [self.x]
        y_positions = [self.y]
        curr_percentage = 0
        while (times[-1] < t_max):
            if times[-1]/t_max - curr_percentage >0.01:
                curr_percentage+=0.01
                print(f'{times[-1]*100/t_max}%')
            self.distance = self.calc_distance(self.x,self.y)
            self.ax, self.ay = self.calc_a_2(dt)
            self.x, self.y = self.calc_position_2(dt)
            self.vx, self.vy = self.calc_v(dt)

            times.append(times[-1] + dt)
            x_positions.append(self.x)
            y_positions.append(self.y)
        return times, x_positions, y_positions
