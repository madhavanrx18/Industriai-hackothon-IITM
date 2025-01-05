import csv
import random
from datetime import datetime, timedelta

def generate_folder_description(path_components):
    # Descriptions for root directories
    root_descriptions = {
        'cloud': 'Primary cloud storage for active documents',
        'local': 'Local network storage for immediate access',
        'network': 'Global network shared storage',
        'backup': 'Long-term backup storage location',
        'archive': 'Historical document archive storage'
    }
    
    # Descriptions for departments
    dept_descriptions = {
        'finance': 'Financial department records and documents',
        'hr': 'Human Resources department files',
        'it': 'Information Technology department resources',
        'operations': 'Business operations documentation',
        'legal': 'Legal department documentation'
    }
    
    # Descriptions for subdepartments
    subdept_descriptions = {
        # Finance subdepartments
        'accounting': 'General accounting and bookkeeping records',
        'payroll': 'Employee payroll processing and records',
        'audit': 'Internal and external audit documents',
        'tax': 'Tax documentation and filings',
        'investments': 'Investment records and analysis',
        
        # HR subdepartments
        'recruitment': 'Hiring and recruitment process documents',
        'benefits': 'Employee benefits administration',
        'training': 'Employee training materials and records',
        'personnel': 'Employee personnel files and records',
        'compliance': 'HR compliance and policy documents',
        
        # IT subdepartments
        'infrastructure': 'IT infrastructure documentation',
        'security': 'Security protocols and systems',
        'development': 'Software development projects',
        'support': 'IT support documentation',
        'systems': 'System administration files',
        
        # Operations subdepartments
        'transactions': 'Transaction processing records',
        'customer_service': 'Customer service documentation',
        'risk': 'Risk assessment and management',
        'fraud': 'Fraud detection and prevention',
        'reporting': 'Operational reports and analytics',
        
        # Legal subdepartments
        'contracts': 'Legal contracts and agreements',
        'regulations': 'Regulatory compliance documents',
        'cases': 'Legal case files and documentation',
        'policies': 'Legal policies and procedures',
        'documentation': 'Legal documentation and records'
    }
    
    # Descriptions for special folders
    special_folder_descriptions = {
        'version': 'Version control folder for document revisions',
        'priority': 'Priority-based classification folder',
        'team': 'Team-specific workspace',
        'project': 'Project-specific documentation'
    }
    
    # Build complete path description
    path_desc = []
    
    for component in path_components:
        if component.startswith('/'):
            component = component[1:]
            
        # Root directory description
        if component in root_descriptions:
            path_desc.append(f"[{component}: {root_descriptions[component]}]")
            
        # Department description
        elif component in dept_descriptions:
            path_desc.append(f"[{component}: {dept_descriptions[component]}]")
            
        # Subdepartment description
        elif component in subdept_descriptions:
            path_desc.append(f"[{component}: {subdept_descriptions[component]}]")
            
        # Year folder
        elif component.isdigit() and len(component) == 4:
            path_desc.append(f"[Year {component}]")
            
        # Month folder
        elif component.isdigit() and len(component) == 2:
            path_desc.append(f"[Month {component}]")
            
        # Special folders (version, priority, team, project)
        else:
            for special_type in special_folder_descriptions:
                if component.startswith(special_type):
                    identifier = component.split('_')[1]
                    path_desc.append(f"[{component}: {special_folder_descriptions[special_type]} #{identifier}]")
                    break
    
    return ' → '.join(path_desc)

def generate_file_description(department, file_name):
    # [Previous generate_file_description function remains the same]
    # Base descriptions for different file types
    descriptions = {
        'finance': {
            'quarterly': 'Financial performance report containing P&L statements, balance sheets, and cash flow data',
            'balance': 'Balance sheet with assets, liabilities, and equity breakdown',
            'transactions': 'Record of daily financial transactions and adjustments',
            'audit': 'Internal audit findings and compliance verification records',
            'tax': 'Annual tax return documentation and supporting schedules'
        },
        'hr': {
            'employee': 'Company policies, procedures, and employee guidelines',
            'training': 'Employee training software with interactive modules',
            'benefits': 'Employee benefits package details and enrollment information',
            'staff': 'Encrypted database of employee records and history',
            'payroll': 'Bi-weekly payroll processing batch file'
        },
        'it': {
            'system': 'Critical system update package with security fixes',
            'security': 'Microsoft security patch for vulnerability remediation',
            'backup': 'Daily system backup archive with incremental changes',
            'config': 'System configuration settings and parameters',
            'api': 'API documentation with endpoints and usage examples'
        },
        'operations': {
            'customer': 'Encrypted customer personal and account information',
            'risk': 'Monthly risk assessment reports and metrics',
            'daily': 'Daily transaction logs with processing status',
            'fraud': 'Rule sets for fraud detection system',
            'operations': 'Standard operating procedures and guidelines'
        },
        'legal': {
            'contract': 'Standard contract templates with legal annotations',
            'compliance': 'Regulatory compliance audit reports',
            'case': 'Active legal case files and supporting documents',
            'legal': 'Internal legal department guidelines and procedures',
            'regulatory': 'Regulatory filing documents and submissions'
        }
    }
    
    file_lower = file_name.lower()
    for key, desc in descriptions[department].items():
        if key in file_lower:
            if 'v' in file_name:
                version = file_name.split('v')[1].split('.')[0]
                desc += f" (Version {version})"
            if any(year in file_name for year in ['2020', '2021', '2022', '2023', '2024']):
                for year in ['2020', '2021', '2022', '2023', '2024']:
                    if year in file_name:
                        desc += f" - Year {year}"
                        break
            return desc
            
    return "General internal document with restricted access"

