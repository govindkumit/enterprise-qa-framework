from utils.db_utils import Database


def test_user_exists_in_database():

    db = Database()

    result = db.execute_query(
        "SELECT * FROM users WHERE id = ?",
        (1,)
    )

    print("Database result:", result)

    assert len(result) == 1

    assert result[0][1] == "George"
    assert result[0][2] == "Bluth"
    assert result[0][3] == "george@reqres.in"

    db.close()