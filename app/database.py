from .models import User, Brick

database = {
    "users": {
        "mahum": User(name="mahum", role=5000, groups=["mahum"]),
        "isaac": User(name="isaac", role=4000, groups=["isaac"]),
        "admin": User(name="admin", role=4000, groups=["admins"]),
        "super": User(name="super", role=9001, groups=[]),
        "public": User(name="public", role=1000, groups=["public"]),
    },
    "bricks": {
        "red": Brick(color="red", allowed_role=5000, allowed_groups=["mahum", "isaac"]),
        "blue": Brick(color="blue", allowed_role=3000, allowed_groups=["admins"]),
        "green": Brick(color="green", allowed_role=1000, allowed_groups=["public"]),
        "yellow": Brick(color="yellow", allowed_role=4000, allowed_groups=["admins"]),
        "black": Brick(color="black", allowed_role=2000, allowed_groups=["public"]),
    },
}
