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

	-- Revenue Based Metrics
	
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
                

-- Metrics for plotting
		Receivables_from_online_payment_platforms, -- plot this against revenue
		
	    Cash_and_cash_equivalents, -- plot this vs revenue
	    
	    short_term_investments, -- plot this vs. quarters
	    
	    Net_cash_generated_from_operating_activities -- plot this vs. quarters
	    
	    
    FROM temu
)

SELECT * FROM qoq
