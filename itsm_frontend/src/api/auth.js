import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/auth/";

export const register = (userData) => {
  return axios.post(`${API_URL}register/`, userData);
};

export const login = (credentials) => {
  return axios.post(`${API_URL}login/`, credentials);
};

export const refreshToken = (token) => {
  return axios.post(`${API_URL}refresh/`, { refresh: token });
};
