import psycopg2
import os
from discord.ext import commands
pass


def insert_player(id, tag):
    conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASS'], host=os.environ['DB_HOST'])
    with conn:
        with conn.cursor() as cur:
            cur.execute(f'INSERT INTO user_tags (discord_id, profile_tag) VALUES (\'{id}\', \'{tag}\') ON CONFLICT DO NOTHING')
    conn.close()

def insert_clan(id, tag):
    conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASS'], host=os.environ['DB_HOST'])
    with conn:
        with conn.cursor() as cur:
            cur.execute(f'INSERT INTO user_tags (discord_id, clan_tag) VALUES (\'{id}\', \'{tag}\') ON CONFLICT DO NOTHING')
    conn.close()

def select_id(id):
    conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASS'], host=os.environ['DB_HOST'])
    with conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT profile_tag FROM user_tags WHERE discord_id = \'{id}\'')
            tag = cur.fetchone()
    conn.close()
    return tag

def unlink_user(id):
    conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASS'], host=os.environ['DB_HOST'])
    with conn:
        with conn.cursor() as cur:
            cur.execute(f'DELETE FROM user_tags WHERE discord_id = \'{id}\'')
    conn.close()