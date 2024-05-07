import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setSchool(schoolName, value) {
  client.set(schoolName, value, print);
};

function displaySchool(schoolName) {
  client.get(schoolName, function(error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  });
}

displaySchool('Holberton');
setSchool('HolbertonSanFrancisco', '100');
displaySchool('HolbertonSanFrancisco');