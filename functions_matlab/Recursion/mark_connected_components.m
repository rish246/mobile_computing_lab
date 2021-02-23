function [input_array, nth_component] = mark_connected_components(input_array)
    
    [n_rows, n_cols] = size(input_array);
    
    %%% Construct the resultant array
    nth_component = -1;
    
    for row = 1 : n_rows
        
        for col = 1 : n_cols
            
            cur_cell = input_array(row, col);
            
            if (cur_cell == 1)
               input_array = mark(input_array, row, col, nth_component);
               nth_component = nth_component - 1;
            end
            
        end
        
    end
            
    

end


function input_array = mark(input_array, row, col, value)
    % Run dfs
    [n_rows, n_cols] = size(input_array);
    
    fprintf("In Mark Function ");
    
    if ((row < 1) || (row > n_rows) || (col < 1) || (col > n_cols))
        fprintf("Coordinates : (%d, %d) are not in range\n", row, col);
        
    elseif(input_array(row, col) == 1)
        disp([row, col]);
        input_array(row, col) = value;
    
        % Mark the four neighbours of the current matrix
        neighbours_x = [row, row,       row + 1, row - 1];
        neighbours_y = [col + 1, col - 1, col,   col];
        
        for i = 1 : 4
            input_array = mark(input_array, neighbours_x(i), neighbours_y(i), value);
        end
    end    
end
