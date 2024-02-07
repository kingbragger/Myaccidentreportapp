import requests

# URL for the local development server
BASE_URL = 'http://127.0.0.1:5000'

# Function to simulate submitting an accident report
def submit_report(date, location, description):
    report_data = {
        'date': date,
        'location': location,
        'description': description
    }
    response = requests.post(f'{BASE_URL}/submit', data=report_data)
    return response

# Function to simulate viewing accident reports
def view_reports():
    response = requests.get(BASE_URL)
    return response

# Demo
if __name__ == '__main__':
    # Submitting a report
    print("Submitting a demo accident report...")
    submit_response = submit_report('2024-02-07', 'Intersection A', 'Car collision')
    print(submit_response.text)

    # Viewing reports
    print("\nViewing accident reports...")
    view_response = view_reports()
    print(view_response.text)
