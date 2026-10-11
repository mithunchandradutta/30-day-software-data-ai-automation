-- Month-wise summary (? jaygay period boshe, jemon '2026-09')
SELECT category, type, SUM(ABS(amount)), COUNT(*)
FROM transactions
WHERE strftime('%Y-%m', date) = ?
GROUP BY category, type
ORDER BY type DESC, SUM(ABS(amount)) DESC;
