from glob_lit import Lit
from glob_either import Either

def test_either_followed_by_literal_match():
    # ⌈{a,b}c⌋ ≈ "ac"
    assert Either(Lit("a"), Lit("b"), Lit("c"))

def test_either_followed_by_literal_no_match():
    # ⌈{a,b}c⌋ ≉ "ax"
    assert not Either(Lit("a"), Lit("b"), Lit("x"))
