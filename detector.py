import re

def detect_scam(text):

    score = 0
    found_words = []
    emails = []

    # Detect emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    found_emails = re.findall(email_pattern, text)

    # Suspicious public email domains
    suspicious_domains = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com"
    ]

    # Trusted company domains
    trusted_domains = [
        "tcs.com",
        "infosys.com",
        "wipro.com",
        "google.com",
        "microsoft.com",
        "amazon.com",
        "accenture.com",
        "ibm.com",
        "oracle.com",
        "capgemini.com"
    ]

    # Check emails
    for email in found_emails:

        emails.append(email)

        domain = email.split("@")[1].lower()

        # Public email providers
        if domain in suspicious_domains:

            score += 10

            found_words.append("Suspicious public email detected")

        # Unknown company domain
        elif domain not in trusted_domains:

            score += 15

            found_words.append("Unverified company domain")

    # Convert score into percentage
    percentage = min(score * 5, 100)

    # Final result
    if score >= 20:

        final_result = "Scam Job"

    elif score >= 10:

        final_result = "Suspicious Job Post"

    else:

        final_result = "Real Job"

        percentage = max(15, percentage)

    # Return output
    return {

        "result": final_result,
        "percentage": percentage,
        "score": score,
        "emails": emails,
        "warnings": found_words

    }