import axios from 'axios';

const api = axios.create({ baseURL: 'http://localhost:8000' });

export const fetchInsights = () => api.get('/insights');
export const fetchPrediction = days => api.get(`/predict/${days}`);

export default api;