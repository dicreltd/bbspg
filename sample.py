import psycopg2
import os
 
#dsn = f"postgresql://{ユーザー名}:{パスワード}@{ホスト名(IPアドレス)}:{ポート番号}/{データベース名}"

# user = 'postgres'
# passwd = 'root'
dsn = os.environ.get('DATABASE_URL') or "postgresql://localhost/bbspg"

# dsn = f"postgresql://{user}:{passwd}@localhost:5432/hanbai"
print(dsn)
con = psycopg2.connect(dsn=dsn)
cur = con.cursor()
cur.execute('SELECT * FROM shouhin')
#cur.commit()
results = cur.fetchall()
for r in results:
    print(r)