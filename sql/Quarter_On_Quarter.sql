WITH qoq AS (
	SELECT 
		quarterly,
        Online_marketing_services_and_others,
		((Online_marketing_services_and_others - 
			LAG(Online_marketing_services_and_others,1) 
				OVER (ORDER BY quarterly ASC))
			/LAG(Online_marketing_services_and_others,1)
				OVER (ORDER BY quarterly ASC) * 100) AS qoqr
		FROM temu
)

SELECT * FROM qoq;
