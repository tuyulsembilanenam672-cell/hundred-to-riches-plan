"""Write the $100-to-riches plan to /output/entry.txt.

Plan: find Shopify stores with broken checkouts, prove the lost sale
with a screenshot, and sell a $49 fix-in-24h, paid by Stripe link.
"""

import os

ENTRY = (
    "Find Shopify stores with broken checkouts via BuiltWith, "
    "screenshot the failure, email owners a $49 fix-in-24h offer "
    "paid by Stripe link. Fix it with Playwright scripts, reinvest "
    "in outreach. Edge: you sell a proven lost sale, not a pitch. "
    "Expect ~$600 in 30 days."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} code points)")


if __name__ == "__main__":
    main()
