from app.security.password import hash_password, verify_password


def test_hash_password_returns_different_value():
    raw_password = "mypassword123"
    hashed_password = hash_password(raw_password)

    assert hashed_password != raw_password


def test_verify_password_returns_true_for_correct_password():
    raw_password = "mypassword123"
    hashed_password = hash_password(raw_password)

    assert verify_password(raw_password, hashed_password) is True


def test_verify_password_returns_false_for_wrong_password():
    raw_password = "mypassword123"
    hashed_password = hash_password(raw_password)

    assert verify_password("wrongpassword", hashed_password) is False