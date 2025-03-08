import { useEffect, useState } from 'react';
import apiClient from '../services/api';
import { useSocket } from '../services/socket';

const StudioBooking = ({ studioId }) => {
  const [slots, setSlots] = useState([]);
  const socket = useSocket();

  useEffect(() => {
    apiClient.get(`/slots/?studio=${studioId}`)
      .then(res => setSlots(res.data));
  }, [studioId]);

  useEffect(() => {
    socket.connect();
    socket.emit('join_room', `studio_${studioId}`);

    socket.on('booking_update', (data) => {
      setSlots(prev => 
        prev.map(slot => 
          slot.id === data.id ? data : slot
        )
      );
    });

    return () => {
      socket.disconnect();
    };
  }, [studioId, socket]);

  const handleBook = (slotId) => {
    apiClient.post('/bookings/', { slot: slotId })
      .then(res => {
        // Обработка успешного бронирования
      });
  };

  return (
    <div>
      {slots.map(slot => (
        <div key={slot.id}>
          {slot.start_time} - {slot.end_time}
          <button onClick={() => handleBook(slot.id)}>Book</button>
        </div>
      ))}
    </div>
  );
};

export default StudioBooking;