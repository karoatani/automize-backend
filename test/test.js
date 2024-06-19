// const myHeaders = new Headers();
// myHeaders.append("Content-Type", "application/json");

// const raw = JSON.stringify({
//   "username": "admin",
//   "password": "babe"
// });

// const requestOptions = {
//   method: "POST",
//   headers: myHeaders,
//   body: raw,
//   redirect: "follow"
// };

// fetch("http://127.0.0.1:8000/api/v1/accounts/login/", requestOptions)
//   .then((response) => response.text())
//   .then((result) => console.log(result))
//   .catch((error) => console.error(error));

// const myHeaders = new Headers();
// myHeaders.append("Content-Type", "application/json");
// myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NjA1MDU4LCJpYXQiOjE3MTg1NzUwNTgsImp0aSI6IjIwZmJmMzcxMTQwOTRlYjBiYWIwMmNhZjJiNmZkYWEwIiwidXNlcl9pZCI6MX0.phgXtiov4k-g_6m7SXe1HsOVYMy-e-ogLrwgkprJoHk");
// document.cookie = 'Authorization=' + "Bearer ."



// // Define the WebSocket endpoint

// const socket = new WebSocket('ws://'+ "127.0.0.1:8000"
//             + '/ws/notifications/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NjkxMjU1LCJpYXQiOjE3MTg2NjEyNTUsImp0aSI6IjhlNWE3Y2RlY2IzMjRiYTNhOWI5ZDg5MGFjY2U2MmMwIiwidXNlcl9pZCI6MX0._J9aNkH7JRmFpYxJVLbhLomucYvRFOpkg4pS0n3t_nU');

// // WebSocket event listeners
// socket.onopen = function(event) {
//   console.log('WebSocket connection established.');
//   // You can send messages to the server once the connection is open
//   socket.send(JSON.stringify({
//     "token": "token text--"
//   }));

 
// }
// socket.onmessage = function(event) {
//   console.log('Message from server:', event.data);
//   // Handle incoming messages from the server
// };

// socket.onclose = function(event) {
//   console.log('WebSocket connection closed:', event.code, event.reason);
//   // Handle closed connection
// };

// socket.onerror = function(error) {
//   console.error('WebSocket error:', error);
//   // Handle any errors that occur.
// };

// myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NDcwMzMxLCJpYXQiOjE3MTg0NDAzMzEsImp0aSI6IjZjYjcxY2JlM2IyZDQ3OTY4M2E5NmJhODQ5OGMwNzk4IiwidXNlcl9pZCI6MX0.WxaiuUB2AfNapGealoxeLtUGqIdiKThRQhq7wKD-PjQ");


const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify({
  "username": "admin",
  "password": "babe"
});

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/login/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));