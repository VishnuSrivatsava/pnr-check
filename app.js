const express = require('express');
const axios = require('axios');
const app = express();

app.set('view engine', 'ejs');

app.get('/', async (req, res) => {
    const apiUrls = [
        "https://pnr-status-for-railways-api.onrender.com/status?pnr=4822030912",
        "https://pnr-status-for-railways-api.onrender.com/status?pnr=2316268170"
    ];

    let dataList = [];

    for (let apiUrl of apiUrls) {
        try {
            const response = await axios.get(apiUrl);
            dataList.push(response.data);
        } catch (error) {
            console.error(`Failed to retrieve data for ${apiUrl}. Status code:`, error.response.status);
            dataList.push({});
        }
    }

    res.render('index', { dataList: dataList });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
