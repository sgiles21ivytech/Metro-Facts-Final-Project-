import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const loginUser = async ({ email, password }) => {
  try {
    const res = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    if (res.ok) {
      localStorage.setItem("user", JSON.stringify(data.user));
      return true;
    }
    return false;
  } catch (error) {
    console.error("Login error:", error);
    return false;
  }
};

export const getUsers = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/users`);
    return response.data;
  } catch (error) {
    console.error("Get users error:", error);
    return [];
  }
};