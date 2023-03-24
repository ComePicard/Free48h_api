from api.dao import get_cursor


def get_all_account():
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM account
        """
        cur.execute(sql)
        result = cur.fetchall()
    return result


def get_account_by_id(id: int):
    with get_cursor() as cur:
        sql = """
            SELECT  *
            FROM account
            WHERE  id = %(id)s
        """
        cur.execute(sql, {"id": id})
        result = cur.fetchone()
    return result


def get_account_by_email(email: str):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM account
            WHERE email = %(email)s
        """
        cur.execute(sql, {"email": email})
        result = cur.fetchone()
    return result


def add_account(
        firstname: str,
        lastname: str,
        email: str,
        password: str,
        role_id: int,
):
    with get_cursor() as cur:
        sql = """
            INSERT INTO account(
                firstname,
                lastname,
                email,
                password,
                role_id
            )
            VALUES (
                %(firstname)s,
                %(lastname)s,
                %(email)s,
                %(password)s,
                %(role_id)s
            )
            RETURNING *
        """
        cur.execute(sql, {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "role_id": role_id,
        })
        result = cur.fetchone()
    return result


def edit_account(
        id: int,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
        role_id: int,
):
    with get_cursor() as cur:
        sql = """
            UPDATE FROM account(
                firstname = %(firstname)s,
                lastname = %(lastname)s,
                email = %(email)s,
                password = %(password)s,
                role_id = %(role_id)s
            )
            WHERE id = %(id)s
            RETURNING *
        """
        cur.execute(sql, {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "role_id": role_id,
            "id": id,
        })
        result = cur.fetchone()
    return result


def delete_account(id: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM account
            WHERE id = %(id)s
        """
        cur.execute(sql, {"id": id})
