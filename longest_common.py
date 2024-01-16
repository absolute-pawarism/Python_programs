def l_c_s(str1, str2):
    m, n = len(str1), len(str2)


    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    max_length = 0
    end_position = 0


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

                
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i
            else:
                dp[i][j] = 0

    l_c_s = str1[end_position - max_length:end_position]

    return l_c_s


str1 = "ABABC"
str2 = "BABCAC"
result = l_c_s(str1, str2)

print(f"The longest common substring is: {result}")
