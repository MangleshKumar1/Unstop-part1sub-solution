# Sample job data with required skills
job_data = {
    'Job Title': ['Data Scientist', 'Web Developer', 'AI Engineer', 'Mobile App Developer'],
    'Skills': ['Python, Machine Learning, Data Analysis', 'HTML, CSS, JavaScript', 'Python, TensorFlow, Neural Networks', 'Java, Kotlin, Android Studio']
}

# Taking User skills input (example)
user_skills = 'Python, Machine Learning, IoT'

# Function to recommend jobs based on user skills
def recommend_jobs(user_skills, job_data):
    recommended_jobs = []
    for idx, job in enumerate(job_data['Job Title']):
        required_skills = job_data['Skills'][idx]
        if all(skill.strip().lower() in user_skills.lower() for skill in required_skills.split(',')):
            recommended_jobs.append(job)
    return recommended_jobs

# Get job recommendations for the user skills
recommended_jobs = recommend_jobs(user_skills, job_data)
print(recommended_jobs)