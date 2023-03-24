from api.dao import get_cursor


def get_all_file():
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM file
        """
        cur.execute(sql)
        result = cur.fetchall()
    return result


def get_file_by_id(id: int):
    with get_cursor() as cur:
        sql = """
            SELECT  *
            FROM file
            WHERE  id = %(id)s
        """
        cur.execute(sql, {"id": id})
        result = cur.fetchone()
    return result


def get_file_by_ticket_id(ticket_id: int):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM message
            INNER JOIN account
            ON message.sender_id = account.id
            WHERE account.id = %(ticket_id)s
        """
        cur.execute(sql, {"ticket_id": ticket_id})
        result = cur.fetchall()
    return result


def add_file(
        link: str,
        ticket_id: int,
):
    with get_cursor() as cur:
        sql = """
            INSERT INTO file(
                link,
                ticket_id
            )
            VALUES (
                %(link)s,
                %(ticket_id)s
            )
            RETURNING *
        """
        cur.execute(sql, {
            "link": link,
            "ticket_id": ticket_id,
        })
        result = cur.fetchone()
    return result


def edit_file(
        id: int,
        link: str,
        ticket_id: int,
):
    with get_cursor() as cur:
        sql = """
            UPDATE FROM file(
                link = %(link)s,
                ticket_id = %(ticket_id)s,
            )
            WHERE id = %(id)s
            RETURNING *
        """
        cur.execute(sql, {
            "id": id,
            "link": link,
            "ticket_id": ticket_id,
        })
        result = cur.fetchone()
    return result


def delete_file(id: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM file
            WHERE id = %(id)s
        """
        cur.execute(sql, {"id": id})
