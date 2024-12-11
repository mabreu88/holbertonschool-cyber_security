def prime(number)
    for x in 2..number
        if number % x == 0
            if x == number
                return true
            else
                return false
            end
        end
    end
end