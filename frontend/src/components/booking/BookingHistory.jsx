// components/booking/BookingHistory.jsx
import { useEffect, useState } from 'react';
import { getBookings } from '../../services/api';

const BookingHistory = () => {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getBookings();
      setBookings(data);
    };
    fetchData();
  }, []);

  return (
    <div>
      {bookings.map(booking => (
        <div key={booking.id}>
          <h3>{booking.studio.name}</h3>
          <p>Date: {new Date(booking.time).toLocaleString()}</p>
          <p>Status: {booking.status}</p>
        </div>
      ))}
    </div>
  );
};