from connectors.postgresql import create_conn, close_conn
from common.listbuilder.lists_generated_data import (names_first)

def main():
    postgres_connection = create_conn()
    # Table Select
    output_data = True
    names_first(postgres_connection, output_data)
    # names_last(postgres_connection)
    # credit_cards(postgres_connection)
    # area_codes(postgres_connection)
    # addresses(postgres_connection)
    # zip_codes(postgres_connection)
    # phone_number(postgres_connection)

    # cursor_query = postgres_connection.cursor()
    # cursor_query.execute("SELECT * from asset_source")
    # data = cursor_query.fetchall()
    # for row in data:
    # Access individual columns using indices
    # column1_value = row[0]
    # column2_value = row[1]
    # print(f"Column 1: {column1_value}, Column 2: {column2_value}")
    # print("Result of asset_source query: ", cursor.fetchall())
    close_conn(postgres_connection)
    # print("PostgreSQL connection is closed")


print("Program Ended")

if __name__ == "__main__":
    main()