from api.dao import get_cursor


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


def delete_ticket(ticket_id: int):
    with get_cursor() as cur:
        sql = """
            DELETE FROM ticket
            WHERE id = %(ticket_id)s
        """
        cur.execute(sql, {"ticket_id": ticket_id})

