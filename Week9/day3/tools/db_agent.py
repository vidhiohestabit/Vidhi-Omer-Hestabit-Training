import sqlite3

DB = "data/sales.db"


def create_table_from_csv(data):

    if not data:
        raise ValueError("CSV file is empty or not loaded correctly")

    import sqlite3
    conn = sqlite3.connect("data/sales.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS sales")

    columns = data[0].keys()
    col_str = ", ".join([f"{c} TEXT" for c in columns])

    cur.execute(f"CREATE TABLE sales ({col_str})")

    for row in data:
        cur.execute(
            f"INSERT INTO sales VALUES ({','.join(['?']*len(row))})",
            list(row.values())
        )

    conn.commit()
    conn.close()


def run_query(query):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(query)
    rows = cur.fetchall()

    conn.close()

    return rows