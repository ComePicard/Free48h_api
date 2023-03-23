import logging
from contextlib import contextmanager, closing

from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from pydantic import BaseSettings, SecretStr

logger = logging.getLogger("uvicorn.error")

CONNECTION_POOL = None


def get_pool():
    global CONNECTION_POOL
    if CONNECTION_POOL is None:
        config = BddConfig()
        cnx = pool.ThreadedConnectionPool(
            1,
            20,
            user=config.bdd_user,
            password=config.bdd_pass.get_secret_value(),
            host=config.bdd_host,
            port=config.bdd_port,
            database=config.bdd_name)
        if cnx:
            print("Création du pool de connexions réussie ✅")
        CONNECTION_POOL = cnx
    return CONNECTION_POOL


class BddConfig(BaseSettings):
    bdd_host: str
    bdd_port: int
    bdd_name: str
    bdd_user: str
    bdd_pass: SecretStr


def connection():
    cnx_pool = get_pool()
    cnx = cnx_pool.getconn()
    logger.info("------> on a obtenu la connexion   %s", cnx.pgconn_ptr)
    return cnx


@contextmanager
def get_cursor():
    cnx_pool = get_pool()
    cnx = cnx_pool.getconn()
    try:
        with cnx:
            yield cnx.cursor(cursor_factory=RealDictCursor)
    finally:
        cnx_pool.putconn(cnx)


@contextmanager
def bdd() -> RealDictCursor:
    with closing(connection()) as cnx:
        cnx.autocommit = True
        with cnx.cursor(cursor_factory=RealDictCursor) as cur:
            yield cur
