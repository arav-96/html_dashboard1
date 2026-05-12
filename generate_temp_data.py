import random

import pandas as pd


random.seed(42)

clients = ["HUMANA", "UHCCOSMOS", "AETNA", "BCBS"]
function_profiles = {
    "Cod_No_Review": {"selected": (0.94, 0.99), "approved": (0.28, 0.42), "finding": (0.07, 0.16)},
    "Cod_Review": {"selected": (0.08, 0.16), "approved": (0.52, 0.68), "finding": (0.08, 0.18)},
    "CVA_No_Review": {"selected": (0.96, 1.00), "approved": (0.26, 0.38), "finding": (0.12, 0.24)},
    "CVA_Review": {"selected": (0.28, 0.40), "approved": (0.56, 0.70), "finding": (0.07, 0.15)},
    "CVA_Review2": {"selected": (0.92, 0.99), "approved": (0.24, 0.34), "finding": (0.10, 0.18)},
    "Deselect": {"selected": (0.10, 0.15), "approved": (0.88, 1.00), "finding": (0.01, 0.04)},
    "NoReview": {"selected": (0.32, 0.45), "approved": (0.24, 0.34), "finding": (0.20, 0.36)},
}
category_1_values = [
    "COD MODEL ONLY",
    "COD RULES & MODEL",
    "COD RULES ONLY",
    "CVA MODEL ONLY",
    "CVA RULES & MODEL",
    "CVA RULES ONLY",
    "MANUAL",
    "MODEL PRIORATIZED",
    "NULL",
]
category_report_values = ["CVA", "DRG", "COD", "null"]
programs = ["Medicare", "Medicaid", "Commercial", "Exchange"]
subprograms = ["CVA", "DRG", "COD", "null"]
statuses = ["Pending", "Approved", "Closed", "null"]
flow_names = ["Inflow", "Inscope", "Selection", "Approval", "Audit", "Finding"]
loadmonths = [202511, 202512, 202601, 202602, 202603, 202604]
selection_months = [202601, 202602, 202603, 202604, 202605, 202606]


def weighted_choice(options):
    labels, weights = zip(*options)
    return random.choices(labels, weights=weights, k=1)[0]


def derive_name(function_pre, category_1):
    prefix = "CVA" if "CVA" in function_pre or "CVA" in category_1 else "COD"
    suffix = {
        "COD MODEL ONLY": "MODEL",
        "COD RULES & MODEL": "RULE_MODEL",
        "COD RULES ONLY": "RULES",
        "CVA MODEL ONLY": "MODEL",
        "CVA RULES & MODEL": "RULE_MODEL",
        "CVA RULES ONLY": "RULES",
        "MANUAL": "MANUAL",
        "MODEL PRIORATIZED": "MODEL_PRIORITIZED",
        "NULL": "NULL",
    }[category_1]
    return f"{prefix}_{suffix}"


def pick_category_for_function(function_pre):
    if function_pre.startswith("Cod"):
        return weighted_choice([
            ("COD MODEL ONLY", 0.20),
            ("COD RULES & MODEL", 0.32),
            ("COD RULES ONLY", 0.28),
            ("MANUAL", 0.08),
            ("MODEL PRIORATIZED", 0.08),
            ("NULL", 0.04),
        ])
    if function_pre.startswith("CVA"):
        return weighted_choice([
            ("CVA MODEL ONLY", 0.18),
            ("CVA RULES & MODEL", 0.36),
            ("CVA RULES ONLY", 0.30),
            ("MANUAL", 0.06),
            ("MODEL PRIORATIZED", 0.07),
            ("NULL", 0.03),
        ])
    return weighted_choice([(value, 1) for value in category_1_values])


def category_report_for(category_1, function_pre):
    if category_1.startswith("CVA") or function_pre.startswith("CVA"):
        return "CVA"
    if category_1.startswith("COD") or function_pre.startswith("Cod"):
        return "COD"
    if function_pre == "NoReview":
        return weighted_choice([("CVA", 0.45), ("DRG", 0.45), ("null", 0.10)])
    return weighted_choice([("CVA", 0.30), ("DRG", 0.35), ("COD", 0.25), ("null", 0.10)])


rows = []

for _ in range(5000):
    function_pre = weighted_choice([
        ("Cod_No_Review", 0.13),
        ("Cod_Review", 0.18),
        ("CVA_No_Review", 0.15),
        ("CVA_Review", 0.08),
        ("CVA_Review2", 0.08),
        ("Deselect", 0.18),
        ("NoReview", 0.20),
    ])
    profile = function_profiles[function_pre]
    category_1 = pick_category_for_function(function_pre)
    category_report = category_report_for(category_1, function_pre)
    category_insight = "CVA" if category_report == "CVA" else "COD" if category_report == "COD" else category_report

    claims = random.randint(1, 90)
    inflow = claims
    inscope = claims
    if function_pre == "Deselect":
        inscope = int(claims * random.uniform(0.02, 0.10))
    elif category_1 == "NULL" or category_report == "null":
        inscope = int(claims * random.uniform(0.00, 0.15))

    selected = int(inscope * random.uniform(*profile["selected"]))
    if function_pre == "Deselect" and inscope > 0:
        selected = max(1, selected)

    approved = int(selected * random.uniform(*profile["approved"]))
    if function_pre == "Deselect" and selected > 0:
        approved = max(1, approved)
    audit = int(approved * random.uniform(0.76, 0.98))
    finding = int(audit * random.uniform(*profile["finding"]))
    no_finding = max(0, audit - finding - random.randint(0, max(0, int(audit * 0.08))))
    exl_savings = round(finding * random.uniform(1200, 9000), 2)

    client = weighted_choice([("HUMANA", 0.55), ("UHCCOSMOS", 0.25), ("AETNA", 0.12), ("BCBS", 0.08)])
    subprogramtype = category_report if category_report in ["CVA", "DRG", "COD"] else weighted_choice([(value, 1) for value in subprograms])
    status = weighted_choice([("Pending", 0.54), ("Approved", 0.18), ("Closed", 0.22), ("null", 0.06)])
    cat_flag = 1 if finding > 0 else 0

    rows.append(
        {
            "client": client,
            "function_pre": function_pre,
            "name": derive_name(function_pre, category_1),
            "loadmonth": random.choice(loadmonths),
            "selection_month": random.choice(selection_months),
            "status": status,
            "subprogramtype": subprogramtype,
            "program": random.choice(programs),
            "flowname": random.choice(flow_names),
            "category": category_report,
            "category_1": category_1,
            "category_report": category_report,
            "cat_flag": cat_flag,
            "category_insight": category_insight,
            "claims": claims,
            "inflow": inflow,
            "inscope": inscope,
            "selected": selected,
            "approved": approved,
            "audit": audit,
            "finding": finding,
            "no_finding": no_finding,
            "exl_savings": exl_savings,
            "overpayment_identified": exl_savings,
        }
    )


df = pd.DataFrame(rows)
df.to_csv("payment_integrity_5000.csv", index=False)
print("File 'payment_integrity_5000.csv' has been generated with 5,000 pivot-style rows.")
