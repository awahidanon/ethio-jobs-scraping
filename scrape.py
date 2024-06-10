import requests

def get_jobs_in_afar():
    base_url = 'http://api.ethiojobs.net/ethiojobs/api/job-board/jobs?search=Afar'
    page = 1
    jobs = []

    while True:
        url = f'{base_url}&page={page}'
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page: {response.status_code}")
            break

        data = response.json()
        
        # Extract job listings from the JSON data
        job_listings = data.get('data', [])
        
        if not job_listings:
            break  # Exit the loop if no job listings are found

        for job in job_listings:
            title = job.get('title', 'N/A')
            company = job.get('company', {}).get('name', 'N/A')
            location = job.get('city', 'N/A')
            link = job.get('career_page_link', 'N/A')
            state = job.get('state', 'N/A')

            # Check if the job state is Afar
            if state == 'Afar' or "Afar Region":
                jobs.append({
                    'title': title,
                    'company': company,
                    'location': location,
                    'link': link
                })
        
        # Pagination info
        meta = data.get('meta', {})
        if page >= meta.get('last_page', 1):
            break
        page += 1

    return jobs

# Run the function and print the jobs
afar_jobs = get_jobs_in_afar()
for idx, job in enumerate(afar_jobs, start=1):
    print(f"{idx}. {job['title']} at {job['company']} - {job['location']} ({job['link']})")

if not afar_jobs:
    print("No jobs found in the Afar region.")
