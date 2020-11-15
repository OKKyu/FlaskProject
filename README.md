# Name
  FlaskProject

# overview
  This project is created for author's learn and practice about flask web framework.  
  Andalso, purpose of coding efficiency by reuse this template.  

# Requirement
  python3, python3-venv

# Download
  please copy you to your any directory. 

# setup
 please run setup.sh  
 first,  virtual environment is maked in "FlaskProject/venv/"
 second, updating pip in virtual environment.
 third,  dependency library is imported by pip requirements.txt

# run
 please type shell below.
   run run.sh  worker-num  hostname(ip address) portnum
 
 This shell use gunicorn with WSGI.
 if you want to use other WSGI, you can overwirte this shell source.
 
# Usage

# Structure

- `FlaskProject/main.py` Flask app (entry point)  
- `FlaskProject/templates/` webpages. htmls.  
- `FlaskProject/static/`    static contents. css, image, media, other contents  
- `FlaskProject/env/`        config files  
- `FlaskProject/data/`       data files. csv, text, etc...  
- `FlaskProject/dao/`       data access objects. python scripts  
- `FlaskProject/venv/`      vurtualenv folder. auto generated by setup.sh  
- `FlaskProject/README.md`  explanation about Web application that implementated by this project  
- `FlaskProject/about_project.txt`  this project's explanation  
- `FlaskProject/run.sh`             execute this web application on WSGI (gunicorn)  
- `FlaskProject/setup.sh`           setup about this web application   

# Lisense
   please writing below about license.  
   for example  
   
   FlaskProject version 1.0.0  
   (c) 2020 OKKyu allrights reserved under MIT license.  
   
## Author
OKKyu
