from common.Consts import Consts

def to_screen(point) -> tuple[float, float]:
    x, y = point[0], point[1]
    return (x + Consts.X0, Consts.HEIGHT - (y + Consts.Y0))