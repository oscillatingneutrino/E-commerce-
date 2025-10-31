WITH qoq AS (
	SELECT 
		Marker,
		quarterly,
	
        Online_marketing_services_and_others,
	
		((Online_marketing_services_and_others - 
			LAG(Online_marketing_services_and_others,1) 
				OVER (ORDER BY Marker ASC))
			/LAG(Online_marketing_services_and_others,1)
				OVER (ORDER BY Marker ASC) * 100) 
					AS qoqr,

	-- 
	
		Online_marketing_services_and_others + 
			transaction_services 
				AS revenue,
	        
	    100 * (Online_marketing_services_and_others + 
			transaction_services - costs_of_revenues)/ (Online_marketing_services_and_others + transaction_services)
				AS gross_margin,
		
		(Online_marketing_services_and_others + 
			transaction_services)
				/sales_and_marketing_expenses 
					AS marketing_efficiency_ratio,
	                
		100 * operating_profit / 
			(Online_marketing_services_and_others + 
				transaction_services)
					AS operating_margin,
                


		Receivables_from_online_payment_platforms, 
		
	    Cash_and_cash_equivalents,
	    
	    short_term_investments, 
	    
	    Net_cash_generated_from_operating_activities 
	    
	    
    FROM temu
)

SELECT * FROM qoq
