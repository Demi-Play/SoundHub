import { createContext, useContext, useEffect, useState } from 'react';
import apiClient from '../services/api';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const login = async (username, password) => {
    const { data } = await apiClient.post('/token/', { username, password });
    localStorage.setItem('access_token', data.access);
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${data.access}`;
    setUser(data.user);
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    delete apiClient.defaults.headers.common['Authorization'];
    setUser(null);
  };

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      // Здесь можно добавить запрос для получения данных пользователя
      const fetchUser = async () => {
        try {
          const { data } = await apiClient.get('/users/me/');
          setUser(data);
        } catch (error) {
          console.error('Error fetching user data:', error);
          logout();
        }
      };
      fetchUser();
    }
  }, []);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);