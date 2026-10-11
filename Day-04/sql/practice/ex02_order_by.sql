-- Exercise 02 -- ORDER BY  (Practice Lab)

-- Top 5 boro transaction
SELECT * FROM transactions ORDER BY amount DESC LIMIT 5;

-- Top 5 choto transaction (amount thaka lagbe, tai NULL bad)
SELECT * FROM transactions WHERE amount IS NOT NULL ORDER BY amount ASC LIMIT 5;

-- Date onujayi sort
SELECT * FROM transactions ORDER BY date;