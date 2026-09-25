from utils.db_utils import Database


def test_user_crud_operations():

    db = Database()

    # --------------------------------------------------
    # 1. INSERT
    # --------------------------------------------------

    inserted = db.execute_update(
        """
        INSERT INTO users
        (id, first_name, last_name, email)
        VALUES (?, ?, ?, ?)
        """,
        (10, "Test", "User", "test.user@example.com")
    )

    print("Rows inserted:", inserted)

    assert inserted == 1


    # --------------------------------------------------
    # 2. SELECT
    # --------------------------------------------------

    result = db.execute_query(
        """
        SELECT id, first_name, last_name, email
        FROM users
        WHERE id = ?
        """,
        (10,)
    )

    print("After INSERT:", result)

    assert len(result) == 1

    assert result[0][0] == 10
    assert result[0][1] == "Test"
    assert result[0][2] == "User"
    assert result[0][3] == "test.user@example.com"


    # --------------------------------------------------
    # 3. UPDATE
    # --------------------------------------------------

    updated = db.execute_update(
        """
        UPDATE users
        SET first_name = ?
        WHERE id = ?
        """,
        ("Updated", 10)
    )

    print("Rows updated:", updated)

    assert updated == 1


    # Verify UPDATE

    result = db.execute_query(
        """
        SELECT first_name
        FROM users
        WHERE id = ?
        """,
        (10,)
    )

    print("After UPDATE:", result)

    assert result[0][0] == "Updated"


    # --------------------------------------------------
    # 4. DELETE
    # --------------------------------------------------

    deleted = db.execute_update(
        """
        DELETE FROM users
        WHERE id = ?
        """,
        (10,)
    )

    print("Rows deleted:", deleted)

    assert deleted == 1


    # --------------------------------------------------
    # 5. Verify DELETE
    # --------------------------------------------------

    result = db.execute_query(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (10,)
    )

    print("After DELETE:", result)

    assert len(result) == 0


    # --------------------------------------------------
    # Close DB connection
    # --------------------------------------------------

    db.close()