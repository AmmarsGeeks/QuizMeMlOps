def test_data_loading():
    data = load_data()
    assert len(data) > 0