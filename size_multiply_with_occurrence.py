'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t, z):
    max_value = -1  # En yüksek değeri -1'e eşitledik

    # t'nin alt dizileri iterasyonu
    for i in range(len(t)):
        for j in range(i + 1, len(t) + 1):
            substring = t[i:j] 

            # Alt dizilerin z'de kaç tane olduğunu bulmak için
            count = z.count(substring)

            # Alt dizilerin uzunluğu ve hesapladığımız z miktarını çarptık
            product = len(substring) * count

            # Bulduğumuz sonuç eğer daha fazlaysa maksimum değeri güncellemek için
            if product > max_value:
                max_value = product

    return max_value

if __name__ == '__main__':
    result = find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print("The maximum value is:", result)
