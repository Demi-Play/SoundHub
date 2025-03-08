import { useParams } from 'react-router-dom';
import { bookStudio } from '../../services/api';

const Booking = () => {
  const { id } = useParams();
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const data = await bookStudio(id, `${date} ${time}`);
      console.log('Booking success:', data);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Book Studio {id}</h2>
      <input 
        type="date" 
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <input 
        type="time" 
        value={time}
        onChange={(e) => setTime(e.target.value)}
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Booking...' : 'Confirm'}
      </button>
    </div>
  );
};

export default Booking;