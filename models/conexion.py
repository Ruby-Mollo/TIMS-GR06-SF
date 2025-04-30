# models/conexion.py
import mysql.connector
from config import db_config

def get_connection():
    return mysql.connector.connect(
        host=db_config.HOST,
        user=db_config.USER,
        password=db_config.PASSWORD,
        database=db_config.DATABASE
    )
