FROM node:12.10.0
WORKDIR /usr/app
ADD . /usr/app
RUN yarn
RUN yarn build
RUN npm install -g react-scripts@3.3.0 --silent
CMD ["npm", "start"]