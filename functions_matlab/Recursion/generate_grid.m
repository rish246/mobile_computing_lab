function grid = generate_grid(n_rows, n_cols)
    grid(n_rows, n_cols) = '.';
    
    for i = 1:n_rows
        
        for j = 1:n_cols
            
            random_toss = rand();
            
            if random_toss < 0.7
                
                grid(i, j) = '.';
                
            else
                grid(i, j) = 'X';
                
            end
        end
        
    end
    
    grid(n_rows, n_cols) = '.';

end