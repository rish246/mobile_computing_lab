n_tests = 10;

for i = 1:n_tests
    
    grid_rows = randi(5, 1) + 5;
    
    grid_cols = randi(5, 1) + 5;
    
    
    grid = generate_grid(grid_rows, grid_cols);
    
    visited = zeros(grid_rows, grid_cols);
    
    [updated_grid, is_path] = find_path(grid, 1, 1, visited);
    
    if is_path
        updated_grid
    end
end