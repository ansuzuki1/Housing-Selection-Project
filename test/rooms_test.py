from app.rooms import fetch_and_filter_rooms

def test_filter_and_fetch_car_barn():
    results = fetch_and_filter_rooms("Car barn")
    assert isinstance(results, list)
    for room_info in results:
        assert isinstance(room_info, dict)       
        for room_id, details in room_info.items():
            assert details.get("view") == "Car Barn"

def test_filter_and_fetch_2br():
    results = fetch_and_filter_rooms("2")
    assert isinstance(results, list)
    for room_info in results:
        assert isinstance(room_info, dict)
        for room_id, details in room_info.items():
            assert str(details.get("beds")) == "2"

