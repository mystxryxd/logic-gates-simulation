from pygame import Vector2, Rect


def point_in_circle(point: Vector2, circle: Vector2, radius: int):
    return (circle - point).magnitude() <= radius


def point_in_rectangle(point: Vector2, rect: Rect):
    return (
        point.x >= rect.left
        and point.x <= rect.right
        and point.y >= rect.top
        and point.y <= rect.bottom
    )


def is_pin_on(pin):
    return (connection := pin.connection) and connection.source.enabled
