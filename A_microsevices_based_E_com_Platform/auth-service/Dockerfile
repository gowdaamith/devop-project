#Efficient docker file should have the follow the following thinngs\
#Reduce image size
#Caching dependencies properly
#Using --upgrade pip
#Avoid copying unnecessary files 
#using python  -m pip to avoid path issue

#Use official lightweight python image 

FROM python:3.10-slim AS build


#set the working directory
WORKDIR /app

#copy only the requirement for caching 
COPY requirements.txt .

#install dependencies
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir -r requirements.txt

#copy only the application 
COPY . .

#Expose the port(adjust for each services)
EXPOSE 5001

#RUN THE APP
CMD ["python","app.py"]
