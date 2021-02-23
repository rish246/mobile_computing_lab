function fib_n = fibbo(n)
    if n <= 2
        fib_n = n;
    else
        fib_n = fibbo(n - 1) + fibbo(n - 2);
        
    end

end
