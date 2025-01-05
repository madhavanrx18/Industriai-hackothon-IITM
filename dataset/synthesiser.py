import csv
import random
from datetime import datetime
from collections import defaultdict

# Function to generate synthetic dataset
def generate_synthetic_dataset_csv(filename, num_records=1000):
    # Updated roles
    roles = ['sys_admin', 'software_dev', 'bank_manager', 'bank_clerk', 'consumer']
    
    # Predefined file paths
    file_paths = [
        '/cloud/finance/investments/2020/02/version_1/priority_1/transactions_95787.csv',
        '/cloud/finance/budget/2021/03/version_2/priority_2/transactions_48291.csv',
        '/cloud/finance/reports/2020/06/version_1/priority_3/audit_56734.csv',
        '/cloud/operations/logistics/2022/01/version_1/priority_4/shipment_83473.csv',
        '/cloud/finance/investments/2021/04/version_3/priority_1/transactions_45367.csv',
        '/cloud/finance/reports/2021/02/version_2/priority_3/quarterly_83956.csv',
        '/cloud/operations/logistics/2023/03/version_4/priority_2/shipment_47619.csv',
        '/cloud/hr/employee_data/2020/12/version_2/priority_1/employees_19374.csv',
        '/cloud/it/security/2021/05/version_1/priority_3/logs_38492.csv',
        '/cloud/marketing/ad_campaigns/2021/11/version_5/priority_1/ad_data_75829.csv',
        '/cloud/sales/transactions/2022/07/version_3/priority_2/sales_data_18265.csv',
        '/cloud/finance/tax/2021/01/version_2/priority_4/tax_reports_23948.csv',
        '/cloud/finance/budget/2022/09/version_3/priority_1/forecast_19384.csv',
        '/cloud/operations/logistics/2022/11/version_2/priority_2/shipment_details_59203.csv',
        '/cloud/hr/employee_data/2021/08/version_2/priority_1/employee_performance_98457.csv',
        '/cloud/it/security/2022/04/version_2/priority_3/security_logs_38273.csv',
        '/cloud/marketing/social_media/2023/09/version_4/priority_2/campaign_metrics_19283.csv',
        '/cloud/sales/transactions/2023/06/version_2/priority_3/customer_purchases_83729.csv',
        '/cloud/finance/forecasting/2022/12/version_1/priority_2/financial_forecast_72918.csv',
        '/cloud/it/maintenance/2021/10/version_5/priority_4/system_logs_17293.csv',
        '/cloud/operations/logistics/2021/05/version_2/priority_1/shipment_invoices_28374.csv',
        '/cloud/finance/investments/2022/01/version_3/priority_1/investment_analysis_94827.csv',
        '/cloud/hr/recruitment/2023/07/version_4/priority_2/job_applications_57392.csv',
        '/cloud/it/deployment/2022/03/version_1/priority_1/deployment_logs_53982.csv',
        '/cloud/marketing/analytics/2022/08/version_3/priority_2/customer_analysis_48192.csv',
        '/cloud/sales/reports/2022/02/version_4/priority_1/sales_performance_73829.csv',
        '/cloud/operations/logistics/2020/09/version_3/priority_2/delivery_schedule_29283.csv',
        '/cloud/hr/employee_data/2022/04/version_2/priority_3/employee_salaries_98234.csv',
        '/cloud/finance/budget/2023/03/version_1/priority_4/expense_report_49384.csv',
        '/cloud/it/security/2022/02/version_4/priority_1/firewall_logs_59382.csv',
        '/cloud/marketing/seo/2023/06/version_5/priority_2/website_traffic_58392.csv',
        '/cloud/finance/reports/2023/05/version_3/priority_1/annual_report_84739.csv'
    ]

    # Create and write CSV data
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        header = [
            "User_ID", "Role", "File_Path", "Behavior_Probability", "Access_Granted"
        ]
        writer.writerow(header)

        # Generate data rows
        for _ in range(num_records):
            user_id = f"UID{random.randint(100000, 999999)}"
            role = random.choice(roles)
            file_path = random.choice(file_paths)
            access_granted = random.choice([True, False])
            
            # Generate behavioral probability
            behavior_probability = round(random.betavariate(2, 5), 2)
            
            # Write row to CSV
            writer.writerow([
                user_id, role, file_path, behavior_probability, access_granted
            ])
    
    print(f"Synthetic dataset generated and saved to '{filename}'")

# Example usage
output_file = "synthetic_data.csv"
generate_synthetic_dataset_csv(output_file, num_records=1000)
