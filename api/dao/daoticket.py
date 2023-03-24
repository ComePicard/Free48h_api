from api.dao import get_cursor


def get_all_tickets():
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM ticket
        """
        cur.execute(sql)
        result = cur.fetchall()
    return result


def get_ticket_by_id(ticket_id: int):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM ticket
            WHERE id = %(ticket_id)s
        """
        cur.execute(sql, {"ticket_id": ticket_id})
        result = cur.fetchone()
    return result


def get_ticket_by_email(email: str):
    with get_cursor() as cur:
        sql = """
            SELECT *
            FROM ticket
            INNER JOIN account
            ON account.id = ticket.sender_id
            WHERE account.email = %(email)s
        """
        cur.execute(sql, {"email": email})
        result = cur.fetchone()
    return result


def add_ticket(content: str, sender_id: int, support_id: int, category_id: int, status_id: int):
    with get_cursor() as cur:
        sql = """
            INSERT INTO ticket(
                content,
                sender_id,
                support_id,
                category_id,
                status_id
                )
            VALUES (
                %(content)s,
                %(sender_id)s,
                %(support_id)s,
                %(category_id)s,
                %(status_id)s,
            )
            RETURNING *
        """
        cur.execute(sql, {
            "content": content,
            "sender_id": sender_id,
            "support_id": support_id,
            "category_id": category_id,
            "status_id": status_id,
        })
        result = cur.fetchone()
    return result


def edit_ticket(ticket_id: int, content: str, sender_id: int, support_id: int, category_id: int, status_id: int):
    with get_cursor() as cur:
        sql = """
            UPDATE ticket
            SET (
                content=%(content),
                sender_id=%(sender_id),
                support_id=%(support_id),
                category_id=%(category_id),
                status_id=%(status_id)
            )
            WHERE id=%(ticket_id)s
            RETURNING *
        """
        cur.execute(sql, {
            "content": content,
            "sender_id": sender_id,
            "support_id": support_id,
            "category_id": category_id,
            "status_id": status_id,
            "ticket_id": ticket_id
        })
        result = cur.fetchone()
    return result


def assign_support_to_ticket(support_id, ticket_id):
    with get_cursor() as cur:
        sql = """
            UPDATE ticket(support_id = %(support_id)s)
            WHERE id = %(ticket_id)
            RETURNING *
        """
        cur.execute(sql, {'ticket_id': ticket_id, "support_id": support_id})
        result = cur.fetchone()
    return result


def change_status_of_ticket(ticket_id, status_id):
    with get_cursor() as cur:
        sql = """
            UPDATE ticket(status_id = %(status_id)s)
            WHERE id = %(ticket_id)
            RETURNING *
        """
        cur.execute(sql, {"status_id": status_id, "ticket_id": ticket_id})
        result = cur.fetchone()
    return result


def edit_content_of_ticket(ticket_id, content):
    with get_cursor() as cur:
        sql = """
            UPDATE ticket(content = %(content)s)
            WHERE id = %(ticket_id)
            RETURNING *
        """
        cur.execute(sql, {"content": content, "ticket_id": ticket_id})
        result = cur.fetchone()
    return result


def change_category_of_ticket(ticket_id, category_id):
    with get_cursor() as cur:
        sql = """
            UPDATE ticket(category_id = %(category_id)s)
            WHERE id = %(ticket_id)
            RETURNING *
        """
        cur.execute(sql, {"category_id": category_id, "ticket_id": ticket_id})
        result = cur.fetchone()
    return result


def delete_ticket(ticket_id: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM ticket
            WHERE id = %(ticket_id)s
        """
        cur.execute(sql, {"ticket_id": ticket_id})
