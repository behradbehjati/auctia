import datetime
import time


def time_correction(float_time):
    min=(time.time()-float_time)/60
    return f'{int(min)} دقیقه قبل'