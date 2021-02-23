function input_matrix = flood_fill(input_matrix, clicked_row, clicked_col)
    %%% Basically Fill the entire color in all the neighbours of the image
    
    % chose its 8 neighbours
    % If the color of the cell is not boundary cell
    % Change the color of cell to current cell's data
    color_to_fill = input_matrix(clicked_row, clicked_col);
    
    input_matrix = fill_color(input_matrix, clicked_row, clicked_col, color_to_fill);
    
    

end


function input_matrix = fill_color(input_matrix, row, col, color)
    
    are_valid_coords = are_valid(input_matrix, row, col);
    
    fprintf("(%d, %d)\n", row, col);
    
    if (are_valid_coords)
        % start filling the color
        input_matrix(row, col) = color;
        
        % FILL COLOR IN NEIGHBOURS
        neighbours_x = [row, row    , row+1, row-1, row+1, row+1, row-1, row-1];
        neighbours_y = [col+1, col-1, col  , col , col+1, col-1, col+1, col-1];
        
        for i_neighbour = 1 : 8
            
            cur_neighbour_x = neighbours_x(i_neighbour);
            cur_neighbour_y = neighbours_y(i_neighbour);
            
            is_valid_neighbour = are_valid(input_matrix, cur_neighbour_x, cur_neighbour_y);
            
            if (is_valid_neighbour)
                % find the color of neighbour
                neighbour_color = input_matrix(cur_neighbour_x, cur_neighbour_y);
                
                if (neighbour_color ~= color)
                    % FIll the current neighbour
                    input_matrix = fill_color(input_matrix, neighbours_x(i_neighbour), neighbours_y(i_neighbour), color);
                end
            end
            
            
        end
        
    end

end


function result = are_valid(matrix, row, col)
    
    [n_rows, n_cols] = size(matrix);
    
    result = true;
    
    if ( (row < 1) || (row > n_rows) || (col < 1) || (col > n_cols))
        result = false;
        
    elseif (matrix(row, col) == 0)
        result = false;
    end
    

end