# Write a program to partition a user-generated URL string into protocol, domain, and path using both methods. Also, modify the program to extract the top-level domain (TLD) from the domain.
user_input = input("Enter a URL: ")

protocol, separator1, domain_and_path = user_input.partition("://")
domain, separator2, path = domain_and_path.rpartition("/")
tld = domain.split(".")[-1]

print("Protocol:", protocol)
print("Domain:", domain)
print("Top-level domain:", tld)
print("Path:", path)
