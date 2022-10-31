from dataclasses import dataclass
from math import log


@dataclass
class MandelbrotSet:
    '''
        Class calculating the iterations to convergence for the
    mandelbrot set.
    '''
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c: complex) -> bool:
        return self.stable(c) == 1

    def stable(self, c: complex, smooth: bool =False, clamp: bool =True) -> float:
        value = self.escape_count(c, smooth) / self.max_iterations
        if clamp:
            return max(0.0, min(value, 1.0))
        else:
            return value

    def escape_count(self, c: complex, smooth: bool =False) -> int | float:
        z = 0
        for i in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return i + 1 - log(log(abs(z))) / log(2)
                return i
        return self.max_iterations