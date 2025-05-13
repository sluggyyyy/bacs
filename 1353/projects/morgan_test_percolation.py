from morgan_percolation import Forest

def test_breadth_first_search_success():
    forest = Forest(3, 3, 0)
    forest.forest = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
    result = forest.breadth_first_search()
    assert result == True


def test_breadth_first_search_failure():
    forest = Forest(3, 3, 0)
    forest.forest = [[1, 0, 0], [0, 0, 0], [1, 0, 0]]
    result = forest.breadth_first_search()
    assert result == False


def test_depth_first_search_success():
    forest = Forest(3, 3, 0)
    forest.forest = [[0, 1, 0],[0, 1, 0], [0, 1, 0]]
    result = forest.depth_first_search()
    assert result == True


def test_depth_first_search_failure():
    forest = Forest(3, 3, 0)
    forest.forest = [[0, 1, 0], [0, 0, 0],[0, 1, 0]]
    result = forest.depth_first_search()
    assert result == False