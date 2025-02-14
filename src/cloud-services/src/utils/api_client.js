 // src/utils/api_client.js
    const axios = require('axios');

    async function fetchData(url) {
        try {
        const response = await axios.get(url);
        return response.data;
        } catch (error) {
          console.error("Error fetching data:", error);
         throw error;
        }
     }
    module.exports = { fetchData };
    ```
