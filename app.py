from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
# Add this line to avoid GUI issues
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_data')
def show_data():
    df = pd.read_csv('/Users/banawata/Documents/Ironhack/projetfinal/data/clean/cleaned_data2.csv')
    print(df.head())
    # Convert DataFrame to HTML
    table_html = df.to_html(classes='data', header='true')
    print(table_html)
    return render_template('showdata.html', table=table_html)

@app.route('/statistics')
def statistics():
    df = pd.read_csv('/Users/banawata/Documents/Ironhack/projetfinal/data/clean/cleaned_data2.csv')

    # Define job_role_mapping
    job_role_mapping = {0: 'HR', 1: 'Data Scientist', 2: 'Software Engineer', 
                        3: 'Sales', 4: 'Marketing', 5: 'Designer', 6: 'Project Manager'}

    # Map non-numeric values in 'Productivity_Change' to numeric equivalents
    productivity_mapping = {'Increase': 1, 'No Change': 0, 'Decrease': -1}
    df['Productivity_Change'] = df['Productivity_Change'].map(productivity_mapping)

    # Group by work location and calculate average productivity change
    work_location_stats = df.groupby('Work_Location')['Productivity_Change'].mean()

    # Mean work-life balance by job role
    job_role_stats_raw = df.groupby('Job_Role')['Work_Life_Balance_Rating'].mean().to_dict()
    job_role_stats = {job_role_mapping.get(k, "Unknown"): v for k, v in job_role_stats_raw.items()}

    # Calculate average hours worked per week
    avg_hours_worked = df['Hours_Worked_Per_Week'].mean()

    # Create and save the work-life balance graph
    job_roles = list(job_role_stats.keys())
    work_life_balance = list(job_role_stats.values())

    plt.figure(figsize=(10, 6))
    plt.bar(job_roles, work_life_balance, color='skyblue')
    plt.xlabel('Job Role')
    plt.ylabel('Average Work-Life Balance')
    plt.title('Work-Life Balance by Job Role')
    plt.savefig('static/img/work_life_balance.png')

    # Additional visualization: Work Location vs Productivity Change
    plt.figure(figsize=(10, 6))
    work_location_stats.plot(kind='bar', color='lightblue')
    plt.title('Average Productivity Change by Work Location')
    plt.xlabel('Work Location')
    plt.ylabel('Average Productivity Change')
    plt.savefig('static/img/productivity_vs_work_location.png')

    # Additional visualization: Stress Levels vs Job Roles
    job_role_stress = df.groupby('Job_Role')['Stress_Level'].mean()
    plt.figure(figsize=(10, 6))
    job_role_stress.plot(kind='bar', color='salmon')
    plt.title('Average Stress Level by Job Role')
    plt.xlabel('Job Role')
    plt.ylabel('Average Stress Level')
    plt.savefig('static/img/stress_vs_job_roles.png')

    # Pass all stats and graph info to the template (only one return)
    return render_template('statistics.html', 
                           job_role_stats=job_role_stats, 
                           avg_hours_worked=avg_hours_worked)

if __name__ == '__main__':
    app.run(debug=True)
