// src/plugins/axios.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:9000', // URL servidor Flask
});

export default axiosInstance;
