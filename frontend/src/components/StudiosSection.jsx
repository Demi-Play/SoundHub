import { useEffect, useState } from 'react';
import apiClient from '../../services/api';

const StudiosSection = () => {
  const [studios, setStudios] = useState([]);

  useEffect(() => {
    apiClient.get('/studios/')
      .then(res => setStudios(res.data.slice(0, 3)))
      .catch(err => console.error(err));
  }, []);

  return (
    <section className="py-20 bg-gray-100">
      <div className="container mx-auto">
        <h2 className="text-3xl font-bold text-center mb-12">Popular Studios</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {studios.map(studio => (
            <div key={studio.id} className="bg-white p-6 rounded-lg shadow-md">
              <h3 className="text-xl font-bold mb-2">{studio.name}</h3>
              <p className="text-gray-600 mb-4">{studio.address}</p>
              <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                Book Now
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default StudiosSection;