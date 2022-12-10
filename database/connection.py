import os
import psycopg2
import pandas as pd

def db_connection():
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']

    conn = None

    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connectée")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn

def insert_sample(data, conn):
    query = f"""
            INSERT INTO app_echantillons (echantillon, elem_ch_1, elem_ch_2, elem_ch_3, elem_ch_4,
                                          elem_ch_5, elem_ch_6, elem_ch_7, elem_ch_8, elem_ch_9,
                                          elem_ch_10, elem_ch_11, elem_ch_12, elem_ch_13, elem_ch_14,
                                          elem_ch_15, elem_ch_16, elem_ch_17, elem_ch_18, elem_ch_19,
                                          elem_ch_20, elem_ch_21, elem_ch_22, elem_ch_23, elem_ch_24,
                                          elem_ch_25, elem_ch_26, elem_ch_27, elem_ch_28, elem_ch_29,
                                          elem_ch_30, elem_ch_31, elem_ch_32, elem_ch_33, elem_ch_34,
                                          elem_ch_35, elem_ch_36, elem_ch_37, elem_ch_38, elem_ch_39,
                                          elem_ch_40, d_0_1, d_0_2, d_0_5, d_0_8, d_0_9, d_3_2, d_4_3,
                                          param_rr_1, param_rr_2, param_rr_3, prediction_rc28j, prediction_date)

            VALUES('{data["echantillon"][0]}', {data["elem_ch_1"][0]}, {data["elem_ch_2"][0]}, {data["elem_ch_3"][0]},
                   {data["elem_ch_4"][0]}, {data["elem_ch_5"][0]}, {data["elem_ch_6"][0]}, {data["elem_ch_7"][0]},
                   {data["elem_ch_8"][0]}, {data["elem_ch_9"][0]}, {data["elem_ch_10"][0]}, {data["elem_ch_11"][0]},
                   {data["elem_ch_12"][0]}, {data["elem_ch_13"][0]}, {data["elem_ch_14"][0]}, {data["elem_ch_15"][0]},
                   {data["elem_ch_16"][0]}, {data["elem_ch_17"][0]}, {data["elem_ch_18"][0]}, {data["elem_ch_19"][0]},
                   {data["elem_ch_20"][0]}, {data["elem_ch_21"][0]}, {data["elem_ch_22"][0]}, {data["elem_ch_23"][0]},
                   {data["elem_ch_24"][0]}, {data["elem_ch_25"][0]}, {data["elem_ch_26"][0]}, {data["elem_ch_27"][0]},
                   {data["elem_ch_28"][0]}, {data["elem_ch_29"][0]}, {data["elem_ch_30"][0]}, {data["elem_ch_31"][0]},
                   {data["elem_ch_32"][0]}, {data["elem_ch_33"][0]}, {data["elem_ch_34"][0]}, {data["elem_ch_35"][0]},
                   {data["elem_ch_36"][0]}, {data["elem_ch_37"][0]}, {data["elem_ch_38"][0]}, {data["elem_ch_39"][0]},
                   {data["elem_ch_40"][0]}, {data["d_0_1"][0]}, {data["d_0_2"][0]}, {data["d_0_5"][0]}, {data["d_0_8"][0]},
                   {data["d_0_9"][0]}, {data["d_3_2"][0]}, {data["d_4_3"][0]}, {data["param_rr_1"][0]}, {data["param_rr_2"][0]},
                   {data["param_rr_3"][0]}, {data["prediction_rc28j"][0]}, '{data["prediction_date"][0]}')
            ;
            """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit() # <- We MUST commit to reflect the inserted data
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:    
        conn.close()