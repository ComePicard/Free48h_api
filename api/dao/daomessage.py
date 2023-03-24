from api.dao import get_cursor


def get_all_message():
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM message
        """
        cur.execute(sql)
        result = cur.fetchall()
    return result


def get_message_by_id(id: int):
    with get_cursor() as cur:
        sql = """
            SELECT  *
            FROM message
            WHERE  id = %(id)s
        """
        cur.execute(sql, {"id": id})
        result = cur.fetchone()
    return result


def get_message_by_account_email(email: str):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM message
            INNER JOIN account
            ON message.sender_id = account.id
            WHERE account.email = %(email)s
        """
        cur.execute(sql, {"email": email})
        result = cur.fetchall()
    return result


def get_message_by_ticket_id(ticket_id: int):
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


def add_message(
        content: str,
        sender_id: int,
        ticket_id: int,
):
    with get_cursor() as cur:
        sql = """
            INSERT INTO message(
                content,
                sender_id,
                ticket_id
            )
            VALUES (
                %(content)s,
                %(sender_id)s,
                %(ticket_id)s
            )
            RETURNING *
        """
        cur.execute(sql, {
            "content": content,
            "sender_id": sender_id,
            "ticket_id": ticket_id,
        })
        result = cur.fetchone()
    return result


def edit_message(
        id: int,
        content: str,
        sender_id: int,
        ticket_id: int,
):
    with get_cursor() as cur:
        sql = """
            UPDATE FROM message(
                content = %(content)s,
                sender_id = %(sender_id)s,
                ticket_id = %(ticket_id)s,
            )
            WHERE id = %(id)s
            RETURNING *
        """
        cur.execute(sql, {
            "id": id,
            "content": content,
            "sender_id": sender_id,
            "ticket_id": ticket_id,
        })
        result = cur.fetchone()
    return result


def delete_message(id: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM message
            WHERE id = %(id)s
        """
        cur.execute(sql, {"id": id})
