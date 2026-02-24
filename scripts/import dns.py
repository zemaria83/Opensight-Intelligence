import dns.resolver
r = dns.resolver.Resolver()
r.nameservers = ["1.1.1.1"]
print(r.resolve("www.google.com", "A"))