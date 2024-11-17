import os
#import psycopg2
#from psycopg2 import Error
from common.file_outputting import file_output_generation

# All the Data Attributes - dataattributeid in datatier
#1, Names - Last
#18, Names - First
#6, Credit Cards
#2, Area Code
#3, Address
#4, ZipCode US - Includes City & State
#5, Phone Number - US


#7,Bank Accounts
#8,Date of Birth
#9,Drivers License Number
#10,Social Security Number
#11,UPC Codes
#12,Company Names
#13,Employer Identification Numbers (EIN)
#14,Account Numbers
#15,User Identities
#16,Bank Routing
#21,Serial Numbers
#22,Regular Expression Based Data
#23,Professions
#24,Devices

# No Data Loaded for
#17,Phone Number - International
#19,Area Code Intl - IDD
#20,ZipCode Intl


#18
def names_first(postgres_connection, output_data):
    str_query = ("select datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,"
                 " dataattributeid, registeredapp,statusid from datatier where dataattributeid = 18 ")
    try:
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Executing a SQL query
        cursor.execute(str_query)
        # Fetch result
        # Fetch all rows
        data = cursor.fetchall()
        # Now you can sort the data based on any parameter
        sorted_list = sorted(data, key=lambda x: x[2], reverse=False)
        # for (datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
        #    dataattributeid, registeredapp,statusid) in sorted_list
        if (output_data == True):
            input_type = "names_first"
            file_output_generation(input_type, sorted_list)
        #print("You are connected to - ", record, "\n")
    except (Exception) as error:
        print("Error ", error)
    finally:
        if (postgres_connection):
            cursor.close()

#1
def names_last(postgres_connection):
    str_query = ("select datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,"
                 " dataattributeid, registeredapp,statusid from datatier where dataattributeid = 1 ")
    try:
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Executing a SQL query
        cursor.execute(str_query)
        # Fetch result
        # Fetch all rows
        data = cursor.fetchall()
        # Now you can sort the data based on any parameter
        sorted_list = sorted(data, key=lambda x: x[2], reverse=False)
        # Print the sorted data
        for (datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid) in sorted_list:
            print(datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid)
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (postgres_connection):
            cursor.close()

#6
def credit_cards(postgres_connection):
    str_query = ("select datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,"
                 " dataattributeid, registeredapp,statusid from datatier where dataattributeid = 6 ")
    try:
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Executing a SQL query
        cursor.execute(str_query)
        # Fetch result
        # Fetch all rows
        data = cursor.fetchall()
        # Now you can sort the data based on any parameter
        sorted_list = sorted(data, key=lambda x: x[2], reverse=False)
        # Print the sorted data
        for (datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid) in sorted_list:
            print(datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid)

        #print("You are connected to - ", record, "\n")
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (postgres_connection):
            cursor.close()

#2
def area_codes(postgres_connection):
    str_query = ("select datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,"
                 " dataattributeid, registeredapp,statusid from datatier where dataattributeid = 2")
    try:
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Executing a SQL query
        cursor.execute(str_query)
        # Fetch result
        # Fetch all rows
        data = cursor.fetchall()
        # Now you can sort the data based on any parameter
        sorted_list = sorted(data, key=lambda x: x[2], reverse=False)
        # Print the sorted data
        for (datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid) in sorted_list:
            print(datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid)

        #print("You are connected to - ", record, "\n")
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (postgres_connection):
            cursor.close()

#3
def addresses(postgres_connection):
    str_query = ("select datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,"
                 " dataattributeid, registeredapp,statusid from datatier where dataattributeid = 3")
    try:
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Executing a SQL query
        cursor.execute(str_query)
        # Fetch result
        # Fetch all rows
        data = cursor.fetchall()
        # Now you can sort the data based on any parameter
        sorted_list = sorted(data, key=lambda x: x[2], reverse=False)
        # Print the sorted data
        for (datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid) in sorted_list:
            print(datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid)

        #print("You are connected to - ", record, "\n")
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (postgres_connection):
            cursor.close()

#4
def zip_codes(postgres_connection):
    str_query = ("select datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,"
                 " dataattributeid, registeredapp,statusid from datatier where dataattributeid = 4")
    try:
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Executing a SQL query
        cursor.execute(str_query)
        # Fetch result
        # Fetch all rows
        data = cursor.fetchall()
        # Now you can sort the data based on any parameter
        sorted_list = sorted(data, key=lambda x: x[2], reverse=False)
        # Print the sorted data
        for (datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid) in sorted_list:
            print(datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid)

        #print("You are connected to - ", record, "\n")
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (postgres_connection):
            cursor.close()

#5
def phone_number(postgres_connection):
    str_query = ("select datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,"
                 " dataattributeid, registeredapp,statusid from datatier where dataattributeid = 5")
    try:
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Executing a SQL query
        cursor.execute(str_query)
        # Fetch result
        # Fetch all rows
        data = cursor.fetchall()
        # Now you can sort the data based on any parameter
        sorted_list = sorted(data, key=lambda x: x[2], reverse=False)
        # Print the sorted data
        for (datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid) in sorted_list:
            print(datatierid, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
            dataattributeid, registeredapp,statusid)

        #print("You are connected to - ", record, "\n")
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (postgres_connection):
            cursor.close()