def generate_complex_path():
    # [Previous path generation code remains the same]
    roots = ['/cloud', '/local', '/network', '/backup', '/archive']
    
    departments = {
        'finance': ['accounting', 'payroll', 'audit', 'tax', 'investments'],
        'hr': ['recruitment', 'benefits', 'training', 'personnel', 'compliance'],
        'it': ['infrastructure', 'security', 'development', 'support', 'systems'],
        'operations': ['transactions', 'customer_service', 'risk', 'fraud', 'reporting'],
        'legal': ['contracts', 'regulations', 'cases', 'policies', 'documentation']
    }
    
    file_types = {
        'finance': [
            'quarterly_report_Q{}_FY{}.xlsx'.format(random.randint(1,4), random.randint(2020,2024)),
            'balance_sheet_{}.pdf'.format(datetime.now().strftime('%Y%m')),
            'transactions_{}.csv'.format(random.randint(10000,99999)),
            'audit_log_{}.txt'.format(datetime.now().strftime('%Y%m%d')),
            'tax_return_{}.pdf'.format(random.randint(2020,2024))
        ],
        'hr': [
            'employee_handbook_v{}.pdf'.format(random.randint(1,5)),
            'training_module_{}.exe'.format(random.randint(100,999)),
            'benefits_plan_{}.docx'.format(datetime.now().year),
            'staff_records.db',
            'payroll_batch_{}.dat'.format(random.randint(1000,9999))
        ],
        'it': [
            'system_patch_{}.exe'.format(random.randint(1000,9999)),
            'security_update_KB{}.msi'.format(random.randint(100000,999999)),
            'backup_{}.tar.gz'.format(datetime.now().strftime('%Y%m%d')),
            'config_{}.xml'.format(random.randint(100,999)),
            'api_documentation_v{}.html'.format(random.randint(1,10))
        ],
        'operations': [
            'customer_data_{}.encrypted'.format(random.randint(1000,9999)),
            'risk_assessment_{}.xlsx'.format(datetime.now().strftime('%Y%m')),
            'daily_transactions_{}.log'.format(datetime.now().strftime('%Y%m%d')),
            'fraud_detection_rules.json',
            'operations_manual_v{}.pdf'.format(random.randint(1,5))
        ],
        'legal': [
            'contract_template_{}.docx'.format(random.randint(100,999)),
            'compliance_report_{}.pdf'.format(datetime.now().year),
            'case_files_{}.zip'.format(random.randint(1000,9999)),
            'legal_guidelines_v{}.pdf'.format(random.randint(1,5)),
            'regulatory_submission_{}.xml'.format(random.randint(1000,9999))
        ]
    }
    
    # Generate path components
    root = random.choice(roots)
    department = random.choice(list(departments.keys()))
    subdepartment = random.choice(departments[department])
    year = str(random.randint(2020, 2024))
    month = f"{random.randint(1,12):02d}"
    
    extra_depth = [
        f"version_{random.randint(1,5)}",
        f"priority_{random.randint(1,3)}",
        f"team_{random.randint(1,10)}",
        f"project_{random.choice(['alpha','beta','gamma','delta'])}"
    ]
    
    selected_extra_depth = random.sample(extra_depth, random.randint(0,2))
    
    # Build the path
    path_components = [root, department, subdepartment, year, month] + selected_extra_depth
    path = '/'.join(path_components)
    
    # Add file
    file = random.choice(file_types[department])
    
    # Generate descriptions
    folder_description = generate_folder_description(path_components)
    file_description = generate_file_description(department, file)
    
    return f"{path}/{file}", folder_description, file_description

def generate_user_data(num_records=5000):
    roles = ['sys_admin', 'software_dev', 'bank_manager', 'bank_clerk', 'consumer']
    
    data = []
    for i in range(num_records):
        user_id = f"UID{random.randint(100000, 999999)}"
        role = random.choice(roles)
        file_path, folder_description, file_description = generate_complex_path()
        
        access_chance = {
            'sys_admin': 0.95,
            'software_dev': 0.8,
            'bank_manager': 0.7,
            'bank_clerk': 0.5,
            'consumer': 0.2
        }
        
        if any(sensitive in file_path.lower() for sensitive in ['security', 'audit', 'encrypted', 'compliance']):
            access_chance = {k: v * 0.7 for k, v in access_chance.items()}
        
        access_granted = random.random() < access_chance[role]
        
        data.append([user_id, role, file_path, folder_description, file_description, access_granted])
    
    return data

def save_to_csv(data, filename='user_access_data.csv'):
    headers = ['User_ID', 'Role', 'File_Path', 'Folder_Description', 'File_Description', 'Access_Granted']
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    user_data = generate_user_data(50000)
    save_to_csv(user_data)
    print(f"Generated {len(user_data)} records of synthetic user access data")