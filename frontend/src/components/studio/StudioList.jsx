import { useEffect, useState } from 'react';
import { getStudios } from '../../services/api';
import StudioCard from './StudioCard';

const StudioList = () => {
  const [studios, setStudios] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStudios = async () => {
      const data = await getStudios();
      setStudios(data);
      setLoading(false);
    };
    
    fetchStudios();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="studio-grid">
      {studios.map(studio => (
        <StudioCard key={studio.id} studio={studio} />
      ))}
    </div>
  );
};

export default StudioList;