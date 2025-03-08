import { io } from 'socket.io-client';

const socket = io(import.meta.env.VITE_SOCKET_URL || 'ws://localhost:8000/ws', {
  autoConnect: false,
  withCredentials: true,
});

export const useSocket = () => {
  return socket;
};