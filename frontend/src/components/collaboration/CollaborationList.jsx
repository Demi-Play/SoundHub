// components/collaboration/CollaborationList.jsx
import { useEffect, useState } from 'react';
import { getCollaborations } from '../../services/api';

const CollaborationList = () => {
  const [collabs, setCollabs] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getCollaborations();
      setCollabs(data);
    };
    fetchData();
  }, []);

  return (
    <div>
      {collabs.map(collab => (
        <div key={collab.id}>
          <h3>{collab.project_name}</h3>
          <p>Status: {collab.status}</p>
          <p>Participants: {collab.participants.join(', ')}</p>
        </div>
      ))}
    </div>
  );
};