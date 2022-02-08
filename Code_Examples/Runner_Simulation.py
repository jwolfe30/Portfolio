"""
Authors: Kevin Hao, Josh Wolfe, Tazebe Beyene

This program creates a Runner class and then runs a race simulation, resulting
in the race statistics.
"""

from random import gauss, uniform
from statistics import mean
from math import exp
import pylab


class Runner:
    """
    Creates a Runner that can be passed parameters such speed and stamina.
    These runners can be raced/compared when given courses to run
    """
    et = 0
    t_dist = 0
    contestant = 0

    def __init__(self, initial_speed=6.0, stamina=200, time=0):
        """
        Intial function sets runner parameters; inital speed, stamina,
        and time and assigns a unique contestant number
        """

        Runner.contestant += 1
        self.initial_speed = initial_speed
        self.stamina = stamina

    def __str__(self):
        """
        Prints out the runner stats
        """

        return 'Runner(%.1f, %d)' % (self.initial_speed, self.stamina)

    def __repr__(self):
        """
        Prints out the runner stats
        """

        return 'Runner(%.1f, %d)' % (self.initial_speed, self.stamina)

    def __lt__(self, other):
        """
        Compares the runners to see which is leading/winning
        """

        if isinstance(other, Runner):
            return self.et < other.et

    def run(self, distance, grade):
        """
        Sets the distance and the grade(steepness) for the course
        """

        s = self.speed(grade)
        self.t_dist += distance
        self.et += s * self.t_dist

    def speed(self, grade=0.0):
        """
        Calculates the speed using the course grade, the stamina,
        and is adjusted by a random factor from a standard distribution
        """

        S = self.initial_speed
        T = self.stamina
        t = self.et
        s = (S * (exp(-self.et / T))) + (5.4 * grade)
        return s * gauss(1.0, 0.1)


def simulation(contestants=100, races=1000, binsize=20):
    """
    Creates and runs a simulation using a given amount of runners (default
    is 100). This runs a given amount of races (default is 1000) and calculates
    the results. A plot is generated at the end to show the average race times.
    """

    A_time = []
    for race in range(races):
        for contest in range(contestants):
            contestant_times = []
            """
                runs a race over a given course (a list of distance/grade pairs)
                with 100 runners and 1000 simulated races
                choosing the runners with:
                a random initial speed (Gaussian distribution, mean 6.0 min/mile,
                standard deviation 1.2 min/mile)
                a random stamina factor (uniform distribution between 100 and 1000)
            """
            contestant = Runner(gauss(6.0, 1.2), uniform(100, 1000))
            # Three race patterns
            contestant.run(10.0, 0.0)  # run 10 miles on a flat segment
            contestant.run(3.0, 0.3)  # three mile hill
            contestant.run(1.8, -0.8)  # last 1.8 miles downhill
            contestant_times.append(contestant.et)
        A_time.append(mean(contestant_times))
    # Histogram of average race time
    pylab.figure(1)
    pylab.hist(A_time, bins=binsize)
    pylab.ylabel('Average Time (Minutes)')
    pylab.xlabel('Number of Races')
    pylab.show()
