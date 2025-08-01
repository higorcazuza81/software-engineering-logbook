# Demonstrate stripping whitespace from a string using .lstrip(), .rstrip(), and .strip().

name = " \t Higor Cazuza \t"

# The repr() function is used to inspect the raw string, revealing escape characters for debugging.
print(f"Variável original: {repr(name)}")

print(f"Result of .lstrip(): {repr(name.lstrip())}")
print(f"Result of .rstrip(): {repr(name.rstrip())}")
print(f"Result of .strip(): {repr(name.strip())}")
