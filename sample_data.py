# Sample TM Bill Data for Testing

SAMPLE_BILL_TEXT = """
TM Technology Services Sdn Bhd 200201003726 (571389-H)
Level 51, Menara TM, 50672 Kuala Lumpur

INVOICE
Account No: 7013080234
Bill No: INV2026011313828938
Bill Date: 13 Jan 2026
Credit Limit: RM140.00
Deposit: RM0.00

BILL OVERVIEW RM 126.35

Total Amount Payable

Hello MIOR FARIDHAL AKTRAS BIN MUSTAPA

Remaining balance from previous month RM85.00

CHARGES
This month's charges RM39.00
Service Tax RM2.34
Total charges for this month RM41.34
Rounding Amount RM0.01

Total Amount Payable RM126.35
(Pay immediately to avoid service disruption)
(Pay before 03 Feb 2026)

YOUR DETAILED CHARGES
Account No: 7013080234 Bill Date: 13 Jan 2026

Remaining balance from previous month
Previous Balance - - - 85.00
Total: RM 85.00

This month's charges
Description Gross (RM) Discount (RM) Amount (RM)
Monthly Charges 39.00 39.00
Usage Charges 0.00 0.00
Other Charges 0.00 0.00
Adjustment 0.00 0.00 0.00

Summary Charges
Total: RM 39.00

Tax Summary
Description Total Before Tax Total Tax (RM)
Service Tax - ST 39.00 2.34
Service Tax - NT 0.00 0.00
Service Tax - S8 0.00 0.00
Total: RM 2.34

UNI5G Postpaid 39 Individual
Description Start Date End Date Gross (RM) Discount (RM) Amount (RM)
0126919381
UNI5G Postpaid 39 (ST) 13/01/2026 12/02/2026 39.00 0.00 39.00
Total: RM 39.00

USAGE/PURCHASE HISTORY
Account No: 7013080234 Bill Date: 13 Jan 2026
0126919381

Mobile Calls
Date Time Called to Duration Amount (RM)
13/12/2025 18:09:19 60129322801 00:04:00 0.00
16/12/2025 16:20:08 60132069395 00:00:17 0.00
16/12/2025 17:41:23 60129322801 00:00:21 0.00
16/12/2025 18:25:29 60129322801 00:01:54 0.00
16/12/2025 18:28:59 60129322801 00:00:28 0.00
20/12/2025 16:32:45 601112337286 00:02:17 0.00
31/12/2025 17:35:14 60124867790 00:00:14 0.00
04/01/2026 14:47:08 60126911756 00:00:47 0.00
06/01/2026 16:31:22 601165861674 00:01:01 0.00
Total 0.00

Special Number SMS
Date Time Number Messaged Amount (RM)
24/12/2025 00:30:20 22233 0.00
Total 0.00

Payment Channels
Self-care
• Unifi App
• JomPAY online
Over the Counter
• TM Authorized Dealer (TAD)
• 7-Eleven
• 99 Speedmart
• e-Pay
• ONEPAY (M1)
• POS Malaysia

IMPORTANT NOTICE
BILL PAYMENT
Payment made later than the due date stated on the front page will cause temporary service
disconnection. A reconnection fee of RM10.00 will be charged for service reconnection of each service.
"""

def get_sample_bill():
    """Returns sample bill text for demo purposes"""
    return SAMPLE_BILL_TEXT
