def process_emails(email_list):
    # a) Filter valid emails using filter() and lambda
    valid_emails = list(filter(lambda e: '@' in e and (e.endswith('.com') or e.endswith('.org')), email_list))

    # b) Extract domain names using list comprehension
    domains = [email.split('@')[1].split('.')[0] for email in valid_emails]

    # c) Construct domain frequency dictionary using dictionary comprehension
    domain_freq = {domain: domains.count(domain) for domain in set(domains)}

    # Display results
    print("✅ Valid Emails:", valid_emails)
    print("📦 Domains:", domains)
    print("📊 Domain Frequency:")
    for domain, count in domain_freq.items():
        print(f"  {domain}: {count}")

# Example input
emails = ["test@gmail.com", "hello123", "abc.org", "world@yahoo.com"]
process_emails(emails)