import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_kit(kit_body)
    assert user_response.status_code == 201
    assert user_response.json()["name"] == kit_body["name"]

def test_create_user_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_create_user_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_kit(kit_body)
    assert response.status_code == 400

def test_create_user_empty_first_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_no_name(kit_body)

def test_create_user_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_no_name(kit_body)

def test_create_user_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_user_has_space_in_name_get_success_response():
    positive_assert("A Aaa")

def test_create_user_has_number_in_name_get_success_response():
    positive_assert("123")

def test_create_user_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

def test_create_user_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_kit(kit_body)
    assert response.status_code == 400