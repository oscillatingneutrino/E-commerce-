

CREATE TABLE temu (
-- Marker is not strictly needed here; it was used as a result of the way that data from Quarterly was written, which caused an
-- ordering issue for formulas in the SQL code in Quarter_On_Quarter
-- That being said, using marker also requires it to be inside of the .csv file, which in this case, it is
Marker INT,
Quarterly TEXT,
Online_marketing_services_and_others INT,
Transaction_Services INT,
sales_and_marketing_expenses INT,
operating_profit INT,
Receivables_from_online_payment_platforms INT,
Prepayments_and_other_current_assets INT,
Cash_and_cash_equivalents INT,
short_term_investments INT,
Net_cash_generated_from_operating_activities INT
);
