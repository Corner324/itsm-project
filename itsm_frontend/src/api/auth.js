import axios from "axios";
import { API_URL } from "@/config.js";

const API_URL_AUTH = `${API_URL}/api/auth/`;

export const register = (userData) => {
  return axios.post(`${API_URL_AUTH}register/`, userData);
};

export const login = (credentials) => {
  return axios.post(`${API_URL_AUTH}login/`, credentials);
};

export const refreshToken = (token) => {
  return axios.post(`${API_URL_AUTH}refresh/`, { refresh: token });
};

export const getAuthToken = () => {
  return localStorage.getItem("accessToken");
};

export const refreshAuthToken = async () => {
  const refreshTokenFromStorage = localStorage.getItem("refreshToken");
  if (!refreshTokenFromStorage) {
    throw new Error("No refresh token available");
  }

  try {
    const response = await axios.post(`${API_URL_AUTH}refresh/`, { refresh: refreshTokenFromStorage });
    const newAccessToken = response.data.access;
    localStorage.setItem("accessToken", newAccessToken);
    return newAccessToken;
  } catch (error) {
    console.error("Ошибка при обновлении токена", error);
    throw error;
  }
};


export const getIncidents = async () => {
  try {
    let token = getAuthToken();
    if (!token) {
      throw new Error("No access token found");
    }

    const response = await axios.get(`${API_URL}/api/incidents/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    return response.data;
  } catch (error) {
    if (error.response && error.response.status === 401) {
      const newToken = await refreshAuthToken();
      const response = await axios.get(`${API_URL}/api/incidents/`, {
        headers: {
          Authorization: `Bearer ${newToken}`,
        },
      });
      return response.data;
    } else {
      console.error("Ошибка при загрузке данных", error);
      throw error;
    }
  }
};
