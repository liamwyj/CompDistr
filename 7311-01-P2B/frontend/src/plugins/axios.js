// src/plugins/axios.js
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: 'https://compdistr.onrender.com', // URL servidor Flask
});

export default axiosInstance;
