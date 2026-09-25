from utils.db_utils import Database
import pytest
@pytest.mark.db
@pytest.mark.regression


def test_user_data_integrity():

    db = Database()

    # --------------------------------------------------
    # 1. Validate total row count
    # --------------------------------------------------

    result = db.execute_query(
        "SELECT COUNT(*) FROM users"
    )

    user_count = result[0][0]

    print("Total users:", user_count)

    assert user_count == 3


    # --------------------------------------------------
    # 2. Validate required fields
    # --------------------------------------------------

    result = db.execute_query(
        """
        SELECT id, first_name, last_name, email
        FROM users
        """
    )

    print("All users:", result)

    assert len(result) == 3


    for user in result:

        user_id = user[0]
        first_name = user[1]
        last_name = user[2]
        email = user[3]

        print(
            f"Validating user: "
            f"{user_id}, {first_name}, {last_name}, {email}"
        )

        assert user_id is not None
        assert first_name is not None
        assert last_name is not None
        assert email is not None

        assert first_name != ""
        assert last_name != ""
        assert email != ""

        assert "@" in email


    # --------------------------------------------------
    # 3. Validate specific business data
    # --------------------------------------------------

    result = db.execute_query(
        """
        SELECT first_name, last_name, email
        FROM users
        WHERE id = ?
        """,
        (2,)
    )

    print("User ID 2:", result)

    assert len(result) == 1

    assert result[0][0] == "Janet"
    assert result[0][1] == "Weaver"
    assert result[0][2] == "janet@reqres.in"


    # --------------------------------------------------
    # 4. Close database
    # --------------------------------------------------

    db.close()