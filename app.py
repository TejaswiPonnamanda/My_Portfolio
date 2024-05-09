from cmath import phase
import json
from os import link
import requests
import pandas as pd
from flask import Flask,request,render_template

app = Flask(__name__)

print("Reading Basic Info Excel File...")
df_basic_info = pd.read_excel(r"C:\webdevusingflask\data.xlsx",sheet_name='Basic Info')
print("Basic Info DataFrame:")
print(df_basic_info)

df_basic_info.fillna('', inplace=True)
print("Filled Basic Info DataFrame:")
print(df_basic_info)

name = df_basic_info[df_basic_info['Column']=='Name']['Value'].values[0]
print("Name:", name)

@app.route('/')
def home():
    print("Rendering Home Page...")
    name = df_basic_info[df_basic_info['Column']=='Name']['Value'].values[0]
    print("Name in Home Route:", name)
    designation = df_basic_info[df_basic_info['Column']=='Designation']['Value'].values[0]
    print("Designation:", designation)
    description = df_basic_info[df_basic_info['Column']=='Description']['Value'].values[0]
    print("Description:", description)
    photo = df_basic_info[df_basic_info['Column']=='Photo']['Value'].values[0]
    print("Photo:", photo)
    github = df_basic_info[df_basic_info['Column']=='GitHub Profile Link']['Value'].values[0]
    print("GitHub Profile Link:", github)
    linkedin = df_basic_info[df_basic_info['Column']=='LinkedIn Profile Link']['Value'].values[0]
    print("LinkedIn Profile Link:", linkedin)
    leetcode = df_basic_info[df_basic_info['Column']=='Leetcode Link']['Value'].values[0]
    print("Leetcode Link:", leetcode)
    email = df_basic_info[df_basic_info['Column']=='Email Id']['Value'].values[0]
    print("Email Id:", email)

    return render_template('home.html',name=name,designation=designation,description=description,photo=photo,
                            github=github,linkedin=linkedin,leetcode=leetcode,email=email)

@app.route('/skills')
def skills():
    print("Reading Skills Excel File...")
    df_skills = pd.read_excel(r"C:\webdevusingflask\data.xlsx",sheet_name='Skills')
    print("Skills DataFrame:")
    print(df_skills)

    df_skills.fillna('', inplace=True)
    print("Filled Skills DataFrame:")
    print(df_skills)

    d = {}
    for i in range(len(df_skills)):
        skill = df_skills.iloc[i]['Skill']
        image = df_skills.iloc[i]['Image']
        experience = df_skills.iloc[i]['Experience']
        d[skill]={}
        d[skill]['image']=image
        d[skill]['experience']=experience
        
    print("Skill Info:")
    print(d)

    return render_template('skills.html', skillinfo=d, name=name)

@app.route('/education')
def education():
    print("Reading Education Excel File...")
    df_education = pd.read_excel(r"C:\webdevusingflask\data.xlsx",sheet_name='Education')
    print("Education DataFrame:")
    print(df_education)

    df_education.fillna('', inplace=True)
    print("Filled Education DataFrame:")
    print(df_education)

    d = {}
    for i in range(len(df_education)):
        institute = df_education.iloc[i]['Institute']
        degree = df_education.iloc[i]['Degree']
        date = df_education.iloc[i]['Date']
        extrainfo = df_education.iloc[i]['Extra Info']
        image = df_education.iloc[i]['Image']
        d[institute]={}
        d[institute]['degree']=degree
        d[institute]['date']=date
        d[institute]['extrainfo']=extrainfo
        d[institute]['image']=image  
    print("Education Info:")
    print(d)

    return render_template('education.html',educationinfo=d,name=name)

@app.route('/experience')
def experience():
    print("Reading Experience Excel File...")
    df_experience = pd.read_excel(r"C:\webdevusingflask\data.xlsx",sheet_name='Experience')
    print("Experience DataFrame:")
    print(df_experience)

    df_experience.fillna('', inplace=True)
    print("Filled Experience DataFrame:")
    print(df_experience)

    d = {}
    for i in range(len(df_experience)):
        designation = df_experience.iloc[i]['Designation']
        company = df_experience.iloc[i]['Company']
        image = df_experience.iloc[i]['Image']
        date = df_experience.iloc[i]['Date']
        info = df_experience.iloc[i]['Info']
        d[company]={}
        d[company]['designation']=designation
        d[company]['image']=image
        d[company]['date']=date
        d[company]['info']=info
    print("Experience Info:")
    print(d)

    return render_template('experience.html',experienceinfo=d,name=name)

@app.route('/projects')
def projects():
    print("Reading Projects Excel File...")
    df_projects = pd.read_excel(r"C:\webdevusingflask\data.xlsx", sheet_name='Projects')
    print("Projects DataFrame:")
    print(df_projects)

    df_projects.fillna('', inplace=True)
    print("Filled Projects DataFrame:")
    print(df_projects)

    d = {}
    for i in range(len(df_projects)):
        projectname = df_projects.iloc[i]['Project Name']
        description = df_projects.iloc[i]['Description']
        image = df_projects.iloc[i]['Image']
        date = df_projects.iloc[i]['Date']
        github_link = df_projects.iloc[i]['GitHub Link']  # Add this line to fetch GitHub link
        d[projectname] = {}
        d[projectname]['image'] = image
        d[projectname]['description'] = description
        d[projectname]['date'] = date
        d[projectname]['github_link'] = github_link  # Add GitHub link to project info
    print("Project Info:")
    print(d)

    return render_template('projects.html', projectinfo=d, name=name)

@app.route('/resume')
def resume():
    print("Reading Resume Excel File...")
    df_basic_info.fillna('',inplace=True)
    resumelink = df_basic_info[df_basic_info['Column']=='Resume Link']['Value'].values[0]
    print("Resume Link:", resumelink)

    return render_template('resume.html',resumelink=resumelink,name=name)


if __name__ == '__main__':
    app.run(debug=True)
