import random

import pandas as pd


random.seed(42)

months = [202601, 202602, 202603, 202604, 202605, 202606]
programs = ["Medicare", "Medicaid", "Commercial"]
categories = ["Clinical DRG", "Technical/Coding", "Coordination of Benefits", "Data Mining"]

inflow_channels = ["Provider Referral", "Data Mining", "Hotline", "Random Sample"]
inscope_channels = ["In Scope", "Out of Scope"]
initial_selection_channels = ["Manual", "Query", "Experimental"]
final_selection_channels = ["Clinical Review", "Coding Review"]
approval_channels = ["Approved", "Rejected", "Pending"]
audit_channels = ["Desk Audit", "Field Audit", "Automated Review"]
finding_channels = ["Overpayment", "No Finding", "Documentation Error"]

link_plan = [
    ("Inflow", inflow_channels, "Inscope", inscope_channels),
    ("Inscope", ["In Scope"], "Initial Selection", initial_selection_channels),
    ("Initial Selection", initial_selection_channels, "Final Selection", final_selection_channels),
    ("Final Selection", final_selection_channels, "Approval", approval_channels),
    ("Approval", ["Approved"], "Audit", audit_channels),
    ("Audit", audit_channels, "Finding", finding_channels),
]


def weighted_choice(options):
    labels, weights = zip(*options)
    return random.choices(labels, weights=weights, k=1)[0]


def choose_link():
    from_step, from_channels, to_step, to_channels = random.choice(link_plan)
    from_channel = random.choice(from_channels)

    if to_step == "Inscope":
        to_channel = weighted_choice([("In Scope", 0.82), ("Out of Scope", 0.18)])
    elif to_step == "Initial Selection":
        to_channel = weighted_choice([("Manual", 0.42), ("Query", 0.38), ("Experimental", 0.20)])
    elif to_step == "Final Selection":
        # Both initial paths intentionally cross into both final review channels.
        if from_channel == "Manual":
            to_channel = weighted_choice([("Clinical Review", 0.62), ("Coding Review", 0.38)])
        elif from_channel == "Query":
            to_channel = weighted_choice([("Clinical Review", 0.44), ("Coding Review", 0.56)])
        else:
            to_channel = weighted_choice([("Clinical Review", 0.52), ("Coding Review", 0.48)])
    elif to_step == "Approval":
        to_channel = weighted_choice([("Approved", 0.78), ("Rejected", 0.14), ("Pending", 0.08)])
    elif to_step == "Audit":
        to_channel = weighted_choice([("Desk Audit", 0.48), ("Field Audit", 0.24), ("Automated Review", 0.28)])
    elif to_step == "Finding":
        to_channel = weighted_choice([("Overpayment", 0.24), ("No Finding", 0.61), ("Documentation Error", 0.15)])
    else:
        to_channel = random.choice(to_channels)

    return from_step, from_channel, to_step, to_channel


rows = []

for _ in range(5000):
    month = random.choice(months)
    program = random.choice(programs)
    category = random.choice(categories)
    from_step, from_channel, to_step, to_channel = choose_link()

    base_volume = random.randint(25, 240)
    stage_factor = {
        "Inflow": 1.00,
        "Inscope": 0.72,
        "Initial Selection": 0.34,
        "Final Selection": 0.27,
        "Approval": 0.22,
        "Audit": 0.18,
    }[from_step]
    category_factor = {
        "Clinical DRG": 1.15,
        "Technical/Coding": 1.05,
        "Coordination of Benefits": 0.88,
        "Data Mining": 0.96,
    }[category]
    program_factor = {"Medicare": 1.12, "Medicaid": 0.96, "Commercial": 0.92}[program]

    claim_count = max(1, int(base_volume * stage_factor * category_factor * program_factor))
    paid_amount = claim_count * random.randint(1600, 9500)

    overpayment_identified = 0
    if to_step == "Finding" and to_channel == "Overpayment":
        overpayment_identified = int(paid_amount * random.uniform(0.08, 0.28))

    rows.append(
        {
            "month": month,
            "Program": program,
            "Category": category,
            "from_step": from_step,
            "from_channel": from_channel,
            "to_step": to_step,
            "to_channel": to_channel,
            "claim_count": claim_count,
            "paid_amount": paid_amount,
            "overpayment_identified": overpayment_identified,
        }
    )


df = pd.DataFrame(rows)
df.to_csv("payment_integrity_5000.csv", index=False)
print("File 'payment_integrity_5000.csv' has been generated with 5,000 Sankey link rows.")
