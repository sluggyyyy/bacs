from projects.morgan_project3part2_sandgame import *
import random
def test_create_world():
    w = create_world(10)
    assert len(w) == 10, "Create world, wrong number of rows"
    for row in w:
        assert len(row) == 10, "Create world, wrong number of columns"
    for row in w:
        for cell in row:
            assert cell == 'EMPTY', "Create world, each cell should start empty"
    
if __name__=="__main__":
    test_create_world()
    # Try the first test, then comment it out and try the second:
    # test_draw_world_1()
    # test_draw_world_2()
