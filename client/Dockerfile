FROM node:12.10.0
WORKDIR /usr/app
ADD . /usr/app
RUN npm install --silent
RUN npm install -g react-scripts@3.3.0 --silent
CMD ["npm", "start"]