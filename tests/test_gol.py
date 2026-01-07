from Game_Of_Life_Return.main import count_neightbor
from Game_Of_Life_Return.main import next_generation
def test_oneofmanytest():
    
    grid=[[1,0,1],
          [0,1,1],
          [1,1,1]]
    
    row = 3 
    col = 3

    assert count_neightbor(grid , 0,0,3,3 )==1
    assert count_neightbor(grid , 0,1,3,3 )==4
    assert count_neightbor(grid , 0,2,3,3 )==2
    assert count_neightbor(grid , 1,0,3,3 )==4
    assert count_neightbor(grid , 1,1,3,3 )==6
    assert count_neightbor(grid , 1,2,3,3 )==4
    assert count_neightbor(grid , 2,0,3,3 )==2
    assert count_neightbor(grid , 2,1,3,3 )==4
    assert count_neightbor(grid , 2,2,3,3 )==3

    new_grid=[[0,0,1],
              [0,0,0],
              [1,0,1]]

    assert next_generation(grid , 3 , 3)== new_grid