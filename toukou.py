import psycopg2

class Toukou:
    def __init__(self,tid,name,body,hi) -> None:
        self.tid = tid
        self.name = name
        self.body = body
        self.hi = hi

class ToukouDB:
    def __init__(self) -> None:
        user = 'postgres'
        passwd = 'root'

        dsn = f"postgresql://{user}:{passwd}@localhost:5432/bbs"
        self.con = psycopg2.connect(dsn=dsn)

        self.cur = self.con.cursor()
    
    def close(self):
        self.con.close()

    def get_all(self) -> list:
        self.cur.execute('SELECT * FROM toukou ORDER BY hi DESC')
        rows = self.cur.fetchall()

        ret = []
        for row in rows:
            tid,name,body,hi = row
            toukou = Toukou(tid,name,body,hi)
            ret.append(toukou)
        
        return ret

    def insert(self,toukou):
        self.cur.execute('INSERT INTO toukou (name,body,hi) VALUES(%s,%s,NOW())',[toukou.name,toukou.body])
        self.con.commit()

if __name__ == "__main__":
    db = ToukouDB()

    d = Toukou(0,'田中','こんにちは',None)
    db.insert(d)
    lst = db.get_all()
    for t in lst:
        print(t.name,t.body)

