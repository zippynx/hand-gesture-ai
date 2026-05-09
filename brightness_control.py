import screen_brightness_control as sbc


def set_brightness(value):

    value = int(value)

    value = max(0, min(100, value))

    sbc.set_brightness(value)
    