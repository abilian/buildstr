from buildstr import Builder


# Tests
def test_simple_builder():
    b = Builder()
    b << "A"
    assert b.build() == "A"


def test_simple_builder_2():
    b = Builder()
    b << "A"
    b << "B"

    assert b.build() == "A B"


def test_simple_builder_3():
    b = Builder("A")
    b << "B"

    assert b.build() == "A B"


def test_chaining():
    b = Builder()
    b << "A" << "B" << "C"

    assert b.build() == "A B C"


def test_convenience_methods():
    b = Builder(separator="")
    b << "A"
    b.nl()
    b << "B"

    assert b.build() == "A\nB"


def test_sub_builder():
    b = Builder()
    b << "A"
    b1 = b(surround=("{ ", " }"), separator="; ")
    b1 << ["a", "b", "c"]

    assert b.build() == "A { a; b; c }"


def test_sub_builder_ilshift():
    b = Builder()
    b <<= "A"
    b1 = b(surround=("{ ", " }"), separator="; ")
    b1 <<= ["a", "b", "c"]

    assert b.build() == "A { a; b; c }"


def test_sub_builder_with_args():
    b = Builder()
    b << "A"
    b1 = b("aa", "bb", surround=("{ ", " }"), separator="; ")
    b1 << ["a", "b", "c"]

    assert b.build() == "A { aa; bb; a; b; c }"


def test_context_manager():
    b = Builder()
    b << "A"
    with b(surround=("{ ", " }"), separator="; "):
        b << ["a", "b", "c"]

    assert b.build() == "A { a; b; c }"


def test_multiple_context_managers():
    b = Builder()
    b << "A"
    with b(name="sub1", surround=("{ ", " }"), separator="; "):
        b << ["a", "b", "c"]

        with b(name="sub2", surround=("(", ")"), separator=", "):
            b << ["x", "y", "z"]

        b << "d"

    assert b.build() == "A { a; b; c; (x, y, z); d }"


def test_context_manager_alt():
    b = Builder()
    b << "A"
    with b(surround=("{ ", " }"), separator="; ") as b1:
        b1 << ["a", "b", "c"]

    assert b.build() == "A { a; b; c }"


def test_multiple_context_managers_alt():
    b = Builder()
    b << "A"
    with b(surround=("{ ", " }"), separator="; ") as b1:
        b1 << ["a", "b", "c"]

        with b(surround=("(", ")"), separator=", ") as b2:
            b2 << ["x", "y", "z"]

        b1 << "d"

    assert b.build() == "A { a; b; c; (x, y, z); d }"
