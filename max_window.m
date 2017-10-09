function input = max_window(input)
    max_val = max(max(input));
    less_than = (input < max_val);
    input(less_than) = 0;

    pullover
    