

def build_rdbms_connection_string(rdbms_type :str,host :str, port :int, dbname :str, uid:str, pwd:str):
    print("build_rdbms_connection_string")
    conn_string = f"{rdbms_type}://{uid}:{pwd}@{host}:{port}/{dbname}"
    return conn_string