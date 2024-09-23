import snowflake.connector

def connect_to_snowflake():
    conn = snowflake.connector.connect(
        user='<your_username>',
        password='<your_password>',
        account='<your_account_identifier>',
        warehouse='<your_warehouse>',
        database='<your_database>',
        schema='<your_schema>'
    )
    return conn

def deploy_ddl_to_snowflake(ddl_file):
    conn = connect_to_snowflake()
    with conn.cursor() as cur:
        with open(ddl_file, 'r') as f:
            sql = f.read()
            cur.execute(sql)
    conn.close()

if __name__ == "__main__":
    ddl_file = 'your_ddl.sql'
    deploy_ddl_to_snowflake(ddl_file)
