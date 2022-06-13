from Domino import DominoAlgorithm, BackwardDominoAlgorithm


def test_domino_algorithm():
    domino = DominoAlgorithm("||//||\||/\|", 1)
    expected = "||///\\\||/\|"
    assert domino == expected


def test_backward_domino_algorithm():
    domino = BackwardDominoAlgorithm("////|||\\\\\\",2)
    expected = "//|||||||\\"
    assert domino == expected
