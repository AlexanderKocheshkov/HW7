def password_checker(password):
    """
    Checking if password matches requirements
    """
    ch_l_reg = "password"
    ch_u_reg = "PASSWORD"
    if len(password) >= 6:
        if password.isdigit() == False:
            if (password.find(ch_l_reg) == -1) 
                and (password.find(ch_u_reg) == -1):
                dig_counter = 0
                for x in password:
                    if x.isdigit() == True:
                        dig_counter += 1
                if dig_counter >= 1:
                    return True
                else: 
                    return False
            else: 
                    return False
        else: 
                    return False
    else: 
                    return False

print("Введите пароль: ", end="")
user_password = input()
if password_checker(user_password) == True:
    print("Пароль задан успешно!")
else:
    print("Пароль не подходит!")

