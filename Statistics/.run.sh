#bin/bash
function stat() {
    echo "Please choose an option:"
    echo "1. Binomial calculation"
    echo "2. Permutation or combination calculation"
    echo "3. Poisson"
    
    # Solicita a entrada do usuário
    echo -n "Enter your choice (1 or 3): "
    read choice

    case "$choice" in
        1)
            python3 binomial.py
            ;;
        2)
            python3 counting.py
            ;;
        3)
            python3 poisson.py
            ;;
        *)
            echo "Invalid choice. Please enter 1 or 2."
            ;;
    esac
}

# function stat() {
#     echo "Please choose an option:"
#     echo "1. Binomial calculation"
#     echo "2. Permutation or combination calculation"

#     read -p "Enter your choice (1 or 2): " choice
#     case "$choice" in
#         bin)
#             python3 binomial.py
#             ;;
#         prob)
#             python3 prob.py
#             ;;
#         *)
#             echo "Usage: stat {bin|com}"
#             echo ""
#             echo "Available options:"
#             echo "  bin  = Binomial calculation"
#             echo "  com  = Permutation or combination calculation"
#             ;;
#     esac
# }

