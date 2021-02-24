function result = are_valid(matrix, row, col)
    
    [n_rows, n_cols] = size(matrix);
    
    result = true;
    
    if ( (row < 1) || (row > n_rows) || (col < 1) || (col > n_cols))
        result = false;
        
    elseif (matrix(row, col) == 0)
        result = false;
    end
    

end