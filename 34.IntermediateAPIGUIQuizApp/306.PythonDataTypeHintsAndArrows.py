# age: int
# name: str
# height: float
# is_human: bool
#
# This is calling Type Hint
def police_check(age: int) ->bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False