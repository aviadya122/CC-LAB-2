from database import get_db

def checkout_logic():
    db = get_db()
    db.row_factory = None

    events = db.execute("SELECT fee FROM events").fetchall()

    # Optimised logic: direct summation instead of nested loops
    total = 0
    for e in events:
        total += e[0]

    return total
