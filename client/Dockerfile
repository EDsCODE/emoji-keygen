FROM node:12.10.0
WORKDIR /usr/app
ADD . /usr/app
RUN yarn
RUN yarn build
CMD ["npm", "start"]