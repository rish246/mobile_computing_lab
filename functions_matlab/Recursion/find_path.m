function [grid, is_path] = find_path(grid, row, col, visited)
    is_path = false;
    grid(1, 1) = '#';
    
    visited(row, col) = 1;
%     fprintf("(%d, %d)\n", row, col);
    
    [n_rows, n_cols] = size(grid);
    
    if (row == n_rows) && (col == n_cols)
        is_path = true;
        return;
    end
    
    
    % Learnt return statement in matlab
    neighbours_x = [row, row, row + 1, row -1];
    neighbours_y = [col - 1, col + 1, col, col];
    
    for i = 1:4
       cur_neighbour_x = neighbours_x(i);
       cur_neighbour_y = neighbours_y(i);
       if are_valid(grid, cur_neighbour_x, cur_neighbour_y) && (grid(cur_neighbour_x, cur_neighbour_y) ~= 'X') && (visited(cur_neighbour_x, cur_neighbour_y) == 0)
           [grid, is_path_from_this_neighbour] = find_path(grid, cur_neighbour_x, cur_neighbour_y, visited);
           is_path = is_path || is_path_from_this_neighbour;
           if is_path
              grid(cur_neighbour_x, cur_neighbour_y) = '#'; 
           end
       end
        
    end

end

%%% Change the characters of the path from '.' to '#'
