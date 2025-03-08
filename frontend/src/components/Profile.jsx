import { useAuth } from '../context/AuthContext.jsx';
import { useEffect, useState } from 'react';
import apiClient from '../services/api';

const Profile = () => {
  const { user } = useAuth();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    if (user) {
      apiClient.get('/profiles/')
        .then(res => setProfile(res.data));
    }
  }, [user]);

  if (!user) return <div>Please login</div>;

  return (
    <div>
      <h2>{profile?.user?.username}</h2>
      <p>{profile?.bio}</p>
    </div>
  );
};

export default Profile;