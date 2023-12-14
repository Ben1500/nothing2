import decimal
from decimal import Decimal,getcontext,Context

new_context = Context(pres=5,rounding=decimal.ROUND_UP)
decimal.setcontext(new_context)

print(decimal(0.1432))