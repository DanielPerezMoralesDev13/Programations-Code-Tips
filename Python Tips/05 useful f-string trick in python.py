
from datetime import datetime
def primerEjemplo():
    n: int = 1_000_000_000
    print(f"{n}")

    n: float = 1e9
    print(f"{n}")

    n: int = 1000000000
    print(f"{n:_}")
    print(f"{n:,}")


def segundoEjemplo():
    var: str = "var"
    print(f"{var:>20}:")
    print(f"{var:<20}:")
    print(f"{var:^20}:")

    print(f"{var:_>20}:")
    print(f"{var:#<20}:")
    print(f"{var:|^20}:")


def tercerEjemplo():
    now: datetime = datetime.now()
    print(f"{now:%d.%m.%y (%H:%M:%S)}")
    print(f"{now:%c}")
    print(f"{now:%I%p}")


def cuartoEjemplo():
    n: float = 1234.5678
    print(n)
    print(round(n,2))
    print(f"{n:.2f}")
    print(f"{n:.0f}")
    print(f"{n:,.3f}")
    print(f"{n:_.3f}")

def quintoEjemplo():
    a: int = 5
    b: int = 10
    my_var: str = "daniel says hi"
    print(f"a + b = {a + b}")
    print(f"{a + b = }")
    print(f"{a + b =}")
    print(f"{a + b=}")
    print(f"{bool(a) = }")
    print(f"{my_var = }")






quintoEjemplo()