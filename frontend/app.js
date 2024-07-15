// app.js

const express = require('express');
const app = express();
const path = require('path');
const axios = require('axios');

// Backend service URL
const backendUrl = 'http://localhost:3000/greet';
app.use('/favicon.ico', express.static(path.join(__dirname, 'public', 'favicon.ico')));

app.get('/', async (req, res) => {
    try {
        // Make a request to the backend service
        const response = await axios.get(backendUrl);
        const greeting = response.data.message;
        console.log("TEST", response)

        // Serve the greeting message
        res.send(`<h1 id = "test" class="message">${greeting}</h1>`);
    } catch (error) {
        console.error(error); 
        res.send('<h1 id = "test" class="message">Hello, World!</h1>');
    }
});

const port = 8080;
app.listen(port, () => {
    console.log(`Frontend service running on port ${port}`);
});

