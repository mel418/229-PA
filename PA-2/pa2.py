""" ----------------- PROBLEM 1 ----------------- """


def primes(a, b):
  """
    prints all primes in the range [a, b]
    """
  if a < 1 or b < a:  # handling invalid range
    raise ValueError("Invalid range given")

  if a == 1:  # handling starting point a = 1
    a = 2  # this ensures 1 is not listed as a prime

  # FIXME: initialize `stop` which is the stopping criteria for
  #        the loop in the Sieve of Eratosthenes
  stop = int(b**(1 / 2)) + 1

  # FIXME: initialize a Python set called `primes` that contains
  #        all integers in the range [a, b]
  P = set(range(a, b + 1))

  for x in range(2, stop):

    # FIXME: use Python list comprehension to create a set
    #        of multiples of x in the range [2, b];
    # HINT: the set of multiples of x can be expressed as
    #       k * x, where k is an integer; hence the comprehension
    #       should loop over values that satisfy k * x <= b
    multiples_x = set(k * x for k in range(2, (b // x) + 1))

    P -= multiples_x  # removing the multiples of x from the set P

  return P


""" ----------------- PROBLEM 2 ----------------- """


def bezout_coeffs(a, b):
  s0 = 1
  t0 = 0
  s1 = -1 * (b // a)
  t1 = 1

  temp = b
  bk = a
  ak = temp % a

  while ak != 0:
    temp_s = s1
    temp_t = t1

    # FIXME: Update s1 according to the formula for sk
    s1 = s0 - (bk // ak) * s1

    # FIXME: Update t1 according to the formula for tk
    t1 = t0 - (bk // ak) * t1

    s0 = temp_s
    t0 = temp_t
    temp = bk

    # FIXME: Update bk and ak
    bk = ak
    ak = temp % ak

  # FIXME: Replace each string with the correct coefficients of a and b
  return {a: s0, b: t0}


""" ----------------- PROBLEM 3 ----------------- """


def gcd(a, b):
  # FIXME: Implement this function
  coeff = bezout_coeffs(a, b)
  coeff_a = coeff[a]
  coeff_b = coeff[b]
  d = abs(coeff_a * a + coeff_b * b)
  return d


# lcm = ((367500 * 43401015) // gcd(367500, 43401015))
# print(primes(2, lcm))

""" ----------------- Quiz 4: Solving Congruences ----------------- """

print(f"gcd: {gcd(53, 3233)}")

''' What is the largest, negative inverse of 97 modulo 3431? '''
gcd_result = gcd(97, 3431)

if gcd_result == 1:
    # Using the Bezout coefficients to find the modular inverse
    bezout_coeffs_result = bezout_coeffs(97, 3431)
    inverse = bezout_coeffs_result[97]

    # Make sure the inverse is negative and within the range [0, 2501)
    while inverse >= 0:
        inverse -= 3431

    print("The largest negative inverse of 97 modulo 3431 is:", inverse)
else:
    print("There is no modular inverse since the GCD is not 1.")


'''
  Find all solutions to the congruence.
  25x ≡ 3 (mod 7)
'''
# Define the given congruence
a = 25
b = 3
modulus = 7

# Calculate the greatest common divisor (GCD) of a and modulus
gcd_result = gcd(a, modulus)

if b % gcd_result == 0:
    # Calculate the modular inverse of 'a' modulo 'modulus'
    modular_inverse = bezout_coeffs(a, modulus)[a]
    # Calculate one solution using the modular inverse
    x = (modular_inverse * (b // gcd_result)) % modulus
    print(f"{x} + {modulus//gcd_result}k")
    # Find all solutions by adding multiples of modulus to the first solution
    solutions = [x + k * (modulus // gcd_result) for k in range(gcd_result)]

    print("All solutions to the congruence {}x ≡ {} (mod {}) are:".format(a, b, modulus))
    print(solutions)
else:
    print("There are no solutions to the congruence since {} is not divisible by the GCD of {} and {}.".format(b, a, modulus))


'''
Suppose you are asked to solve the system,
x=2(mod5)
x=3(mod7)
x=10(mod11)
using Chinese Remainder Theorem.  You form the solution,
y = 2 *M1 * InverseM1 + 3* M2 * InverseM2 + 10*M3 * InverseM3
Identify each value.  Make sure that any inverse value is the smallest positive inverse possible:
'''
# Define the moduli
modulus_1 = 5
modulus_2 = 7
modulus_3 = 11

# Calculate M1, M2, M3
M1 = modulus_2 * modulus_3
M2 = modulus_1 * modulus_3
M3 = modulus_1 * modulus_2

# Calculate the modular inverses and store them in variables without "lineover"
inverse_M1 = bezout_coeffs(M1, modulus_1)[M1]
inverse_M2 = bezout_coeffs(M2, modulus_2)[M2]
inverse_M3 = bezout_coeffs(M3, modulus_3)[M3]

# Ensure that inverses are positive (use modulus if needed)
if inverse_M1 < 0:
    inverse_M1 += modulus_1
if inverse_M2 < 0:
    inverse_M2 += modulus_2
if inverse_M3 < 0:
    inverse_M3 += modulus_3

# Print the values
print("M1 =", M1)
print("M2 =", M2)
print("M3 =", M3)
print("Inverse of M1 =", inverse_M1)
print("Inverse of M2 =", inverse_M2)
print("Inverse of M3 =", inverse_M3)

'''
According to Fermat's Little Theorem, what is the smallest, non-negative integer that is congruent to 3302 under modulo 11?
'''
# Define the values
a = 3
exponent = 302
modulus = 11

# Calculate the smallest non-negative integer congruent to a^exponent (mod modulus)
result = pow(a, exponent % (modulus - 1), modulus)

print("The smallest non-negative integer congruent to 3^302 (mod 11) is:", result)