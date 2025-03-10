from souvenir_python import parse_id, parse_uuid, random_id, zero_id


class Test:
    @staticmethod
    def prefix() -> str:
        return "u"


def test_zero_id():
    id = zero_id(Test)
    expected = "u_00000000000000000000000000"
    assert str(id) == expected


def test_bytes():
    id = parse_id(Test, "u_3456789abc0000123456789abc")

    data = bytes(
        [
            0x64,
            0x29,
            0x8E,
            0x84,
            0xA9,
            0x6C,
            0x00,
            0x00,
            0x00,
            0x88,
            0x64,
            0x29,
            0x8E,
            0x84,
            0xA9,
            0x6C,
        ]
    )

    assert id.bytes() == data

    id = parse_id(Test, "u_7zzzzzzzzzzzzzzzzzzzzzzzzz")
    data = bytes(
        [
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
            0xFF,
        ]
    )

    assert id.bytes() == data


def test_round_trip():
    for _ in range(1_000_000):
        id = random_id(Test)
        id_str = id.__str__()
        id2 = parse_id(Test, id_str)
        assert id.bytes() == id2.bytes()

        uuid = id.uuid()
        id3 = parse_uuid(Test, uuid)
        assert id.bytes() == id3.bytes()
