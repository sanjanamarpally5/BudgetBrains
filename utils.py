# utils.py - helpers for budget calculation, summarization, demographic adaptation
import pandas as pd
from typing import Dict, Any




def detect_user_demographic(profile: Dict[str, Any]) -> str:
"""Very small heuristic: expect profile to contain 'age' and 'occupation'.
Returns 'student' or 'professional'.
"""
age = profile.get("age")
occ = profile.get("occupation", "").lower()
if occ and "student" in occ:
return "student"
try:
if age is not None and int(age) < 25:
return "student"
except Exception:
pass
return "professional"




def create_budget_summary(transactions: pd.DataFrame) -> Dict[str, Any]:
# transactions: columns = [date, category, amount]
summary = transactions.groupby("category").amount.sum().sort_values(ascending=False)
total = transactions.amount.sum()
pct = (summary / total * 100).round(2).to_dict()
return {"total": float(total), "by_category": pct}